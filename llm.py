import requests
import json
from apikey import LOCAL_API_URL, GEMINI_API_KEY, GEMINI_MODEL

def llm_request(prompt, use_gemini=False):
    if use_gemini:        
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)
        return response.text.strip() if response else None
    else:        
        payload = {
            "model": "local-model",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        try:
            r = requests.post(LOCAL_API_URL, json=payload)
            r.raise_for_status()
            data = r.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        except Exception as e:
            print(f"❌ Local model request failed: {e}")
            return None