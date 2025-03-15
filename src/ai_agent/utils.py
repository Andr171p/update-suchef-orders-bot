from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from langchain_core.documents import Document


def format_docs(documents: List["Document"]) -> str:
    return "\n\n".join([document.page_content for document in documents])
