import ollama

def ask_llm(model, prompt):

    try:

        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"].strip()

    except Exception as e:

        return f"LLM Error: {str(e)}"