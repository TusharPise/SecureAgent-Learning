from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
import secrets
from google import genai
from agent.brain import process_request

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(32)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True

Session(app)

@app.route("/api/validate-key", methods=["POST"])
def validate_key():

    data = request.get_json()

    api_key = data.get("api_key", "").strip()

    if not api_key:
        return jsonify({"valid": False, "error": "API key is required."}), 400

    try:
        client = genai.Client(api_key=api_key)

        client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents="Reply with OK."
        )

        return jsonify({"valid": True})

    except Exception:
        return jsonify({
            "valid": False,
            "error": "Invalid or unusable API key."
        }), 401

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_input = data.get("message", "").strip()
    api_key = data.get("api_key", "").strip()

    if not user_input:
        return jsonify({"error": "Message is required."}), 400

    if not api_key:
        return jsonify({"error": "API key is required."}), 400

    last_result = session.get("last_result")

    answer = process_request(
        user_input,
        api_key,
        last_result
    )

    session["last_result"] = answer
    session.modified = True

    return jsonify({"answer": answer})


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)