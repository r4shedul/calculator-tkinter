import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

display = tk.Entry(root, font=("Segoe UI", 22), bd=8, relief=tk.FLAT, justify='right', bg="#f2f2f2")
display.pack(fill=tk.BOTH, ipadx=10, ipady=20, padx=12, pady=12)

def click(event):
    btn_text = event.widget.cget("text")
    if btn_text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif btn_text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, btn_text)

button_frame = tk.Frame(root, bg="#d9d9d9")
button_frame.pack(padx=10, pady=0, fill="both", expand=True)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame, bg="#d9d9d9")
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(row_frame, text=btn, font=("Segoe UI", 18), bd=0, bg="#ffffff", activebackground="#e6e6e6")
        b.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        b.bind("<Button-1>", click)

root.mainloop()
