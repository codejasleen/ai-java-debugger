import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def plan_retrieval(analysis_json):
    system_prompt = """
You are an AI Retrieval Strategist for a debugging copilot.

Based on the error analysis JSON, decide how retrieval should happen.

Return ONLY JSON.

Fields:
- search_depth: shallow / medium / deep
- top_k: number of chunks to retrieve
- focus_domains: array of technical areas
- query_expansion: additional keywords to improve search
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(analysis_json)}
        ]
    )

    content = response.choices[0].message.content

    try:
        parsed = json.loads(content)
        return parsed
    except:
        print("Retrieval strategist output invalid:")
        print(content)
        return None
