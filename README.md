# Linear Equation Solver in Python

A simple script to solve linear equations of the form:

ax = b²  →  x = b² / a

This tool uses Python's `fractions` module to convert decimal values into fractions, ensuring precise and accurate calculation.

🧮 How It Works

Given:
- `a`: a decimal number
- `b`: an integer

The equation is:

a * x = b²

To find `x`, we solve:

x = b² / a

Python handles this by first converting `a` into a `Fraction` for precision, then divides `b²` by `a`.

💡 Example

python
a = 0.2
b = 5

Equation:

0.2x = 5² = 25
x = 25 / 0.2 = 125

Output:

125


📄 How to Use

1. Make sure you have Python 3 installed.


2. Run the script:



python solve_linear_equation.py

3. Input values for a and b when prompted.


📦 Requirements

Python 3.x

Standard library only (no extra packages needed)


📁 File Structure

linear-equation-solver-python/
├── solve_linear_equation.py
└── README.md


👤 Author

Made by Rama Prasetya
A simple tool from a self-taught coder's journey ✨


