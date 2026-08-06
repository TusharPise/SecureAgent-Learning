import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.1-flash-lite"

history = []


def ask_llm(user_input):
    history.append(user_input)

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents="\n".join(history)
        )

        answer = response.text

        history.append(answer)

        return answer

    except Exception as e:

        if "429" in str(e):
            return "⚠️ Gemini API rate limit reached. Please wait a while and try again."

        return "⚠️ Something went wrong."