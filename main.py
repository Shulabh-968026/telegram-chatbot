import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import requests
from dotenv import load_dotenv
from typing import Final

load_dotenv()
TOKEN: Final = os.getenv("TOKEN")
CHAT_ID: Final = os.getenv("CHAT_ID")


def chatbot(message: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)


# create a root window
root = tk.Tk()
root.title("Python Telegram Bot")
root.geometry("500x400")
root.resizable(False, False)
root.config(background="pink")

# create a label
label_text = "Python Telegram Bot".upper()
spaced_text = " ".join(label_text)
label = ttk.Label(
    root,
    text=spaced_text,
    font=("Segoe UI", 20),
    foreground="blue",
    background="pink",
    padding=10,
)
label.pack(pady=20)

# create a text area field
text_area = tk.Text(
    root,
    width=38,
    height=5,
    font=("Segoe UI", 15),
    padx=10,
    pady=10,
    background="pink",
)
text_area.pack(pady=10)


# create a function for focusing the text area
def focus_text_area(event):
    text_area.focus()


# bind the function to the root window
root.bind("<Key>", focus_text_area)


# create a function for clearing the text area
def clear_message():
    text_area.delete("1.0", "end")


# create a function for sending message
def send_message():
    message = text_area.get("1.0", "end-1c").strip()
    if not message:
        messagebox.showwarning("Warning", "Please enter a message")
        return
    else:
        chatbot(message)
        messagebox.showinfo("Success", "Message sent successfully")
        clear_message()


# create a button for sending message
button = ttk.Button(
    root,
    text="Send Message",
    command=send_message,
)
button.pack(pady=10, ipadx=5, ipady=5, side=tk.LEFT, expand=True)

# create a button for clearing the text area
clear_button = ttk.Button(
    root,
    text="Clear",
    command=clear_message,
)
# remove the pack methods for the buttons
clear_button.pack(pady=10, ipadx=5, ipady=5, side=tk.RIGHT, expand=True)

# bind the Enter key to the send_message function
root.bind("<Return>", lambda event=None: send_message())

# run the mainloop
root.mainloop()
