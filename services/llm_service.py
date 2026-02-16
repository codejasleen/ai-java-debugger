from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from services.retrieval_service import retrieve_relevant_context

client = Groq(api_key=GROQ_API_KEY)


def load_prompt():
    with open("prompts/debug_prompt.txt", "r") as file:
        return file.read()


def get_debug_response(java_error: str):
    system_prompt = load_prompt()

    # CALL RETRIEVAL (this line was missing or not executed)
    context = retrieve_relevant_context(java_error)

    print("\nCONTEXT SENT TO LLM:\n", context)

    enhanced_prompt = f"""
Relevant debugging knowledge:
{context}

User error:
{java_error}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": enhanced_prompt}
        ]
    )

    return response.choices[0].message.content
