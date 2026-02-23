import tkinter as tk
from tkinter import messagebox, filedialog
import re
import hashlib
import time
from datetime import datetime


WORDLIST = "rockyou.txt"

last_report = ""   # To store report for saving


def analyze_password():

    global last_report

    password = entry.get()

    if password == "":
        messagebox.showerror("Error", "Please enter a password")
        return


    # ---------------- Strength Check ----------------

    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1


    if score >= 6:
        strength = "VERY STRONG"
    elif score >= 4:
        strength = "STRONG"
    elif score >= 2:
        strength = "MEDIUM"
    else:
        strength = "WEAK"


    # ---------------- Hash ----------------

    target_hash = hashlib.sha256(password.encode()).hexdigest()


    output.delete(1.0, tk.END)

    output.insert(tk.END, "===== PASSWORD ANALYSIS =====\n\n")

    output.insert(tk.END, f"Strength     : {strength}\n")
    output.insert(tk.END, f"SHA-256 Hash : {target_hash}\n\n")


    # ---------------- Dictionary Attack ----------------

    output.insert(tk.END, "Starting Dictionary Attack (RockYou)...\n\n")

    start = time.time()

    found = False
    cracked = "Not Found"


    try:

        with open(WORDLIST, "r", errors="ignore") as file:

            for line in file:

                word = line.strip()

                word_hash = hashlib.sha256(word.encode()).hexdigest()

                if word_hash == target_hash:

                    end = time.time()

                    cracked = word
                    found = True

                    output.insert(tk.END, "⚠️ PASSWORD CRACKED!\n")
                    output.insert(tk.END, f"Password : {word}\n")
                    output.insert(tk.END, f"Time     : {end-start:.2f} seconds\n\n")

                    break


    except FileNotFoundError:

        messagebox.showerror("Error", "rockyou.txt not found!")
        return


    if not found:

        end = time.time()

        output.insert(tk.END, "✅ Password NOT found in RockYou\n")
        output.insert(tk.END, f"Time : {end-start:.2f} seconds\n")
        output.insert(tk.END, "Status: Relatively Strong\n\n")


    # ---------------- Report Generation ----------------

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time_now = now.strftime("%H:%M:%S")


    last_report = f"""
================================
 PASSWORD SECURITY AUDIT REPORT
================================

Date : {date}
Time : {time_now}

--------------------------------
Strength : {strength}
Hash     : {target_hash}

--------------------------------
Cracking Result
--------------------------------
Password : {cracked}
Status   : {"SUCCESS" if found else "FAILED"}
Time     : {end-start:.2f} seconds

--------------------------------
Remarks:
{"Weak password (found in RockYou)" if found else "Strong password (not in RockYou)"}

================================
"""


    output.insert(tk.END, "✔ Analysis Completed\n")
    output.insert(tk.END, "Click 'Save Report' to export\n")



def save_report():

    global last_report

    if last_report == "":
        messagebox.showerror("Error", "No report to save!")
        return


    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file == "":
        return


    with open(file, "w") as f:
        f.write(last_report)


    messagebox.showinfo("Success", "Report Saved Successfully!")



# ---------------- GUI ----------------

window = tk.Tk()
window.title("Password Security Tool - CEH Project")
window.geometry("850x620")


tk.Label(window, text="Enter Password:", font=("Arial", 11)).pack(pady=5)

entry = tk.Entry(window, width=40, show="*")
entry.pack(pady=5)


btn_frame = tk.Frame(window)
btn_frame.pack(pady=8)


tk.Button(
    btn_frame,
    text="Analyze Password",
    command=analyze_password,
    width=20
).grid(row=0, column=0, padx=5)


tk.Button(
    btn_frame,
    text="Save Report",
    command=save_report,
    width=20
).grid(row=0, column=1, padx=5)



output = tk.Text(window, height=26, width=100)
output.pack(pady=10)


window.mainloop()

