import logging

class FallbackEngine:
    """Routes generation to ensure a report is ALWAYS created."""
    def __init__(self, local_llm_func, cloud_llm_func, rule_based_func):
        self.local_llm = local_llm_func
        self.cloud_llm = cloud_llm_func
        self.rule_based = rule_based_func

    def generate(self, prompt, data):
        try:
            logging.info("Attempting Local LLM (Ollama)...")
            return self.local_llm(prompt)
        except Exception:
            try:
                logging.info("Local failed. Attempting Cloud Fallback (Groq)...")
                return self.cloud_llm(prompt)
            except Exception:
                logging.warning("AI Generation failed. Triggering Clinical Rules Engine.")
                return self.rule_based(data)