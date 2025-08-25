import pandas as pd
import google.generativeai as genai
from google.api_core import exceptions

def generate_csr_narrative(dataframe, api_key):
    genai.configure(api_key=api_key)
    summary_table = dataframe.groupby(['treatment_group', 'adverse_event']).size().unstack(fill_value=0)
    summary_table_str = summary_table.to_string()

    prompt_template = f'''
    You are an expert medical writer specializing in clinical study reports. Your task is to interpret a summary table of adverse events and write a concise, professional narrative.

    **Source Data:**
    ```{summary_table_str}```

    **Instruction:**
    Write a concise paragraph summarizing these findings. Mention the number of events for each treatment group and highlight any notable differences.
    '''

    model = genai.GenerativeModel('gemini-1.5-flash') 
    try:
        response = model.generate_content(prompt_template)
        return response.text
    except exceptions.ResourceExhausted:
        return "ERROR: The API is busy or you have exceeded your quota. Please try again in a minute."
    except Exception as e:
        return f"ERROR: An unexpected error occurred: {e}"