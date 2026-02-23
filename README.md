# Password Auditing Tool

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Security](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Hashing](https://img.shields.io/badge/Cryptography-SHA256-green)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A GUI-based password security auditing tool built using Python and Tkinter.  
The tool performs password strength analysis, secure SHA-256 hashing, and dictionary-based attack simulation using the RockYou wordlist.

---

## 🚀 Features

- Password strength evaluation  
- SHA-256 secure hashing  
- RockYou-based dictionary attack simulation  
- Real-time cracking performance measurement  
- Automated security report generation  
- User-controlled report export  
- Clean graphical interface  

---

## 🛠️ Tech Stack

- Python  
- Tkinter (GUI Framework)  
- hashlib (SHA-256)  
- RockYou Wordlist  
- Linux  

---

## 📦 Installation & Usage

### 1️⃣ Install Python

Make sure Python 3 is installed:

```bash
python3 --version
```

### 2️⃣ Ensure RockYou Wordlist Exists

On Kali / Parrot:

```bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
cp /usr/share/wordlists/rockyou.txt .
```

### 3️⃣ Run the Application

```bash
python3 password_tool_gui.py
```

---

## 🧠 How It Works

1. The user enters a password.  
2. The system evaluates strength based on:
   - Length  
   - Uppercase & lowercase characters  
   - Numbers  
   - Special characters  
3. The password is securely hashed using SHA-256.  
4. A dictionary attack simulation is performed using RockYou.  
5. Results are displayed in the GUI and can be exported as a structured report.  

---

## 📊 Security Concepts Implemented

- Password Strength Analysis  
- Cryptographic Hashing (SHA-256)  
- Dictionary Attack Simulation  
- Performance Timing Measurement  
- Security Reporting  
- Ethical Hacking Principles  

---

## ⚠️ Disclaimer

This project is intended strictly for educational purposes and authorized lab environments only.  
Do NOT use this tool for unauthorized password cracking.

---

## 📌 Future Improvements

- Multi-threaded cracking engine  
- Brute-force mode  
- Progress bar for large wordlists  
- PDF report export  
- Integration with vulnerability assessment modules  

---

## 👨‍💻 Author

**Aroh Maurya**  
GitHub: https://github.com/aroh3006  

---

⭐ If you found this useful, consider giving the repository a star.
