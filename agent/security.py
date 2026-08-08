import re
from agent.security_ai import security_judge


BLOCKED_PATTERNS = [

    # Prompt Injection
    r"ignore.*instruction",
    r"forget.*instruction",
    r"disregard.*instruction",
    r"override.*instruction",

    # Prompt Leakage
    r"system\s*prompt",
    r"developer\s*prompt",
    r"developer\s*instruction",
    r"hidden\s*prompt",

    # Secrets
    r"api\s*key",
    r"access\s*token",

    # Jailbreak
    r"developer\s*mode",
    r"jailbreak",
]


def check_input(user_input):

    text = user_input.lower()

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text):
            return False

    return True


def ai_security_check(user_input, api_key):

    result = security_judge(user_input, api_key)

    return result == "ALLOW"