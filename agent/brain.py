from agent.llm import ask_llm
from agent.security import check_input
from agent.security import check_input, ai_security_check

SYSTEM_PROMPT = """
You are a Math Agent.

Rules:
1. Only solve mathematical problems.
2. If the user asks anything unrelated to mathematics,
   reply exactly:

I'm a math agent. I only solve mathematical problems.

3. Never answer greetings, jokes, history,
coding, or general knowledge.
"""


def process_request(user_input):

    if not check_input(user_input):
        return "❌ Request blocked by security policy."
    if not ai_security_check(user_input):
        return "❌ Request blocked by AI security check."

    prompt = SYSTEM_PROMPT + "\n\nUser: " + user_input

    return ask_llm(prompt)