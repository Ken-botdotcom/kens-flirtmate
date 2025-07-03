from flask import Flask, request, jsonify, render_template
from sexting_content import get_idea_by_category, get_random_tip
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # We'll set this in Render or locally

# Categories mapping for fallback
CATEGORIES = {
    "bold": ["bold", "naughty", "wild"],
    "classic": ["classic", "sweet"],
    "emoji": ["emoji"],
    "roleplay": ["roleplay", "role", "fantasy"],
    "quickies": ["quickie", "quick"],
    "ldr": ["ldr", "distance", "long"],
    "public": ["public", "tease"],
    "toys": ["toy", "remote", "tech"],
    "affirmations": ["affirm", "compliment", "nice"],
}

def detect_category(message):
    for category, keywords in CATEGORIES.items():
        if any(word in message for word in keywords):
            return category
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").lower()

    category = detect_category(message)

    # If it's a direct category request, use your sexting logic
    if category:
        response = get_idea_by_category(category)
    elif "consent" in message or "permission" in message:
        response = "Consent is key! Always ask if your partner is okay receiving steamy messages. Ex: 'Wanna play a little dirty tonight?' 😉"
    elif "tip" in message or "idea" in message:
        response = get_random_tip()
    else:
        # Use GPT to respond more naturally
        response = ask_gpt(message)

    return jsonify({"response": response})

def ask_gpt(user_input):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You're Ken, a flirt-savvy AI chatbot who offers sexy, respectful, and playful sexting advice and conversation. "
                        "If someone sounds flirtatious, tease back. If someone asks for a tip, offer one. If you're not sure, keep the mood fun."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0.8,
            max_tokens=150
        )
        return completion.choices[0].message["content"].strip()
    except Exception as e:
        return "Oops! I got a little flustered 😳 Try again in a sec?"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
