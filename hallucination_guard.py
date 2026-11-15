def verify_rag_context(rag_chunks: list) -> bool:
    """Ensures the LLM does not answer without medical evidence."""
    if not rag_chunks or len(rag_chunks) == 0:
        return False
    return True