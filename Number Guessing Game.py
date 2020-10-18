from tkinter import *
import random

# Game Specific variables

guess = 10
winning_no = random.randint(1, 100)

# Game function - Main function
def check_answer():

    # Global variables
    global guess
    global text

    guess -= 1
    attempts = int(entry_window.get())

    # Gameloop condition
    if attempts == winning_no:
        text.set("YOU WIN!!")
        text.set("Congratulations! You've guessed the correct number")
        btn_check.pack_forget()

    elif guess == 0:
        text.set("You are out of attempts!!")
        btn_check.pack_forget()

    elif attempts < winning_no:
        text.set(f"TOO LOW! You have {str(guess)} attempts remaining - Go Higher!!")

    elif attempts > winning_no:
        text.set(f"TOO HIGH! You have {str(guess)} attempts remaining - Go Lower!!")

    return

root = Tk()

root.title("Number Guessing Game by Shivam")

root.geometry("500x150")

label = Label(root, text="Guess the number between 1 & 100")
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check the answer", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit the game", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 10 attempts remaining! Good Luck!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()