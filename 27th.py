# Kotyadipathi problem
# List of questions, each question is a dictionary containing the question, options, and the correct answer.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Madrid", "Paris", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon Dioxide"
    }
]

def ask_question(question_dict):
    print(question_dict["question"])
    for i, option in enumerate(question_dict["options"], start=1):
        print(f"{i}. {option}")
    
    user_answer = input("Enter the number of your answer (1-4): ")
    user_answer = int(user_answer) - 1  # Convert the user's answer to an index (0-3)

    if question_dict["options"][user_answer] == question_dict["correct_answer"]:
        return True
    else:
        return False

score = 0

for question in questions:
    if ask_question(question):
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['correct_answer']}\n")

print(f"You got {score} out of {len(questions)} questions correct.")
