import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def validate_solution(fix_output):
    system_prompt = """
You are a senior Java code reviewer.

Your job is to VALIDATE the debugging solution.

Check:
- Is the root cause logical?
- Is the recommended fix correct?
- Any obvious mistakes?

Return ONLY JSON.

Format:
{
  "valid_root_cause": true/false,
  "fix_is_correct": true/false,
  "notes": "...short simple feedback..."
}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(fix_output)}
        ]
    )

    content = response.choices[0].message.content
    content = content.replace("```json", "").replace("```", "").strip()

    try:
        parsed = json.loads(content)
        return parsed
    except:
        print("Validator JSON error:")
        print(content)
        return None
