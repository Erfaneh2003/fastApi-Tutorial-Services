import requests
import sys

API_URL = "http://127.0.0.1:8000/chat"


def start_chat():
    print(" AI Agent Terminal Chat")
    print("---------------------------------")
    print("Type 'exit' or 'quit' to end the session.")
    print("---------------------------------")

    thread_id = "terminal_user_1"

    while True:
        try:
            # 1. Get user input
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            # 2. Prepare data payload
            payload = {
                "text": user_input,
                "thread_id": thread_id
            }


            response = requests.post(API_URL, json=payload)

            # 4. Check for errors
            if response.status_code == 200:
                data = response.json()
                ai_response = data.get("response", "No response field found.")
                print(f"AI: {ai_response}")
            else:
                print(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.ConnectionError:
            print("\n Error: Could not connect to the server.")
            print("Make sure 'aiagent.py' is running in another terminal!")
            break
        except Exception as e:
            print(f"\n An error occurred: {e}")
            break


if __name__ == "__main__":
    start_chat()