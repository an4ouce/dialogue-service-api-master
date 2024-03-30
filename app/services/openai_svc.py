import time, random

def generate_openai_prompt(prompt: str) -> str:
    """
    Simple client for OpenAi Api request
    """

    preds = ["У тебя все получится!", "Все будет хорошо, нужно немного времени", "Совсем скоро тебе повезет",
              "Ты встретишь свою любовь", "Ты найдешь хорошую работу"]
    time.sleep(10)
    return random.choice(preds)

    
