from mcp.server.fastmcp import FastMCP
from mcp.types import PromptReference, Completion
from pydantic import Field
from mcp.server.fastmcp.prompts import base
mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a file and return it as string."
)
def read_document(
    doc_id: str = Field(description="ID of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]

@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the document contents with a new string."
)
def edit_document(
    doc_id: str = Field(description="ID of the document that will be edited"),
    old_string: str = Field(description="The text to replace. Must match exactly, including case and punctuation."),
    new_string: str = Field(description="The new text to insert in place of the old text."),
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    if old_string not in docs[doc_id]:
        raise ValueError(f"String '{old_string}' not found in document '{doc_id}'")
    docs[doc_id] = docs[doc_id].replace(old_string, new_string)
    return f"Document '{doc_id}' updated successfully."

# Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())


@mcp.resource("docs://documents/", mime_type="application/json")
def list_docs_slash() -> list[str]:
    return list(docs.keys())

#Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with ID {doc_id} not found")
    return docs[doc_id]
# Write a prompt to rewrite a doc in markdown format

@mcp.prompt(
    name="format",
    description="Rewrite the contents of a document in markdown format."
)

def format_document(
    doc_id: str=Field(description="ID of the document to format")
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document using markdown syntax.

    The ID of the document you need to reformat is:
    <document_id>
    {doc_id}
    </document_id>

    Add headers, bullet points, tables, etc. as necessary. Feel free to use any markdown syntax that would be appropriate.
    Use the 'edit_document' tool to apply the changes. After the document is reformatted, return the newly formatted document contents as the final answer.
    """
    return [base.UserMessage(prompt)]


# TODO: Write a prompt to summarize a doc


@mcp.completion()
async def handle_completion(ref, argument, context):
    if isinstance(ref, PromptReference) and ref.name == "format" and argument.name == "doc_id":
        matches = [doc_id for doc_id in docs.keys() if argument.value.lower() in doc_id.lower()]
        return Completion(values=matches)
    return None


if __name__ == "__main__":
    mcp.run(transport="stdio")
