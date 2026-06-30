# 🔵 Circular Pong

A unique twist on the classic Pong game — played on a **circular arena** with a rotating paddle.  
Built with **Pygame**.

---

## 🎮 Features

- **Circular arena** — the game is played inside a circle
- **Rotating paddle** — use left/right arrow keys to move the paddle around the circle
- **Dynamic ball physics** — ball speed increases slightly with each paddle hit
- **Randomized bounce** — each hit adds a small random variation to the ball's trajectory
- **Score tracking** — points increase with each successful paddle hit
- **Game over detection** — the game ends when the ball escapes the arena

---

## 🛠️ Technologies Used

- **Python 3** — core logic
- **Pygame** — 2D rendering and input handling

---

## 🚀 How to Run

### Requirements

Install Pygame:

```bash
pip install pygame

### Compile

python3 circular_pong.py

🎮 Controls
Key	Action
Left Arrow	Move paddle counter-clockwise
Right Arrow	Move paddle clockwise
Close Window	Exit the game
🧠 How It Works

    Arena — a circular boundary with a radius of 450 pixels

    Paddle — a red line that rotates around the circle's edge

    Ball — starts at the center and moves in a random direction

    Collision — when the ball hits the paddle, it bounces back with:

        A slight speed increase

        A small random trajectory variation

    Scoring — each successful paddle hit increases the score by 1

    Game Over — if the ball escapes the circle (exceeds epsilon), the game ends

🎯 Gameplay Tips

    Keep the paddle between the ball and the edge of the circle

    Anticipate the ball's trajectory — the paddle rotates, so timing is key

    The ball speeds up slightly with each hit, so react quickly!

