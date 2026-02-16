from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from services.retrieval_service import retrieve_relevant_context
from services.agent_error_analyst import analyze_error
from services.agent_retrieval_strategist import plan_retrieval
from services.agent_fix_generator import generate_fix
from services.agent_solution_validator import validate_solution

client = Groq(api_key=GROQ_API_KEY)


def load_prompt():
    with open("prompts/debug_prompt.txt", "r") as file:
        return file.read()


def get_debug_response(java_error: str):
    system_prompt = load_prompt()

    # STEP 1 — Error Analyst Agent
    analysis = analyze_error(java_error)
    print("\nAGENT ANALYSIS:\n", analysis)

    # STEP 2 — Retrieval Strategist Agent
    strategy = plan_retrieval(analysis) if analysis else None
    print("\nRETRIEVAL STRATEGY:\n", strategy)

    # STEP 3 — Build strategist-guided search query
    if analysis and strategy:
        expanded_keywords = " ".join(strategy.get("query_expansion", []))

        search_query = f"""
Exception: {analysis.get('exception_type')}
Domain: {analysis.get('domain')}
Cause: {analysis.get('likely_cause')}
Keywords: {expanded_keywords}
"""
    else:
        # fallback if agents fail
        search_query = java_error

    # STEP 4 — Adaptive retrieval with dynamic top_k
    top_k = strategy.get("top_k", 5) if strategy else 5
    context = retrieve_relevant_context(search_query, top_k=top_k)

    print("\nCONTEXT SENT TO LLM:\n", context)

    # STEP 5 — Final reasoning by LLM
    # STEP 5 — Fix Generator Agent
    fix_output = generate_fix(java_error, context, analysis)

    # STEP 6 — Solution Validator
    validation = validate_solution(fix_output)

    print("\nVALIDATION RESULT:\n", validation)

    return {
        "solution": fix_output,
        "validation": validation
    }
