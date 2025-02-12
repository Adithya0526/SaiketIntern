import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            data = response.json()
            joke = f"{data['setup']}\n\n{data['punchline']}"
            joke_var.set(joke)
        else:
            joke_var.set("Failed to fetch joke. Try again!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network Error: {e}")

# GUI setup
root = tk.Tk()
root.title("Random Joke Fetcher")
root.geometry("400x200")
root.resizable(False, False)

frame = ttk.Frame(root, padding="10")
frame.pack(expand=True, fill="both")

# Button to fetch joke
fetch_button = ttk.Button(frame, text="Get a Joke", command=fetch_joke)
fetch_button.pack(pady=10)

# Label to display joke
joke_var = tk.StringVar()
joke_label = ttk.Label(frame, textvariable=joke_var, wraplength=350, justify="center", font=("Arial", 12))
joke_label.pack(pady=10)

root.mainloop()
