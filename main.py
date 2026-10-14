
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
}
]


score=0 
for question in questions:
    print("\n🧠 Python Quiz")
    print(question["question"])


    for index,option in enumerate (question["options"]):
        print(f"{index + 1}. {option}")
    
#user's input      
    user_input=input("enter choice(1-4):")
    while user_input not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        user_input = input("Enter choice (1-4): ")

    
     
#checking of the answer's  and score calculation      
    if user_input==str(question["options"].index(question["answer"]) + 1):
       print("Your input:", user_input)
       print("Correct answer number:", question["options"].index(question["answer"]) + 1)
       print("correct!!")
       score+=1
       print(question["explanation"])  
    else:
        print("Try again! next time")
print(f"\nYour final score: {score}/{len(questions)}")
              
              





