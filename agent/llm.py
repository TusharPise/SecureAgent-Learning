from google import genai

MODEL_NAME = "gemini-3.1-flash-lite"

def ask_llm(user_input, api_key):
    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_input
        )

        return response.text

    except Exception as e:
        if "429" in str(e):
            return "⚠️ Gemini API rate limit reached. Please wait a while and try again."

        return "⚠️ Something went wrong."