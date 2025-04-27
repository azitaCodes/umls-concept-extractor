# 🧠 UMLS Clinical Concept Extractor using UMLS REST API

This project extracts medical concepts (CUIs) from clinical text using the official [UMLS REST API](https://documentation.uts.nlm.nih.gov/rest/home.html).

It’s great for healthcare NLP projects, research, or learning about biomedical ontologies like UMLS.

---

## 🔍 What It Does

- Authenticates with the UMLS API using your API key
- Splits a clinical sentence into key medical phrases
- Searches UMLS and extracts the top CUI for each phrase
- Saves results to a file (`results.txt`)

---

## 🧪 Example Input

```text
The patient was admitted to the ICU with sepsis secondary to a urinary tract infection and showed signs of hypotension, elevated lactate, and decreased urine output.
```

---

## ✅ Example Output

See full output in 👉 [results.txt](results.txt)

```text

---

### ✅ With this updated section:

```markdown
## ✅ Example Output

See full output in 👉 [results.txt](results.txt)

```text
🔍 UMLS concepts found in sentence:
📝 "The patient was admitted to the ICU with sepsis secondary to a urinary tract infection and showed signs of hypotension, elevated lactate, and decreased urine output."

📘 Term: ICU
🧠 UMLS Match: Bedside ICU Monitoring
🆔 CUI: C1547986
------------------------------------------------------------
📘 Term: sepsis
🧠 UMLS Match: Sepsis
🆔 CUI: C0243026
------------------------------------------------------------
📘 Term: urinary tract infection
🧠 UMLS Match: Urinary tract infection
🆔 CUI: C0042029
------------------------------------------------------------
📘 Term: hypotension
🧠 UMLS Match: Hypotension
🆔 CUI: C0020649
------------------------------------------------------------
📘 Term: elevated lactate
🧠 UMLS Match: Elevated lactate level
🆔 CUI: C4054756
------------------------------------------------------------
📘 Term: decreased urine output
🧠 UMLS Match: Decreased urine output
🆔 CUI: C3887784
------------------------------------------------------------
```

---

## 🛠 How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/umls-concept-extractor.git
cd umls-concept-extractor
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Get Your UMLS API Key

📘 Follow this guide 👉 [UMLS_Access_Guide.txt](UMLS_Access_Guide.txt)

### 4. Run the Script

Edit `umls_extractor.py` and replace the placeholder with your real UMLS API key:

```python
API_KEY = "your_real_umls_api_key_here"
```

Then run the script:

```bash
python umls_extractor.py
```

This will:
- Print UMLS matches to the terminal
- Save them to `results.txt`

---

## 📦 Files Included

| File | Description |
|------|-------------|
| `umls_extractor.py` | Main Python script |
| `requirements.txt` | Python dependencies (`requests`) |
| `UMLS_Access_Guide.txt` | Step-by-step guide to create UMLS account + get API key |
| `results.txt` | Example output from the tool |

---

## 💡 Future Ideas

- Auto keyword extraction using NLP
- Web UI with Streamlit
- JSON/CSV export

---

## 🙌 Author

Made by [Your Name] – Ph.D. student at Cleveland State University
