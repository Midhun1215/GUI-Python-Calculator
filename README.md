# GUI-Python-Calculator
This is a game made using Python Which Helps in Basics
🖩 Tkinter Simple Calculator
📖 Overview
This project is a Graphical User Interface (GUI) Calculator built using Python’s tkinter library. It provides an interactive way to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The calculator is designed with a clean layout, styled buttons, and an entry box that displays both input and results.

✨ Features
Basic Arithmetic: Addition, subtraction, multiplication, and division.

Decimal Support: Allows floating-point calculations.

Error Handling: Displays ERROR when attempting division by zero.

Utility Functions: Clear all input, delete last character, and add decimal point.

Interactive GUI: Large, styled buttons with intuitive layout.

Dynamic Input: Users can build expressions step by step and evaluate them with the = button.

🛠️ Technologies Used
Python 3

Tkinter (standard Python GUI library)

📂 Code Structure
Entry Box: Displays current input and results.

Functions:

click(Number) → Appends digits.

clear() → Clears all input.

delete() → Deletes last character.

decimal_point() → Adds a decimal.

add(), subtract(), multiply(), divide() → Store first number and operation.

equal() → Performs calculation and displays result.

Buttons: Numeric, operator, and utility buttons created with tk.Button.

Layout: Organized using grid() for neat positioning.

🚀 Example Run
Code
Input: 12 + 8
Output: 20

Input: 15 ÷ 0
Output: ERROR
🎯 Learning Outcomes
This project demonstrates:

GUI design with Tkinter (Button, Entry, grid).

Event-driven programming with command callbacks.

Handling user input/output dynamically.

Error handling in arithmetic operations.

Building a structured, interactive Python application.

📌 Future Improvements
Add support for multiple chained operations.

Implement keyboard input support.

Improve error handling for invalid inputs (e.g., multiple decimals).

Add scientific functions (square root, power, etc.).

Create a more compact and responsive layout.
