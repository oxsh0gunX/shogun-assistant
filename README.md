# 🛡️ Shogun Assistant

Shogun Assistant is a lightweight Linux automation assistant built in Python.  
It uses a wake word system and executes system commands using Python's subprocess module.

This project is designed as a learning-based prototype evolving into a structured automation tool.

---

## 🚀 Features

- Wake word activation (`shogun`)
- Dictionary-based command execution
- Safe command validation
- Terminal wrapping for TUI applications (e.g., btop)
- Error handling for missing applications
- Prototype development tracking

---

## 📂 Project Structure

shogun-assistant/
│
├── proto/ # Early prototype versions
│ ├── proto_1.py
│ ├── proto_2.py
│
├── src/ # Stable version
│ └── assistant.py
│
├── README.md
└── requirements.txt


---

## ⚙️ Requirements

- Python 3.10+
- Linux OS
- terminator (optional)
- btop (optional)

Install required tools:

```bash
sudo apt install terminator btop


▶️ Usage

Run the assistant: python src/assistant.py


Example commands:
shogun open terminal
shogun open brave
shogun open btop




🧠 How It Works

User input is captured.

Wake word is validated.

Command is parsed and cleaned.

The command is matched against a dictionary.

Matching system command is executed using subprocess.Popen().
🔒 Error Handling

Unknown commands are safely handled.

Missing applications will not crash the program.

Input validation prevents execution without wake word.

📈 Roadmap

Future improvements:

Flexible natural language matching

Dynamic application opening

Process management (close apps)

Command logging system

Voice recognition integration

Modular architecture refactor

🎯 Purpose

This project is built as:

A Linux automation experiment

A learning project for Python system programming

A portfolio-ready demonstration of structured software design

⚠️ Disclaimer

This tool executes system commands.
Use responsibly.

👤 Author

Safvan (0xSh0gunX)
