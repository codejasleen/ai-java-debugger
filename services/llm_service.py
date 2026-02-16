from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from services.retrieval_service import retrieve_relevant_context
from services.agent_error_analyst import analyze_error
from services.agent_retrieval_strategist import plan_retrieval
from services.agent_fix_generator import generate_fix
from services.agent_solution_validator import validate_solution
from services.memory_service import search_memory, add_to_memory

client = Groq(api_key=GROQ_API_KEY)


def load_prompt():
    with open("prompts/debug_prompt.txt", "r") as file:
        return file.read()


def get_debug_response(java_error: str):
    system_prompt = load_prompt()

    # STEP 0 — Check memory first
    memory_result = search_memory(java_error)

    if memory_result:
        print("\nMEMORY HIT FOUND:\n", memory_result)
        return {
            "solution": {
                "root_cause": memory_result["root_cause"],
                "recommended_fix": memory_result["fix"],
                "quick_steps": ["Previously solved similar error — apply stored fix"],
                "fix_options": []
            },
            "validation": {
                "valid_root_cause": True,
                "fix_is_correct": True,
                "notes": "Reused from memory"
            }
        }

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

    # STEP 7 — Save to memory
    add_to_memory(java_error, fix_output, validation)

    return {
        "solution": fix_output,
        "validation": validation
    }

