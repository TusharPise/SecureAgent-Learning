from agent.brain import process_request

print("Secure AI Agent")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    answer = process_request(user)

    print("\nAgent:", answer)
    print()