#Name: [Ye Haoyu]
#Assignment One
#ddl is 22/9/2026 23:59pm

import turtle  # used by Task C

# ==================================================================
# Task A - Simple Calculator
# A terminal-based calculator that processes user inputs using a
# structured for loop. It prompts for two numbers and an operator
# (+, -, *, /), then displays a clear math result.
# ==================================================================
def task_a_calculator():
    print("=" * 50)
    print("Simple Calculator")
    print("=" * 50)

    # Structured for loop: the user chooses how many calculations
    # to perform (default 3 rounds).
    try:
        rounds = int(input("How many calculations do you want to do? (default 3): ") or 3)
    except ValueError:
        rounds = 3

    for i in range(1, rounds + 1):
        print(f"\n--- Calculation {i} of {rounds} ---")

        # Prompt for the two numbers (re-prompt until valid numbers)
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter numeric values.")
            continue

        op = input("Choose operation (+, -, *, /): ")

        # Clear math result for each operator
        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Result: Error - cannot divide by zero!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation! Please choose +, -, *, or /.")

    print("\nCalculator finished. Thanks for using it!")


# ==================================================================
# Task B - QA Bot
# An interactive bot that matches user questions using conditional
# (if / elif / else) logic. Supports at least 5 keywords:
# hello, python, jetson, ai, name.
# ==================================================================
def task_b_qa_bot():
    print("=" * 50)
    print("Question Answering Bot")
    print("Type 'quit' to exit the bot.")
    print("=" * 50)

    while True:
        question = input("\nAsk me something: ").strip().lower()

        if question == "quit":
            print("Bot: Goodbye! See you next time.")
            break
        elif question == "hello":
            print("Bot: Hello! Nice to meet you.")
        elif question == "python":
            print("Bot: Python is a language.")
        elif question == "jetson":
            print("Bot: Jetson Nano is an AI computer.")
        elif question == "ai":
            print("Bot: AI means Artificial Intelligence.")
        elif question == "name":
            print("Bot: My name is Python Bot.")
        elif "how are you" in question:
            print("Bot: I am doing great, thank you for asking!")
        elif question in ("help", "what can you do"):
            print("Bot: Try asking me: hello, python, jetson, ai, name ...")
        else:
            print("Bot: Sorry, I don't understand.")


# ==================================================================
# Task C - Turtle Drawing
# Showcase creativity using Python's built-in vector drawing engine:
#   - draw a star
#   - draw a square, triangle and a colourful rotating pattern
#   - dynamically change colour & length inside a for loop
# ==================================================================
def task_c_turtle_drawing():
    print("=" * 50)
    print("Turtle Drawing - colourful patterns")
    print("(A drawing window will pop up)")
    print("=" * 50)

    pen = turtle.Turtle()
    pen.speed(0)          # fastest drawing speed
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Assignment 1 - Task C Turtle Drawing")

    colours = ["red", "orange", "yellow", "green",
               "cyan", "blue", "purple", "magenta"]

    # --- 1) A star -------------------------------------------------
    pen.penup()
    pen.goto(-200, 100)
    pen.pendown()
    pen.color("gold")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(100)
        pen.right(144)
    pen.end_fill()

    # --- 2) A square + triangle with dynamic colour & length -------
    # Structured for loop: each round the length grows and the
    # pen colour changes, producing a colourful rotating pattern.
    length = 20
    for i in range(36):
        pen.color(colours[i % len(colours)])   # dynamically change colour
        # Draw a square with the current length
        for _ in range(4):
            pen.forward(length)
            pen.right(90)
        # Draw a triangle on top with the same dynamic colour
        for _ in range(3):
            pen.forward(length)
            pen.left(120)
        pen.right(10)                          # rotate the whole pattern
        length += 5                            # dynamically change length

    pen.hideturtle()
    screen.mainloop()


# ==================================================================
# Main entry point
# ==================================================================
def main():
    task_a_calculator()
    task_b_qa_bot()
    task_c_turtle_drawing()


if __name__ == "__main__":
    main()

