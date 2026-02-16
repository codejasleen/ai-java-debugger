from services.llm_service import get_debug_response


def main():
    print("\n=== Java AI Debugger ===\n")

    java_error = input("Paste your Java error:\n")

    print("\nAnalyzing error...\n")

    response = get_debug_response(java_error)

    print("----- AI Debug Result -----\n")
    print(response)


if __name__ == "__main__":
    main()
