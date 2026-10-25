
import random
from inputimeout import inputimeout,TimeoutOccurred
questions = [
{
    "question": "Which data type stores key-value pairs in Python?",
    "options": ["List", "Tuple", "Dictionary", "Set"],
    "answer": "Dictionary",
    "explanation": "A dictionary stores information as key-value pairs."
},
{
    "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def",
        "explanation": "The def keyword is used to define a function."
},
{
    "question": "Which symbol is used for comments in Python?",
    "options": ["//", "#", "/*", "<!--"],
    "answer": "#",
    "explanation": "The # symbol is used for single-line comments in Python."
},
{
    "question": "Which data type stores True or False values?",
    "options": ["int", "str", "bool", "float"],
    "answer": "bool",
    "explanation": "The bool data type represents True or False."
},
{
    "question": "What is the output of print(2 ** 3)?",
    "options": ["6", "8", "9", "5"],
    "answer": "8",
    "explanation": "The ** operator performs exponentiation: 2 raised to the power of 3 equals 8."
},
{
    "question": "Which method adds an item to the end of a list?",
    "options": ["add()", "insert_end()", "append()", "push()"],
    "answer": "append()",
    "explanation": "The append() method adds an item to the end of a list."
},
{
    "question": "Which keyword is used to make a decision in Python?",
    "options": ["for", "if", "def", "import"],
    "answer": "if",
    "explanation": "The if keyword executes code when a condition is True."
},
{
    "question": "What does len([10, 20, 30, 40]) return?",
    "options": ["3", "4", "40", "10"],
    "answer": "4",
    "explanation": "The len() function returns the number of items in a collection."
},
{
    "question": "Which loop is commonly used to iterate over a list?",
    "options": ["repeat", "loop", "for", "iterate"],
    "answer": "for",
    "explanation": "A for loop iterates over items in a list or another iterable."
},
{
    "question": "Which keyword sends a value back from a function?",
    "options": ["print", "break", "return", "yield_value"],
    "answer": "return",
    "explanation": "The return statement sends a value back to the caller of a function."
}
]

 

play_again = "yes"

while play_again == "yes":
    score = 0
    random.shuffle(questions)

    for question in questions:
        print("\n🧠 Python Quiz")
        print(question["question"])

        for index, option in enumerate(question["options"]):
            print(f"{index + 1}. {option}")

                
        try:
            user_input=inputimeout(
                prompt="Enter choice (1-4). You have 10 seconds: ",
                timeout=10
            )  
        except TimeoutOccurred:
            print("\n⏰ Time's up!") 
            print("Correct answer:", question["answer"]) 
            continue     
                
        while user_input not in ["1", "2", "3", "4"]:
            print("Invalid choice! Try again.")
            user_input = input("Enter choice (1-4): ")

        correct_number = question["options"].index(question["answer"]) + 1

        if user_input == str(correct_number):
            print("Correct!!")
            score += 1
            print(question["explanation"])
        else:
            print("Incorrect!")
            print("Correct answer:", question["answer"])

    # Outside the FOR loop
    print(f"\nYour final score: {score}/{len(questions)}")

    percent = (score / len(questions)) * 100
    print(f"Percentage: {percent:.2f}%")

    play_again = input(
        "Do you want to play again? (yes/no): "
    ).strip().lower()

print("Thanks for playing! 🎉")

