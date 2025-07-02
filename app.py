from flask import Flask, request, render_template, jsonify
from sexting_content import get_random_tip, get_idea_by_category

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").lower()

    if "tip" in message or "advice" in message:
        return jsonify({"response": get_random_tip()})
    elif "bold" in message or "naughty" in message or "wild" in message:
        return jsonify({"response": get_idea_by_category("bold")})
    elif "classic" in message or "sweet" in message:
        return jsonify({"response": get_idea_by_category("classic")})
    elif "emoji" in message:
        return jsonify({"response": get_idea_by_category("emoji")})
    elif "role" in message or "roleplay" in message or "fantasy" in message:
        return jsonify({"response": get_idea_by_category("roleplay")})
    elif "quickie" in message or "quick" in message:
        return jsonify({"response": get_idea_by_category("quickies")})
    elif "ldr" in message or "distance" in message or "long" in message:
        return jsonify({"response": get_idea_by_category("ldr")})
    elif "public" in message or "tease" in message:
        return jsonify({"response": get_idea_by_category("public")})
    elif "toy" in message or "remote" in message or "tech" in message:
        return jsonify({"response": get_idea_by_category("toys")})
    elif "affirm" in message or "compliment" in message or "nice" in message:
        return jsonify({"response": get_idea_by_category("affirmations")})
    elif "consent" in message or "permission" in message:
        return jsonify({"response": "Consent is key! Always ask if your partner is okay receiving steamy messages. Ex: 'Wanna play a little dirty tonight?' 😉"})
    else:
        return jsonify({"response": get_random_tip()})  # Fallback

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
