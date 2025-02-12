import tkinter as tk
from tkinter import ttk

def calculate_emi(*args):
    try:
        P = float(principal_var.get())
        annual_rate = float(rate_var.get())
        N = int(tenure_var.get())
        
        R = (annual_rate / 100) / 12  # Monthly interest rate
        EMI = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)
        
        result_var.set(f"EMI: {EMI:.2f}")
    except ValueError:
        result_var.set("Invalid Input")

root = tk.Tk()
root.title("Loan EMI Calculator")
root.geometry("400x250")
root.resizable(False, False)

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input Variables
principal_var = tk.StringVar()
rate_var = tk.StringVar()
tenure_var = tk.StringVar()
result_var = tk.StringVar()

# Labels and Entry Fields
ttk.Label(frame, text="Principal (P):").grid(row=0, column=0, sticky=tk.W, pady=5)
ttk.Entry(frame, textvariable=principal_var, width=20).grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Annual Interest Rate (%):").grid(row=1, column=0, sticky=tk.W, pady=5)
ttk.Entry(frame, textvariable=rate_var, width=20).grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Loan Tenure (Months):").grid(row=2, column=0, sticky=tk.W, pady=5)
ttk.Entry(frame, textvariable=tenure_var, width=20).grid(row=2, column=1, pady=5)

# Calculate Button
calculate_button = ttk.Button(frame, text="Calculate EMI", command=calculate_emi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result Display
ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold"), foreground="blue").grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
