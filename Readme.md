
# 🧠 Python Quiz & Learning Platform

A beginner-friendly, interactive quiz application built with Python to make learning Python more engaging through questions, explanations, time limits, streaks, and achievements.

## ✨ Features

- 📝 **Interactive Quiz:** Answer Python-related multiple-choice questions.
- 🔀 **Randomized Questions:** Questions appear in a shuffled order for each game.
- ✅ **Input Validation:** Handles invalid answer choices.
- ⏱️ **Timed Questions:** Answer within a 10-second time limit.
- 📊 **Score Tracking:** Calculates the final score and percentage.
- 🔁 **Replay Option:** Play another round after finishing a quiz.
- 🔥 **Streak Tracking:** Track consecutive correct answers.
- 🏆 **Achievements:** Unlock rewards such as *3 in a Row* and *Quiz Master*.
- 💡 **Explanations:** Learn why an answer is correct.

## 🛠️ Technologies Used

- Python
- `random` — to shuffle questions
- `inputimeout` — to implement timed input

## 📂 Project Structure

```text
quiz-learning-platform/
├── main.py
├── timer_test.py
└── README.md
```

- `main.py` — Main quiz application.
- `timer_test.py` — A separate script used to test the timer functionality.
- `README.md` — Project documentation.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kinjal-09/quiz-learning-platform.git
```

### 2. Navigate to the project folder

```bash
cd quiz-learning-platform
```

### 3. Install the required package

```bash
python -m pip install inputimeout
```

### 4. Run the quiz

```bash
python main.py
```

To run the timer test separately:

```bash
python timer_test.py
```

## 🎮 How It Works

1. Start the quiz.
2. Answer each multiple-choice question within the time limit.
3. Receive feedback and explanations.
4. Build your streak by answering consecutive questions correctly.
5. Unlock achievements as you progress.
6. View your final score, percentage, and achievements.
7. Play again if you want another round.

## 📚 What I Learned

Building this project helped me practise:

- Python functions, loops, and conditional statements
- Lists and dictionaries
- User input and input validation
- Randomization
- Exception handling
- Working with external Python packages
- Tracking scores and consecutive answers
- Implementing a timer
- Debugging and improving an existing project

## 🚀 Future Improvements

- Add difficulty levels.
- Expand the question bank.
- Add more achievements and rewards.
- Save high scores between sessions.
- Improve the user interface.
- Organize questions into different topics.

## 👩‍💻 About

This project is part of my journey of learning Python and building practical projects as I work toward a career in Data Science and AI/ML.

I'm continuously improving it by adding new features and applying what I learn.

**More features coming soon!** 🚀
