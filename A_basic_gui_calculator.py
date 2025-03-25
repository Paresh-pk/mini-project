import ast
from tkinter import *

expression = ""

def press(num):
    """Handles button presses and updates the expression."""
    global expression
    expression += str(num)
    equation.set(expression)  # Update the display

def calculate():
    """Evaluates the mathematical expression safely."""
    try:
        global expression
        total = str(ast.literal_eval(expression))  # Evaluate safely
        equation.set(total)  # Show result
        expression = total  # Allow chaining of operations
    except Exception as e:
        equation.set("Error")  # Display error
        expression = ""

def calculate_percentage():
    """Converts the expression into a percentage (divides by 100)."""
    try:
        global expression
        total = str(ast.literal_eval(expression) / 100)  # Compute percentage
        equation.set(total)  # Show result
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    """Clears the calculator display."""
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    # Create GUI Window
    gui = Tk()
    gui.configure(background="black")
    gui.title("Simple Calculator")
    gui.geometry("400x500")  # Fixed geometry format

    equation = StringVar()  # Holds the expression for display
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 20, "bold"), justify="right")
    expression_field.grid(columnspan=4, ipadx=70, pady=20)

    # Define button layout
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "%", "+"]
    ]

    # Create buttons dynamically
    for i in range(4):
        for j in range(4):
            button_text = buttons[i][j]

            if button_text == "%":
                button = Button(
                    gui,
                    text=button_text,
                    fg="black",
                    bg="red",
                    font=("Arial", 20, "bold"),
                    command=calculate_percentage,
                    height=1,
                    width=7,
                )
            else:
                button = Button(
                    gui,
                    text=button_text,
                    fg="black",
                    bg="red",
                    font=("Arial", 20, "bold"),
                    command=lambda x=button_text: press(x),
                    height=1,
                    width=7,
                )
            button.grid(row=i + 2, column=j)

    # Clear button
    clear_button = Button(
        gui,
        text="Clear",
        fg="black",
        bg="red",
        font=("Arial", 20, "bold"),
        command=clear,
        height=1,
        width=14,  # Make it wider
    )
    clear_button.grid(row=6, column=0, columnspan=2)

    # Equal button
    equal_button = Button(
        gui,
        text="=",
        fg="black",
        bg="red",
        font=("Arial", 20, "bold"),
        command=calculate,
        height=1,
        width=14,  # Make it wider
    )
    equal_button.grid(row=6, column=2, columnspan=2)

    # Run the GUI
    gui.mainloop()
