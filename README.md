# 🔐 Phishing URL Detection System

This project is a simple web application that checks whether a given website URL looks **Safe**, **Suspicious**, or **Phishing** based on common phishing patterns.

The application is built using **Python and Flask**. It uses rule-based logic to analyze URLs and is mainly created for learning and demonstration purposes.

---

## 📖 About the Project

Phishing websites try to trick users into sharing sensitive information such as passwords, bank details, or OTPs.  
This project helps in identifying such URLs by analyzing their structure.

The system does **not scan the internet** or use real-time data.  
Instead, it checks the format of the URL and applies logical rules to classify it.

---

## ✨ Features

- Enter any website URL
- Detect common phishing indicators
- Classifies URLs as:
  - ✅ Safe  
  - ⚠️ Suspicious  
  - 🚫 Phishing
- Shows risk score and reasons
- Simple and clean user interface

---

## ⚙️ How It Works

The application checks the URL for:
- URL length
- HTTPS availability
- Special characters such as `@` and `-`
- Use of IP address instead of domain name

Based on these checks, a score is calculated and the final result is displayed.

---

## 🛠️ Technologies Used

- Python  
- Flask  
- HTML  
- CSS  
- Git & GitHub  

---

## 📂 Project Structure

The screenshots below show how the project files and folders are organized.
### Structure View 1
<img src="https://raw.githubusercontent.com/harshachalla878-commits/phishing-url-detector/main/screenshots/structure-1.png" width="800"/>

---

### Structure View 2
<img src="https://raw.githubusercontent.com/harshachalla878-commits/phishing-url-detector/main/screenshots/structure-2.png" width="800"/>

---

### Structure View 3
<img src="https://raw.githubusercontent.com/harshachalla878-commits/phishing-url-detector/main/screenshots/structure-3.png" width="800"/>


---

## ▶️ How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/harshachalla878-commits/phishing-url-detector.git
2.	Move into the project folder:
   >>> cd phishing-url-detector
3.	Install Flask:
   >>> pip3 install flask
4.	Run the application:
   >>> python3 app.py
5.	Open your browser and go to:
   >>> http://127.0.0.1:10000
