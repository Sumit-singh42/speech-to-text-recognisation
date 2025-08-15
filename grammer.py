from llm import llm_request

def correct_grammar(text, use_gemini=False):
    prompt = f"Correct the grammar of the following sentence without changing meaning:\n\n{text}"
    return llm_request(prompt, use_gemini)