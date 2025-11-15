from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS FIX
CORS(app, resources={r"/*": {"origins": "*"}})

def generate_reply(message):
    message = message.lower()

    # Greetings
    if "hello" in message or "hi" in message:
        return "Hello! where are doing  you sex today?"

    # How are you?
    if "how are you" in message:
        return "I'm dhasu! Thanks for asking 😊. How can I fuck you?"

    # Bot name
    if "your name" in message:
        return "I'm Gungun Gupta Assistant Bot 🤖! How can I help you?"

    # About Meerut Mart
    if "gungun gupta" in message:
        return "Gungun Gupta is your personal assistant who helps you with various tasks."

    # Price related
    if "song" in message:
        return " ummm AAH Bheetaar  bheetar Aag laage"

    # Default fallback
    return "Sorry, I don't understand because i am looking at you  😊."


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Chatbot is running"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message")
    reply = generate_reply(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
