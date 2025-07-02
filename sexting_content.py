import random

TIPS = [
    "Ask for consent before you sext. Always.",
    "Use sensory language—describe how things feel, smell, sound.",
    "Build anticipation with teasing messages.",
    "Ask playful questions like: 'What would you do to me right now if we were alone?'",
    "Tease, pause, and build suspense — don’t rush the heat.",
    "Talk about boundaries before getting spicy. It builds trust.",
    "Always double-check who you’re sending it to. No accidental boss texts!"
]

IDEAS = {
    "classic": [
        "I wish you were here right now...",
        "I've been thinking about that night in the car after dinner...",
        "I can't stop replaying that last kiss in my head."
    ],
    "bold": [
        "Imagine me on my knees, looking up at you with a grin.",
        "I want to feel your breath on my neck while your hands explore me.",
        "You're in charge tonight. Tell me what to do..."
    ],
    "emoji": [
        "🍑💦👅",
        "😈😏🔥💋",
        "You + me + 🛏️ = 🔥🔥🔥"
    ],
    "roleplay": [
        "You’re the professor, I’m the student who needs a little extra credit...",
        "Let’s pretend we’re strangers who meet in an elevator. What happens next?",
        "You’re the cop, and I’ve been very, very bad..."
    ],
    "ldr": [
        "Put your phone on speaker... I want to talk you through this.",
        "I just want to feel your voice in my ear tonight.",
        "Let’s sync up our toys and make it count 🔥"
    ],
    "quickies": [
        "Bathroom. 5 minutes. No talking. 😈",
        "I’m not wearing anything under this hoodie.",
        "Just thinking about your hands on me. That’s it. That’s the sext."
    ],
    "toys": [
        "Should I bring the toy we talked about? Or surprise you with a new one? 😏",
        "Imagine me teasing you with my vibe while on FaceTime.",
        "Let’s have a remote-controlled night... your turn to buzz me. 😉"
    ],
    "public": [
        "If you keep texting me like that, I might lose it in this Uber.",
        "I’m not wearing panties. And I’m sitting across from you.",
        "Text me one thing you’d do to me right now… in this café."
    ],
    "affirmations": [
        "You turn me on just by existing. And that’s not even the hottest part about you.",
        "You’re sexy as hell. And I love how you always make me laugh.",
        "You make me feel wanted. And right now, I want *you*."
    ]
}

def get_random_tip():
    return random.choice(TIPS)

def get_idea_by_category(cat):
    return random.choice(IDEAS.get(cat, IDEAS["classic"]))
