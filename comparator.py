from llm_interface import ask_llm

def compare_summaries(summary1, summary2):

    prompt = f"""
Two AI models analyzed the same dataset.

Summary from Model A:
{summary1}

Summary from Model B:
{summary2}

If both summaries agree, return a unified summary.
If they disagree, explain the discrepancy and produce a corrected final summary.
"""

    final = ask_llm("llama3.2", prompt)

    return final