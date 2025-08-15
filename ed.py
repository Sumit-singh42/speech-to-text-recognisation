from llm import llm_request
from memory import get_recent_context

def detect_emotion_with_context(current_text, use_gemini=False):
    past_entries = get_recent_context()
    
    past_texts = "\n".join(
        [f"[{e['timestamp']}] {e['transcript']} (Emotion: {e['emotion']})"
         for e in past_entries]
    )

    prompt = f"""
You are an emotion analysis AI. Consider the current text and also the previous conversation context.

Previous context:
{past_texts}

Current text:
{current_text}

Respond with the most likely emotion for the current text, considering the context.
Only return the emotion word.
    """
    return llm_request(prompt, use_gemini)
