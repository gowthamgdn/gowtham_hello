import random

def get_quote():
    quotes = [
        "Keep pushing forward! - Gowtham",
        "Success is the sum of small efforts, repeated daily.",
        "Code, Learn, Improve, Repeat!",
        "Your only limit is your mind.",
        "The best way to predict the future is to create it."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_quote())
