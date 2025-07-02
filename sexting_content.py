import random

TIPS = [
    "Ask for consent before you sext. Always.",
    "Use sensory language—describe how things feel, smell, sound.",
    "Build anticipation with teasing messages.",
    "Ask questions like: 'What would you do to me if we were together right now?'",
]

IDEAS = {
    "classic": ["I wish you were here right now...", "I've been thinking about that night in the car after dinner..."],
    "bold": ["I want to feel your hands all over me.", "Imagine me on top, whispering what I want to do..."],
    "ldr": ["Let’s sync up our toys tonight 😈", "Put your phone on speaker... I want to guide you through this."],
    "emoji": ["🍑💦👅", "😈😏🔥"],
    "roleplay": ["What if I were your boss and you were late for our 'meeting'?", "You’re the patient, I’m the doctor..."],
}

def get_random_tip():
    return random.choice(TIPS)

def get_idea_by_category(cat):
    return random.choice(IDEAS.get(cat, IDEAS["classic"]))
