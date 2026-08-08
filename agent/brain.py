from agent.llm import ask_llm
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
4. Format mathematical equations using LaTeX.
5. Use $$ ... $$ for equations that should appear on their own line.
6. Use $ ... $ for short inline mathematical expressions.
7. Keep explanations concise and readable.
8. Do not use Markdown bold for mathematical calculations.
9. Give the shortest correct solution for simple calculations.
10. Only show detailed steps when the problem is complex or the user explicitly asks for steps.
11. Keep simple arithmetic answers to one or two lines.
12. Keep responses concise and focused on the mathematical problem.
13. End with a clearly labeled final answer when solving a problem.
"""


def process_request(user_input, api_key, last_result=None):

    if not check_input(user_input):
        return "❌ Request blocked by security policy."

    if not ai_security_check(user_input, api_key):
        return "❌ Request blocked by AI security check."

    memory = ""

    if last_result:
        memory = f"""
Previous calculation result:
{last_result}

Use this previous result only when the user's new message refers to it.
"""

    prompt = (
        SYSTEM_PROMPT
        + "\n"
        + memory
        + "\nUser: "
        + user_input
    )

    return ask_llm(prompt, api_key)