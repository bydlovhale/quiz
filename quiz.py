
**Code (quiz.py)**  
```python
import json

with open("questions.json", "r") as f:
    questions = json.load(f)

score = 0
for q in questions:
    print("\n" + q["question"])
    for i, opt in enumerate(q["options"], 1):
        print(f"{i}. {opt}")
    ans = int(input("Your choice: "))
    if q["options"][ans-1] == q["answer"]:
        score += 1

print(f"\nYour score: {score}/{len(questions)}")
