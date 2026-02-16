import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_fix(java_error, context, analysis):
    system_prompt = """
You are a senior Java debugging assistant.

Your job is to suggest FIXES in a SIMPLE and PRACTICAL way.

Return ONLY JSON.

Rules:
- Use simple language
- No jargon
- Explain fixes clearly
- Give multiple options
- Recommend one best fix
- Provide quick step-by-step actions

JSON format:

{
  "root_cause": "...",
  "fix_options": [
    {
      "method": "...",
      "when_to_use": "...",
      "why_it_works": "..."
    }
  ],
  "recommended_fix": "...",
  "quick_steps": ["...", "...", "..."]
}
"""

    user_prompt = f"""
Error:
{java_error}

Analysis:
{analysis}

Retrieved context:
{context}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    content = response.choices[0].message.content

    # Clean markdown
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        parsed = json.loads(content)
        return parsed
    except:
        print("Fix agent JSON error:")
        print(content)
        return None
