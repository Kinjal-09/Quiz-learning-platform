
question = {
    "question": "Which data type stores key-value pairs in Python?",
    "options": ["List", "Tuple", "Dictionary", "Set"],
    "answer": "Dictionary",
    "explanation": "A dictionary stores information as key-value pairs."
}

print(" \n PYTHON QUIZ")
print(question["question"])
for index,option in enumerate (question["options"]):
    print(f"{index + 1}. {option}")
    
score=0    
user_input=input("enter choice(1-4):")
if user_input==str(question["options"].index(question["answer"]) + 1):
    print("correct!!")
    score+=1
    print(question["explanation"])  
else:
    print("Try again! next time")
print(f"Your score: {score}")
