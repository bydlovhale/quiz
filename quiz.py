import json

def load_questions(filename="questions.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON.")
        return []

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")

        while True:  # input validation loop
            try:
                ans = int(input("Your choice: "))
                if 1 <= ans <= len(q["options"]):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(q['options'])}.")
            except ValueError:
                print("Please enter a valid integer.")

        if q["options"][ans - 1] == q["answer"]:
            score += 1

    print(f"\nYour scor: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions()
    if questions:
        run_quiz(questions)
