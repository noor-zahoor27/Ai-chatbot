import tkinter as tk

# --------- Chatbot Logic ----------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 😊 How can I help you?"
    elif "your name" in user_input:
        return "I am an AI Chatbot built using Python 🤖"
    elif "ai" in user_input:
        return "Artificial Intelligence helps machines think like humans!"
    elif "python" in user_input:
        return "Python is a powerful language for AI and Machine Learning."
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a great day!"
    else:
        return "Sorry, I am still learning. Can you ask something else?"

# --------- Send Message Function ----------
def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_text + "\n")
    response = chatbot_response(user_text)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

# --------- GUI Window ----------
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("400x500")
window.config(bg="#f0f0f0")

# Chat Display Area
chat_area = tk.Text(window, height=20, width=45)
chat_area.pack(pady=10)

# User Input
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Buttons
send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack(pady=5)

exit_btn = tk.Button(window, text="Exit", command=window.quit)
exit_btn.pack(pady=5)

window.mainloop()
