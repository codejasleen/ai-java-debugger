from services.llm_service import get_debug_response


def main():
    print("\n=== Java AI Debugger ===\n")

    java_error = input("Paste your Java error:\n")

    print("\nAnalyzing error...\n")

    response = get_debug_response(java_error)

    print("\n===== AI DEBUG RESULT =====\n")

    solution = response["solution"]
    validation = response["validation"]

    print("ROOT CAUSE:")
    print(solution["root_cause"])
    print()

    print("RECOMMENDED FIX:")
    print(solution["recommended_fix"])
    print()

    print("QUICK STEPS:")
    for step in solution["quick_steps"]:
        print("-", step)
    print()

    print("OTHER FIX OPTIONS:")
    for option in solution["fix_options"]:
        print(f"- {option['method']}: {option['when_to_use']}")
    print()

    print("VALIDATION:")
    print("Root cause valid:", validation["valid_root_cause"])
    print("Fix correct:", validation["fix_is_correct"])
    print("Reviewer note:", validation["notes"])
    print()


if __name__ == "__main__":
    main()
