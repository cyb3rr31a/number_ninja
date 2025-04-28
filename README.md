# ⚔️ Number Ninja

**Number Ninja** is a Python-based number guessing game where players must uncover a secret number within a calculated number of attempts. Think fast, guess smart — or be defeated!

---

## 🧠 How It Works

1. The user enters a **lower and upper bound**.
2. The computer randomly selects a **secret number** within that range.
3. You guess until you get it right or run out of chances.
4. Each guess gives feedback:
   - “Too high” 🔺
   - “Too low” 🔻
   - “Correct!” 🎯
5. Your total allowed guesses are determined using binary search logic: `ceil(log₂(upper - lower + 1))`

---

## 🕹️ How to Play

```bash
python number_ninja.py
```

You’ll be prompted to:
- Enter the lower and upper bounds
- Start guessing the secret number

Example:
```
Enter lower bound: 1
Enter upper bound: 100
You have 7 attempts to guess the number.
Guess a number: 50
Try again! You guessed too high.
...
```

---

## ✅ Features
- Custom number range input
- Smart attempt limit using binary search
- Friendly command-line interface
- Clean win/lose messaging
- Difficulty levels (Easy, Medium, Hard)
- Score tracking

---

## 🚀 Future Features (Coming Soon)
- High score persistence
- Hints system
- GUI version

---

## ⚙️ Tech Stack
- Python 3.x
- Standard libraries only (no external dependencies)

---

## 📊 Complexity

### Time Complexity
- **Best case**: `O(1)` (correct guess on first try)
- **Worst case**: `O(log n)` where `n = (upper - lower + 1)`

### Space Complexity
- **O(1)** — uses constant memory regardless of input size

---

## 📁 Project Structure
```
number_ninja/
├── number_ninja.py       # Main game script
├── README.md             # Game overview and instructions
```

---

## 🧙‍♂️ Inspiration
This game was built to practice control flow, loops, conditionals, and user input in Python — with a fun twist of logic-driven gameplay!

---

## 📜 License
MIT License

---

Good luck, Ninja. 🍀🥷

