import random
from model_utils import generate_gpt2_captions

def generate_emojis(mood):
    emoji_dict = {
        "happy": ["😊", "✨", "🌞", "🥳", "😁"],
        "chill": ["😌", "🌊", "🧘‍♀️", "🍃", "🎧"],
        "energetic": ["⚡", "🔥", "💪", "🚀", "🏃‍♂️"],
        "romantic": ["❤️", "💫", "💖", "🌹", "😘"],
        "funny": ["😂", "🤣", "😜", "🤪", "🙃"]
    }
    return random.sample(emoji_dict.get(mood, ["✨", "💬"]), 2)

def generate_hashtags(theme, tone, custom_tags):
    base_tags = [f"#{word.strip()}" for word in theme.lower().split()]
    tone_tags = [f"#{tone.lower()}"]
    custom = [f"#{tag.strip()}" for tag in custom_tags.split(",") if tag.strip()] if custom_tags else []
    return random.sample(["#Vibes", "#Inspo", "#NowPlaying", "#Mood", "#ExploreMore"], 2) + base_tags + tone_tags + custom

def format_caption(platform, caption):
    if platform == "Twitter":
        return caption[:280]
    elif platform == "Instagram":
        return caption + "\n.\n.\n.\n#ExploreMore"
    return caption

def generate_template_caption(theme, tone, mood, platform, hashtags):
    templates = {
        "funny": [
            f"When life gives you {theme}, laugh it off",
            f"Still waiting for {theme} to make sense 😂",
            f"{theme}? I barely know her! 😜",
            f"I came, I saw, I {theme}ed 💁",
            f"{theme} level: expert 🙃"
        ],
        "formal": [
            f"Embracing the journey of {theme} with grace.",
            f"{theme} drives innovation and excellence.",
            f"Rethinking the way we approach {theme}.",
            f"{theme}: Where professionalism meets purpose.",
            f"Redefining {theme}, one step at a time."
        ],
        "sarcastic": [
            f"Oh wow, {theme} again. How original 🙄",
            f"{theme}? Groundbreaking. Truly. 🤔",
            f"Because we totally needed more {theme}... sure.",
            f"Living the {theme} dream, one eye-roll at a time 😏",
            f"{theme} is the gift that keeps on giving—like taxes."
        ]
    }

    selected = random.sample(templates.get(tone.lower(), templates["funny"]), 5)
    captions = []
    for line in selected:
        emojis = " ".join(generate_emojis(mood))
        tags = " ".join(hashtags)
        captions.append(format_caption(platform, f"{line} {emojis}\n{tags}"))
    return captions

def generate_captions(theme, tone, mood, platform, custom_tags, use_gpt2):
    hashtags = generate_hashtags(theme, tone, custom_tags)

    if use_gpt2:
        return generate_gpt2_captions(theme, tone, mood, platform, hashtags)
    else:
        return generate_template_caption(theme, tone, mood, platform, hashtags)
