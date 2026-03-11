from llm_interface import ask_llm

def summarize_results(data, model):

    prompt = f"""
You are analyzing Twitch streamer statistics.

Dataset results:
{data}

Explain the key insights in 2–3 sentences.
"""

    return ask_llm(model, prompt)