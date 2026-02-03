# 🔐 Phishing URL Detection System

This project is a simple web application that checks whether a given website URL looks **safe**, **suspicious**, or **phishing** based on common phishing patterns.

The application is developed using **Python Flask** and basic rule-based logic. It is intended for learning and demonstration purposes.

---

## 📖 About the Project

Phishing websites try to trick users into giving sensitive information such as passwords, bank details, or OTPs.  
This project helps in identifying such URLs by analyzing their structure.

The system does **not use real-time internet scanning**.  
Instead, it checks the URL format and applies logical rules to classify it.

---

## ✨ Features

- Enter any website URL
- Detect common phishing indicators
- Classifies URLs as:
  - Safe
  - Suspicious
  - Phishing
- Displays a risk score and reasons
- Simple and clean user interface

---

## ⚙️ How It Works

The application checks the URL for:
- Length of the URL
- HTTPS availability
- Special characters like `@` and `-`
- Use of IP address instead of domain name

Based on these checks, a score is calculated and the final result is shown to the user.

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Git & GitHub

---

## 📂 Project Structure (Screenshots)

The following screenshots show the structure of the project files and folders used in this application.

### Structure View 1
![Project Structure View 1](screenshots/structure-1.png)


---

### Structure View 2
![Project Structure View 2](screenshots/structure-2.png)


---

### Structure View 3
![Project Structure View 3](screenshots/structure-3.png)

