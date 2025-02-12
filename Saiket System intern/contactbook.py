import tkinter as tk
from tkinter import messagebox, ttk

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        update_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields must be filled!")

def update_list():
    contact_list_add.delete(0, tk.END)
    contact_list_search.delete(0, tk.END)
    contact_list_delete.delete(0, tk.END)
    for contact in contacts:
        contact_text = f"{contact['name']} - {contact['phone']}"
        contact_list_add.insert(tk.END, contact_text)
        contact_list_search.insert(tk.END, contact_text)
        contact_list_delete.insert(tk.END, contact_text)

def search_contact():
    query = search_entry.get().lower()
    contact_list_search.delete(0, tk.END)
    for contact in contacts:
        if query in contact["name"].lower():
            contact_list_search.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected_index = contact_list_delete.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        update_list()
    else:
        messagebox.showwarning("Selection Error", "No contact selected!")

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Add Contact Tab
add_tab = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(add_tab, text="Add Contact")

tk.Label(add_tab, text="Name:", bg="#f0f8ff").pack()
name_entry = tk.Entry(add_tab)
name_entry.pack()

tk.Label(add_tab, text="Phone:", bg="#f0f8ff").pack()
phone_entry = tk.Entry(add_tab)
phone_entry.pack()

tk.Button(add_tab, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white").pack()
contact_list_add = tk.Listbox(add_tab, width=50, height=15)
contact_list_add.pack()

# Search Contact Tab
search_tab = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(search_tab, text="Search Contact")

tk.Label(search_tab, text="Search:", bg="#f0f8ff").pack()
search_entry = tk.Entry(search_tab)
search_entry.pack()
tk.Button(search_tab, text="Search", command=search_contact, bg="#2196F3", fg="white").pack()
contact_list_search = tk.Listbox(search_tab, width=50, height=15)
contact_list_search.pack()

# Delete Contact Tab
delete_tab = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(delete_tab, text="Delete Contact")

contact_list_delete = tk.Listbox(delete_tab, width=50, height=15)
contact_list_delete.pack()

tk.Button(delete_tab, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white").pack()

update_list()
root.mainloop()
