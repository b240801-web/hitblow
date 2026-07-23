import random

def hint(secret, guess):
    result = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result.append(f"{i+1}桁目はHitです")
        elif guess[i] in secret:
            result.append(f"{i+1}桁目はBlowです")

    if len(result) == 0:
        return "HitやBlowしている数字はありません"

    return random.choice(result)