from transformers import pipeline, set_seed
import random

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_gpt2_captions(theme, tone, mood, platform, hashtags):
    prompt = f"Write a short, {tone}, {mood} social media caption about {theme}. Include emojis and keep it under 280 characters."

    results = generator(prompt, max_length=60, num_return_sequences=5, do_sample=True, temperature=0.9)
    captions = []
    for res in results:
        text = res['generated_text'].strip().split('\n')[0]
        tag_line = " ".join(random.sample(hashtags, min(5, len(hashtags))))
        captions.append(text + "\n" + tag_line)
    return captions
