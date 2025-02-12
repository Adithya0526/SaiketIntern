import tkinter as tk
from tkinter import messagebox
import random

# Initialize variables
random_number = None
guess_count = 0  # To keep track of the number of guesses

# Function to generate a random number and reset the game
def start_game():
    global random_number,guess_count
    random_number = random.randint(1,100)
    guess_count = 0  # Reset guess count
    guess_entry.delete(0,tk.END)  # Clear the input field
    result_label.config(text="Game started! Try guessing the number.")
    count_label.config(text="Guess Count: 0")  # Reset guess count display
    messagebox.showinfo("Game Started","A random number between 1 and 100 has been generated. Try to guess it!")

# Function to check the user's guess
def check_guesss(event=None):
    global random_number,guess_count
    if random_number is None:  # Check if the game has started
        messagebox.showerror("Error","Please start the game first!")
        return
    
    try:
        user_guess=int(guess_entry.get())  # Get the user input and convert to integer
        guess_count +=1  # Increment guess count
        count_label.config(text=f"Guess Count: {guess_count}")  # Update guess count display

        if user_guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif user_guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text="Congratulations! You guessed it!")
            messagebox.showinfo("Success",f"You guessed the correct number in {guess_count} attempts!")
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter a valid number.")


# Create the main application window
root=tk.Tk()
root.title("Number Guessing Game")

#Set full screen 
root.attributes("-fullscreen",True)

#Colours
bg_color="#e6f7ff"  # Light blue background
btn_color="#66ccff"  # Button color
text_color="#004d80"  # Dark blue text

#Set background colour
root.configure(bg=bg_color)

#Title label 
title_label=tk.Label(root,text="Number Guessing Game",font=("Arial",24,"bold"),bg=bg_color,fg=text_color)
title_label.pack(pady=20)

#Instruction label 
instruction_label=tk.Label(root,text="Guess a number between 1 and 100",font=("Arial",16),bg=bg_color,fg=text_color)
instruction_label.pack(pady=10)

#entry field for user input 
guess_entry=tk.Entry(root,font=("Arial",16),width=10,justify='center')
guess_entry.pack(pady=20)

#Bind Enter key to check_guess
guess_entry.bind("<Return>",check_guesss)

#buttons
start_button=tk.Button(root,text='Start Game',font=("Arial",16),bg=btn_color,fg="white",command=start_game)
start_button.pack(pady=10)
check_button=tk.Button(root,text="Check Guess",font=("Arial",16),bg=btn_color,fg="white",command=check_guesss)
check_button.pack(pady=10)

#label to show the number of guesses
count_label=tk.Label(
    root,text="Guess Count :0",font=("Arial",16),
    bg=bg_color,fg=text_color
)
count_label.pack(pady=10)

#label to show the result 
result_label=tk.Label(root,text="",font=("Arial",16),bg=bg_color,fg=text_color)
result_label.pack(pady=20)

#Add an exit button to close the full screen mode 
exit_button=tk.Button(
    root,text="Exit Game",font=("Arial",16),bg="red",fg="white",command=root.destroy
)
exit_button.pack(pady=10)

#Center all widgetrs
for widget in root.winfo_children():
    widget.pack_configure(anchor="center")

# Start the main event loop
root.mainloop()
