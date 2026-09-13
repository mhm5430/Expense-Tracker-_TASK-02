# Expense-Tracker-_TASK-02
DecodeLabs-Expense-Tracker TASK 02


A state-preserving CLI Expense Tracker in Python with input validation and real-time data accumulation.



# 💰 Expense Tracker - State-Preserving Backend Engine

An architecture-focused Python CLI application built to demonstrate continuous data processing, state preservation, type safety, and defensive coding.

Developed as part of **Project 2** for the **DecodeLabs Python Development Internship Program**.

---

## 🌟 Key Technical Features

- **State Preservation:** Keeps active state outside iteration loops to retain continuous numerical data.
- **Defensive Coding (Digital Poka-Yoke):** Implements robust `try-except` blocks handling `ValueError` to prevent runtime crashes on bad inputs.
- **Accumulator Pattern:** Implements real-time ledger logic via $State(new) = State(old) + Input$.
- **Graceful Shutdown (Sentinel Value):** Halted safely using dedicated kill-switch triggers.

---

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.x
- **Architecture:** IPO Model (Input -> Process -> Output)
- **Error Handling:** `try-except` (Poka-Yoke)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/mhm5430/DecodeLabs-Expense-Tracker.git]
