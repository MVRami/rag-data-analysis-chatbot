from llm_interface import ask_llm

def generate_query(question):

    prompt = f"""
You are a Python data assistant.

Convert the user question into a VALID pandas dataframe query.

Rules:
- Return ONLY the pandas query
- No explanation
- DataFrame name is df
- Use exact column names
- If using multiple conditions use parentheses

Columns available:
Channel
Watch time(Minutes)
Stream time(minutes)
Peak viewers
Average viewers
Followers
Followers gained
Views gained
Partnered
Mature
Language

Example:
df[df['Language']=="English"]

User question:
{question}
"""

    query = ask_llm("llama3.2", prompt)

    return query