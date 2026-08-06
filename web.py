from flask import Flask, request
from agent.brain import process_request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":
        user = request.form["message"]
        answer = process_request(user)

    return f"""
    <h1>🛡️ Secure Math Agent</h1>
    <p>Ask a mathematical question below.</p>

    <form method="POST">
        <input
            type="text"
            name="message"
            placeholder="Ask something..."
            style="width:300px;"
        >

        <button type="submit">
            Send
        </button>
    </form>

    <br>

    <b>Agent:</b> {answer}
    """

if __name__ == "__main__":
    app.run(debug=True)