from collections import Counter


WORD_FILE = "words.txt"


def load_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = []

        for line in f:
            word = line.strip().lower()

            if len(word) == 5 and word.isalpha():
                words.append(word)

        return list(set(words))



def get_feedback(answer, guess):
    """
    Creates real Wordle feedback.

    G = Green
    Y = Yellow
    . = Gray

    Handles duplicate letters correctly.
    """

    feedback = ["."] * 5
    remaining = Counter(answer)



    for i in range(5):

        if guess[i] == answer[i]:
            feedback[i] = "G"
            remaining[guess[i]] -= 1


    for i in range(5):

        if feedback[i] == "G":
            continue

        letter = guess[i]

        if remaining[letter] > 0:
            feedback[i] = "Y"
            remaining[letter] -= 1

    return "".join(feedback)




def matches(word, guess, feedback):


    actual_feedback = get_feedback(word, guess)

    return actual_feedback == feedback




def filter_words(words, guess, feedback):

    return [
        word
        for word in words
        if matches(word, guess, feedback)
    ]




def explain_constraints(guess, feedback):

    green = {}
    yellow = set()
    gray = set()

    for i in range(5):

        letter = guess[i]
        result = feedback[i]

        if result == "G":
            green[i] = letter

        elif result == "Y":
            yellow.add(letter)

        elif result == ".":
            gray.add(letter)

    return green, yellow, gray




def score_word(word, possible_answers):

    if not possible_answers:
        return 0

    # Letter frequency
    frequency = Counter(
        "".join(possible_answers)
    )

    score = 0
    seen = set()

    # Prefer common UNIQUE letters
    for letter in word:

        if letter not in seen:
            score += frequency[letter]
            seen.add(letter)

    return score




def get_suggestions(possible_answers, all_words, number=10):

    scored = []

    for word in all_words:

        score = score_word(
            word,
            possible_answers
        )

        scored.append(
            (score, word)
        )

    scored.sort(
        reverse=True
    )

    return [
        word
        for score, word in scored[:number]
    ]

def show_constraints(guess, feedback):

    green, yellow, gray = explain_constraints(
        guess,
        feedback
    )

    print()
    print("KNOWN INFORMATION")
    print("-----------------")

    # Green letters
    for position, letter in green.items():

        print(
            f"GREEN: position {position + 1} = {letter.upper()}"
        )

    # Yellow letters
    for letter in sorted(yellow):

        print(
            f"YELLOW: {letter.upper()} is in the word"
        )

    # Gray letters
    for letter in sorted(gray):

        # Only show as completely gray if it wasn't
        # also confirmed elsewhere.
        if letter not in yellow and letter not in green.values():

            print(
                f"GRAY: {letter.upper()} is NOT in the word"
            )

    print()




def main():

    all_words = load_words(WORD_FILE)

    possible_answers = all_words.copy()

    print("=" * 50)
    print("              WORDLE GUESSER")
    print("=" * 50)

    print()
    print("G = Green")
    print("Y = Yellow")
    print(". = Gray")
    print()

    print("Example:")
    print("Guess:    SNIPE")
    print("Feedback: ....G")
    print()

    while True:


        print("-" * 50)

        print(
            f"Possible answers: {len(possible_answers)}"
        )

        if len(possible_answers) == 0:

            print()
            print("NO WORDS MATCH.")
            print()
            print(
                "Check that your previous feedback "
                "was entered correctly."
            )

            break



        if len(possible_answers) == 1:

            print()
            print(
                "ANSWER:",
                possible_answers[0].upper()
            )

            break


        suggestions = get_suggestions(
            possible_answers,
            all_words,
            number=10
        )

        print()
        print("BEST SUGGESTIONS:")

        for i, word in enumerate(
            suggestions,
            start=1
        ):

            print(
                f"{i:2}. {word.upper()}"
            )

        print()


        guess = input(
            "Enter your guess: "
        ).strip().lower()

        if len(guess) != 5 or not guess.isalpha():

            print(
                "ERROR: Enter exactly 5 letters."
            )

            continue


        feedback = input(
            "Enter feedback (G/Y/.): "
        ).strip().upper()

        if len(feedback) != 5:

            print(
                "ERROR: Feedback must have 5 characters."
            )

            continue

        if any(
            character not in "GY."
            for character in feedback
        ):

            print(
                "ERROR: Use only G, Y, and ."
            )

            continue


        show_constraints(
            guess,
            feedback
        )



        possible_answers = filter_words(
            possible_answers,
            guess,
            feedback
        )


        if len(possible_answers) <= 20:

            print(
                "Remaining:",
                ", ".join(
                    word.upper()
                    for word in possible_answers
                )
            )


if __name__ == "__main__":
    main()
