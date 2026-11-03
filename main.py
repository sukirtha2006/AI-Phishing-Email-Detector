
import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model
model = joblib.load("model/phishing_model.pkl")


# Email checking function
def check_email():

    email = email_input.get("1.0", tk.END).strip()

    if not email:
        messagebox.showwarning(
            "Warning", "Please enter an email message!"
        )
        return

    prediction = model.predict([email])[0]
    probabilities = model.predict_proba([email])[0]
    confidence = max(probabilities) * 100

    if prediction == "phishing":
        result_text = "PHISHING EMAIL"
        result_color = "red"
    else:
        result_text = "LEGITIMATE EMAIL"
        result_color = "green"

    result_label.config(
        text=f"{result_text}\nModel score: {confidence:.2f}%",
        fg=result_color
    )

    # Save prediction report
    with open("security_report.txt", "a", encoding="utf-8") as file:
        file.write("\n--------------------------\n")
        file.write(f"Email: {email}\n")
        file.write(f"Prediction: {result_text}\n")
        file.write(f"Model score: {confidence:.2f}%\n")


# Clear function
def clear_email():
    email_input.delete("1.0", tk.END)
    result_label.config(text="")


# Main window
root = tk.Tk()
root.title("AI Phishing Email Detector")
root.geometry("600x450")
root.configure(bg="#eaf2f8")

# Heading
heading = tk.Label(
    root,
    text="AI PHISHING EMAIL DETECTOR",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8",
    fg="#1a237e"
)
heading.pack(pady=20)

# Instruction
instruction = tk.Label(
    root,
    text="Enter your email message below:",
    font=("Arial", 12),
    bg="#eaf2f8"
)
instruction.pack()

# Email input
email_input = tk.Text(
    root,
    height=8,
    width=55,
    font=("Arial", 11)
)
email_input.pack(pady=15)

# Check button
check_button = tk.Button(
    root,
    text="CHECK EMAIL",
    command=check_email,
    bg="#1976d2",
    fg="white",
    font=("Arial", 12, "bold")
)
check_button.pack(pady=5)

# Clear button
clear_button = tk.Button(
    root,
    text="CLEAR",
    command=clear_email,
    font=("Arial", 10)
)
clear_button.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#eaf2f8"
)
result_label.pack(pady=15)

# Disclaimer
disclaimer = tk.Label(
    root,
    text="Educational prototype. Verify suspicious emails independently.",
    font=("Arial", 9),
    bg="#eaf2f8",
    fg="gray"
)
disclaimer.pack()

root.mainloop()
