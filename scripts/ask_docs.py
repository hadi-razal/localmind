from rag.queryengine import RagQuery


def main():
    rag = RagQuery()

    print("🔥 LocalMind RAG v1")
    print("Ask about your PDFs (type 'exit' to quit)\n")

    while True:
        question = input("You > ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        try:
            response = rag.ask(question, top_k=5)
            
            print("\nLocalMind >")
            # Access the response text properly
            # llama_index Response objects can be accessed via str() or .response attribute
            if response is None:
                response_text = "Empty Response (None)"
            elif hasattr(response, 'response') and response.response:
                response_text = str(response.response)
            elif hasattr(response, '__str__'):
                response_text = str(response)
            else:
                response_text = "Empty Response (Unknown format)"
            
            # Check if response is actually empty
            if not response_text or (isinstance(response_text, str) and response_text.strip() == ""):
                response_text = "Empty Response"
            
            print(response_text)
            print()

            # Show sources
            if hasattr(response, "source_nodes") and response.source_nodes:
                # print("Sources:")
                # for i, node in enumerate(response.source_nodes, start=1):
                #     metadata = node.node.metadata or {}
                #     source = metadata.get("file_name") or metadata.get("source") or "Unknown"
                #     print(f"{i}. {source}")
                print()
        except ValueError as e:
            print(f"\nError: {e}\n")
            continue
        except Exception as e:
            print(f"\nError: {e}\n")
            import traceback
            traceback.print_exc()
            continue


if __name__ == "__main__":
    main()
