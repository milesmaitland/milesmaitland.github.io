import random

def magic_8_ball():
    responses = [
        "Yes",
        "No",
        "Ask again later",
        "Cannot predict now",
        "Don't count on it",
        "Maybe",
        "Outlook not so good",
        "Most likely",
        "Reply hazy, try again",
        "It is certain"
    ]

    print("Welcome to the Magic 8-Ball!")
    input("Ask a yes or no question: ")

    # Generating a random response from the list
    response = random.choice(responses)
    print(f"The Magic 8-Ball says: {response}")

if __name__ == "__main__":
    magic_8_ball()