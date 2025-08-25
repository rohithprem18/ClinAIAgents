# ClinAIAgent Demo 💊

A simple Streamlit app for generating clinical study report (CSR) narratives from CSV data using AI.

## Features
- Upload your own CSV file or use sample data
- Preview uploaded data
- Generate a narrative using the `generate_csr_narrative` agent
- Easy-to-use sidebar controls

## Requirements
- Python 3.8+
- Streamlit
- pandas
- python-dotenv

Install dependencies:
```powershell
pip install -r requirements.txt
```

## Usage
1. Create a `.env` file in the project root with your Google API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```
2. Run the app:
   ```powershell
   python -m streamlit run app.py
   ```
3. Open the provided local URL in your browser.
4. Upload a CSV or use sample data, then click "✨ Generate Narrative".

## File Structure
- `app.py` — Main Streamlit app
- `agent_logic.py` — Contains the narrative generation logic
- `requirements.txt` — Python dependencies
- `.env` — Your API key (not included)

## Example CSV Format
```
patient_id,treatment_group,age,adverse_event
P001,DrugA,45,Headache
P002,DrugA,52,Nausea
P003,Placebo,48,Headache
P004,DrugA,60,Headache
P005,Placebo,55,None
P006,Placebo,62,Nausea
```

## Notes
- The narrative generation logic in `agent_logic.py` is a placeholder. Replace it with your own implementation as needed.
- Make sure your API key is valid and has access to the required AI service.

---
