import tkinter as tk
from main import shopping_online_run

def print_input_value():
    location = e1.get()
    keyword = e2.get()
    page = e3.get()
    root.destroy()
    shopping_online_run(location, keyword, page)

# Create the main tkinter window
root = tk.Tk()
root.title("Shopping Online Info")
root.geometry("600x300")

tk.Label(root, text='Location: ', padx=100,pady=10).grid(row=0)
tk.Label(root, text='Keyword: ', padx=100, pady=10).grid(row=1)
tk.Label(root, text='Page: ', padx=100, pady=10).grid(row=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

# Create a button to trigger printing the input value
print_button = tk.Button(root, text="Print Input Value", command=print_input_value)
print_button.grid(row=4, column=1)

# Start the tkinter main loop
root.mainloop()