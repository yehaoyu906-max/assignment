#Name: [Ye Haoyu]
#Assignment One
#ddl is 22/9/2026 23:59pm

#Calculator HINT
print("Simple Calculator")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
op = input("Choose operation(+,-,*,/):")
if op == "+":
    print("Result:",num1 + num2)
elif op == "-":
    print("Result:",num1 - num2)
elif op == "*":
    print("Result:",num1 * num2)
elif op == "/":
    print("Result:",num1 / num2)
else:
    print("Invalid operation")

#QA BOT HINT
print("Question Answering Bot")
question = input("Ask me something:")
if question == "hello":
    print("Bot: Hello! Nice to meet you.")
elif question == "python":
    print("Bot: Python is a language.")
elif question == "jetson":
    print("Bot: Jetson Nano is an AI computer.")
elif question == "ai":
    print("Bot: AI means Artificial Intelligence.")
elif question == "name":
    print("Bot: My name is Python Bot.")
else:
    print("Bot: Sorry, I don't understand.")


