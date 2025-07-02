from flask import Flask, request, render_template, jsonify
from sexting_content import get_random_tip, get_idea_by_category

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").lower()

    if "tip" in message:
        return jsonify({"response": get_random_tip()})

    elif "idea" in message:
        if "role" in message:
            category = "roleplay"
        elif "emoji" in message:
            category = "emoji"
        elif "ldr" in message:
            category = "ldr"
        elif "bold" in message:
            category = "bold"
        else:
            category = "classic"
        return jsonify({"response": get_idea_by_category(category)})

    elif "consent" in message:
        return jsonify({"response": "Consent is key! Ask if they’re okay with receiving steamy messages. You can say: 'Hey, are you cool if I send something flirty?'"})

    return jsonify({"response": "Want a sexting tip, a category idea (classic, bold, emoji, roleplay), or advice on consent?"})

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

