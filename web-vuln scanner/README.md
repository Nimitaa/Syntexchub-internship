# Web Vulnerability Scanner 🔍

A Python-based web vulnerability scanner that detects reflected XSS vulnerabilities by crawling web pages,
injecting payloads, and analyzing responses.

# 🚀 Features
- Web crawler (link + form extraction)
- XSS payload injection
- Reflection-based detection
- JSON vulnerability reporting

# 🛠️ Tech Stack
- Python
- requests
- BeautifulSoup

#  📂 Project Structure
- crawler → finds pages & forms
- injector → sends payloads
- detector → checks for XSS
- reporter → saves results

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py

⚠️ Disclaimer
Only test on permitted environments like:
DVWA
OWASP Juice Shop

📌 Future Improvements
Context-aware XSS detection
Multi-threaded scanning
GUI dashboard
Authentication support
