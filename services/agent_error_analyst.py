import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def analyze_error(java_error: str):
    system_prompt = """
You are an expert Java debugging analyst.

Analyze the given error and return ONLY a JSON object.

Fields required:
- exception_type
- error_category (runtime / compile / logical)
- domain (collections / threading / database / IO / spring / general)
- severity (low / medium / high)
- likely_cause
- search_hints (array of keywords useful for retrieving debugging knowledge)

Do not explain.
Do not add text.
Return JSON only.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": java_error}
        ]
    )

    content = response.choices[0].message.content

    # Remove markdown formatting if model adds ```json ```
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        parsed = json.loads(content)
        return parsed
    except:
        print("Agent output not valid JSON:")
        print(content)
        return None
