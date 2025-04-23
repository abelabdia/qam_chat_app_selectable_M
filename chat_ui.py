import tkinter as tk
from chat_backend import send_message, start_receiver_thread

def send():
    msg = entry.get()
    selected_M = int(qam_option.get())
    if msg:
        send_message(msg, selected_M)
        chat_window.insert(tk.END, "You: " + msg + "\n")
        entry.delete(0, tk.END)

# UI setup
root = tk.Tk()
root.title("Raspberry Pi QAM Chat")

chat_window = tk.Text(root, height=20, width=50)
chat_window.pack()

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(root, text="Send", command=send)
send_button.pack(side=tk.RIGHT, padx=5)

# QAM Selector
qam_option = tk.StringVar(root)
qam_option.set("16")  # default value
qam_menu = tk.OptionMenu(root, qam_option, "4", "8", "16", "64", "256")
qam_menu.pack()

# Start listener
start_receiver_thread(chat_window, qam_option)

root.mainloop()