def validate_patient_inputs(data: dict) -> list:
    """Blocks impossible inputs from reaching the AI."""
    errors = []
    if not data.get("diagnosis"):
        errors.append("Diagnosis cannot be empty.")
        
    age = data.get("age")
    if age is None or not (0 <= float(age) <= 120):
        errors.append("Patient age must be between 0 and 120.")
        
    return errors