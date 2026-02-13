import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from localmind.core.chat_engine import ChatEngine

def main():
    print("LocalMind v0 — type 'exit' to quit\n")

    engine = ChatEngine()

    while True:
        user_input = input("You > ")

        if user_input.lower() in ["exit", "quit"]:
            break

        response = engine.ask(user_input)
        print("\nLocalMind >", response)
        print()


if __name__ == "__main__":
    main()