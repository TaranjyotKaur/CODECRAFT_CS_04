# CODECRAFT_CS_04

# 🔑 Simple Python Keylogger

This is a basic keylogger built with [pynput](https://pynput.readthedocs.io/) in Python.  
It records keystrokes and saves them to a text file (`log.txt`).  
The program automatically stops when the **Escape (Esc)** key is pressed.  

---

## 🚀 Features
- Logs all keystrokes to a file (`log.txt`).
- Handles special keys like **Space**, **Enter**, **Shift**, and **Ctrl**.
- Stops gracefully when the **Esc** key is pressed.
- Cross-platform (works on Windows, Linux, and macOS).

---

## 📦 Requirements
- Python 3.x  
- `pynput` library  

Install dependencies with:
```
pip install pynput
```

🖥️ Usage
Clone this repository:
```
git clone https://github.com/your-username/python-keylogger.git
cd python-keylogger
```
Run the script:
```
python keylogger.py
```
Keystrokes will be saved in  (`log.txt`).

Press Esc anytime to stop the logger.

