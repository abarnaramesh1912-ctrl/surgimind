<div align="center">

# 🩺 SurgiMind

### AI-Driven Distributed Surgical Support

*A research-oriented AI Clinical Decision Support System that combines Machine Learning, Retrieval-Augmented Generation (RAG), Explainable AI, and Multi-Tier AI Safety mechanisms to assist surgeons with evidence-based pre-operative risk assessment.*

</div>

---

# 💡 Inspiration

Pre-operative surgical risk assessment remains a complex process that depends heavily on physician experience and subjective judgment. In high-acuity environments, clinicians must rapidly evaluate multiple patient factors while ensuring every decision aligns with established clinical guidelines.

SurgiMind was developed to function as an **AI-powered Doctor Copilot** that assists surgeons by combining structured clinical prediction models with trustworthy retrieval-based reasoning.

Instead of replacing clinicians, SurgiMind provides explainable recommendations grounded in evidence from the **MIMIC-III Clinical Database** and validated surgical guidelines while maintaining strict AI safety through deterministic fallback mechanisms.

---

# 🏆 Highlights

### 🧠 Machine Learning Clinical Risk Prediction

- End-to-End Python ML Pipeline
- Scikit-learn Random Forest Classifier
- TF-IDF Clinical Text Vectorization
- Balanced Class Weights
- 100 Decision Trees
- **80.77% Prediction Accuracy**

---

### 📊 Weighted Multi-Signal Risk Engine

Instead of relying solely on machine learning, SurgiMind combines multiple clinical indicators into a deterministic weighted scoring system.

Signals include:

- Diagnosis Severity
- Patient Age
- Admission Type
- Abnormal Laboratory Count

These signals generate a **0–100 Risk Score**, categorizing patients into:

- 🔴 HIGH Risk
- 🟡 MEDIUM Risk
- 🟢 LOW Risk

---

### 🛡 AI Safety First

Unlike traditional AI assistants, SurgiMind prioritizes **clinical reliability over creativity**.

A **Three-Tier Safety Architecture** guarantees the system continues functioning even if AI models become unavailable.

**Tier 1**
Local LLMs using Ollama
- Qwen2.5
- Phi-3

↓

If unavailable...

**Tier 2**
Cloud LLM
- Groq Llama 3

↓

If unavailable...

**Tier 3**
Deterministic Clinical Rules Engine

This guarantees that the application always produces safe, rule-based recommendations.

---

### 📚 Retrieval-Augmented Generation (RAG)

To reduce hallucinations, SurgiMind never allows language models to answer using internal memory alone.

Instead, every response is grounded using:

- FAISS Vector Database
- Semantic Similarity Search
- 171 Surgical Guidelines
- Evidence Retrieval Pipeline

This architecture ensures recommendations remain evidence-based rather than speculative.

---

### 🔍 Explainable AI Dashboard

Built with Streamlit, the Glass Box Dashboard enables surgeons to understand exactly why the system produced a recommendation.

Features include:

- Prediction Confidence
- Clinical Evidence
- Retrieved Guidelines
- Risk Score Breakdown
- Red Flag Detector
- Laboratory Alerts

---

### 🔒 Secure Infrastructure

SurgiMind follows secure software engineering principles.

Security mechanisms include:

- Flask REST API
- PostgreSQL / SQLite
- PBKDF2-SHA256 Password Hashing
- HMAC Session Token Verification
- Secure Authentication

---

# ⚙️ What It Does

SurgiMind is an AI-powered Clinical Decision Support System that assists healthcare professionals during pre-operative evaluation.

The system combines machine learning, retrieval-augmented generation, deterministic reasoning, and explainable AI into a unified decision-support platform.

Core capabilities include:

- Clinical Risk Prediction
- Surgical Recommendation Assistance
- Medical Knowledge Retrieval
- Explainable AI
- Laboratory Analysis
- Risk Stratification
- AI Safety Enforcement
- Clinical Rule Validation

Rather than replacing physician expertise, SurgiMind augments clinical decision-making through transparent, evidence-backed recommendations.

---

# 🏆 Key Research Innovations

## 1. Hybrid Machine Learning + Rule-Based Risk Prediction

Combines statistical learning with deterministic medical scoring.

This hybrid architecture improves robustness while preserving interpretability.

---

## 2. Three-Tier AI Safety Architecture

The reasoning backend follows a cascading safety mechanism.

```
Local LLM (Ollama)

↓

Cloud LLM (Groq)

↓

Clinical Rules Engine
```

This guarantees uninterrupted clinical support even during AI model failures.

---

## 3. Hallucination Mitigation using RAG

Instead of allowing unrestricted text generation, every recommendation is grounded through semantic retrieval over indexed surgical guidelines.

This minimizes hallucinations while increasing factual consistency.

---

## 4. Explainable Glass Box Dashboard

Every recommendation displays:

- Risk Probability
- Weighted Score
- Retrieved Evidence
- Guideline References
- Prediction Confidence

No "black box" predictions are shown to clinicians.

---

## 5. Clinical Red Flag Detector

Automatically identifies abnormal laboratory findings and visually highlights critical values requiring immediate attention.

---

## 6. Distributed Modular Architecture

The application separates responsibilities into:

- Machine Learning
- Retrieval Engine
- LLM Gateway
- API Layer
- Database Layer
- Frontend Dashboard

This modular architecture improves maintainability and scalability.

---

# 📖 Detailed User Guide

## Step 1

Login securely.

Passwords are protected using PBKDF2-SHA256.

---

## Step 2

Upload or enter patient clinical information.

Examples include:

- Diagnosis
- Admission Type
- Age
- Laboratory Results

---

## Step 3

The Machine Learning model predicts the patient's surgical risk.

---

## Step 4

The Weighted Multi-Signal Engine computes the overall clinical score.

---

## Step 5

The RAG Pipeline retrieves relevant surgical guidelines.

---

## Step 6

The AI Safety Layer selects the safest reasoning backend.

Priority order:

1. Local Ollama
2. Groq Cloud
3. Clinical Rules Engine

---

## Step 7

The Streamlit Dashboard displays:

- Risk Level
- Supporting Evidence
- Clinical Explanation
- Retrieved Guidelines
- Red Flag Alerts

---

# 🧪 How to Test Core Features

## Test 1

Verify Machine Learning Prediction.

Upload a sample patient record and confirm the predicted risk category.

---

## Test 2

Disconnect Ollama.

The system should automatically switch to Groq.

---

## Test 3

Disable internet connectivity.

The Clinical Rules Engine should generate deterministic recommendations.

---

## Test 4

Upload abnormal laboratory values.

The Red Flag Detector should highlight critical findings.

---

## Test 5

Search clinical questions.

Verify that responses reference retrieved surgical guidelines instead of hallucinated information.

---

## Test 6

Inspect the Explainability Dashboard.

Ensure every recommendation includes supporting evidence and prediction confidence.

---

# 🚀 Deployment & Demo Setup Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/SurgiMind.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Backend

```bash
python app/api/app.py
```

---

## Run Streamlit Dashboard

```bash
streamlit run app/frontend/dashboard.py
```

---

## Start Ollama

```bash
ollama serve
```

Pull required models

```bash
ollama pull qwen2.5
ollama pull phi3
```

---

## Database

Create PostgreSQL (or SQLite) database and update configuration in `config.py`.

---

## Project Structure

```
SurgiMind/

README.md

requirements.txt

main.py

app/
├── api/
├── frontend/
├── ml/
├── rag/
├── llm/
├── utils/
└── config/

data/

models/

vectorstore/

tests/

docs/
```

---

# Future Improvements

- Multi-Hospital Deployment
- Federated Learning
- FHIR Integration
- Real-Time ICU Monitoring
- Explainable Deep Learning
- Multi-Language Clinical Support

---

# Tech Stack

- Python
- Scikit-learn
- Streamlit
- Flask
- Ollama
- Groq
- FAISS
- PostgreSQL
- SQLite
- Pandas
- NumPy
- Joblib

---

# License

This project is intended for research and educational purposes.

Clinical decisions should always be reviewed by qualified healthcare professionals.
