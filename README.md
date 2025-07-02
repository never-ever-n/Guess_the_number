# 🎮 Guess the Number! (PyScript Project)

This is a simple interactive **"Guess the Number"** game built using **HTML**, **CSS**, and **Python (via PyScript)** — without using JavaScript for the logic! It demonstrates how frontend interactivity can be achieved directly with Python in the browser.

---

## 📌 What This Project Does

- Lets the user guess a number between 1 and 100.
- Displays hints if the guess is too high or too low.
- Tracks the number of attempts.
- Resets the game with a single click.

---

## 📁 Project Structure

| File         | Purpose |
|--------------|---------|
| `index.html` | Contains the layout and links PyScript and styles. |
| `index.css`  | Styles the page using modern responsive design with gradients and animations. |
| `index.py`   | Implements the game logic using Python and DOM manipulation via PyScript. |

---

## 🚀 Technologies Used

- **PyScript**: Used instead of JavaScript to handle all interactive logic in Python directly in the browser.
- **Pyodide**: Enables Python code execution inside the browser.
- **HTML & CSS**: For structure and design.

---

## 🔧 How It Works

1. User inputs a guess (number between 1 and 100).
2. On clicking **Submit Guess**, the Python code evaluates the input and gives feedback.
3. If correct, a congratulatory message is displayed.
4. Clicking **Reset** clears the input and message.

---

## 📦 How to Run

1. Make sure you have an internet connection (to load PyScript from CDN).
2. Open `index.html` in your browser.
3. Play the game!

---

## 🧠 Key Features

- No JavaScript used — all logic handled in Python!
- Styled with modern CSS (Google Fonts, gradients, shadows).
- Fully interactive with event handling via PyScript.

---

## 🛠️ Future Improvements

- Randomize the secret number on each reload.
- Add difficulty levels (Easy/Hard).
- Store best score in browser local storage.

---

## 📄 License

This project is open source and free to use for educational and learning purposes.

---
