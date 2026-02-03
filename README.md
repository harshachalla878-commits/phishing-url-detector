# 🔐 AI-Based Phishing URL Detection System

An AI-inspired cybersecurity web application that detects phishing websites by analyzing URL characteristics and classifying them as **Safe**, **Suspicious**, or **Phishing**.

This project is built using **Python Flask** with rule-based AI logic and a simple, user-friendly interface.

---

## 📌 Features

- Analyze any website URL
- Detect phishing patterns using URL features
- Classify URLs into:
  - ✅ Safe
  - ⚠️ Suspicious
  - 🚫 Phishing
- Display risk score and reasons for classification
- Clean and simple web interface

---

## 🧠 How It Works

The system extracts important features from the given URL, such as:
- URL length
- HTTPS usage
- Presence of special characters (`@`, `-`)
- IP address usage instead of domain

A rule-based AI scoring logic is applied to these features to determine the risk level of the URL.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Python, Flask  
- **AI Logic:** Rule-based inference  
- **Tools:** Git, GitHub  

---

## 📂 Project Structure
## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/harshachalla878-commits/phishing-url-detector.git
   cd phishing-url-detector
   pip3 install flask
   python3 app.py
   http://127.0.0.1:5000
   http://paypal.com@login-secure.example
   http://192.168.1.10/verify
   http://secure-login-google.example
---
