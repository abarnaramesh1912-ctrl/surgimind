def apply_hardcoded_safety_rules(age: float, diagnosis: str, admission_type: str) -> str:
    """Deterministic rules that override ML if absolute danger is detected."""
    diag_lower = diagnosis.lower()
    if "cardiac arrest" in diag_lower or "sepsis" in diag_lower:
        return "HIGH"
    if age > 75 and admission_type == "emergency":
        return "HIGH"
    return "UNKNOWN"