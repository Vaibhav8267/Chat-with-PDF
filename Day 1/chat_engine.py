import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""Answer the question using the context below.

Context:
{context}

Question: {query}
Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']
