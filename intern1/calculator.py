import tkinter as tk  # Import the tkinter library for GUI

# Function to handle button clicks
def click(event):
    value = entry.get()  # Get current entry value
    btn_text = event.widget.cget("text")  # Get text of clicked button
    if btn_text == "=":
        try:
            result = str(eval(value))  # Evaluate the expression
            entry.delete(0, tk.END)    # Clear entry
            entry.insert(0, result)    # Show result
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")   # Show error if invalid
    elif btn_text == "C":
        entry.delete(0, tk.END)        # Clear entry if 'C' is pressed
    else:
        entry.insert(tk.END, btn_text) # Add button text to entry

root = tk.Tk()                         # Create main window
root.title("Calculator")                # Set window title
root.configure(bg="#222831")            # Set background color

# Entry widget for input/output
entry = tk.Entry(root, font="Arial 22", justify="right", bg="#393e46", fg="#00fff5", bd=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

# List of calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Button color scheme
btn_bg = {
    "/": "#ff5722", "*": "#ff5722", "-": "#ff5722", "+": "#ff5722", "=": "#00adb5", "C": "#f44336"
}
btn_fg = {
    "=": "#fff", "C": "#fff"
}

# Place buttons in a grid
row, col = 1, 0
for text in buttons:
    bg = btn_bg.get(text, "#393e46")
    fg = btn_fg.get(text, "#eeeeee")
    btn = tk.Button(
        root, text=text, font="Arial 18 bold", width=4, height=2,
        bg=bg, fg=fg, activebackground="#00fff5", activeforeground="#222831", bd=2, relief=tk.RAISED
    )
    btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
    btn.bind("<Button-1>", click)      # Bind click event
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make the grid cells expand with window resize
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row+1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()                        # Start the GUI event loop