from dataset_loader import load_dataset
from query_generator import generate_query
from result_summarizer import summarize_results
from comparator import compare_summaries

df = load_dataset()

print("\nThis dataset contains statistics about top Twitch streamers.")
print("Ask questions about followers, viewers, language, etc.\n")

question = input("User: ")

query = generate_query(question)

print("\nGenerated Query:")
print(query)

try:

    query = query.split("\n")[-1].strip()

    print("\nExecuting Query:", query)

    result = eval(query, {"df": df})

    if len(result) > 10:

        print("\nToo many results:", len(result))
        print("Please refine your query.")

    else:

        print("\nQuery Result:")
        print(result)

        summary_llama = summarize_results(result, "llama3.2")
        summary_deepseek = summarize_results(result, "deepseek-r1")

        print("\nSummary from Llama:")
        print(summary_llama)

        print("\nSummary from DeepSeek:")
        print(summary_deepseek)

        final = compare_summaries(summary_llama, summary_deepseek)

        print("\nFinal Unified Answer:")
        print(final)

except Exception as e:

    print("\nError executing query:", e)
    print("Please try another question.")