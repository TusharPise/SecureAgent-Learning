# 🛡️ Secure Math Agent

A simple AI-powered Math Agent with a 3-layer security architecture to resist prompt injection and prompt leakage attacks.

## Features

- Solves mathematical problems
- Rule-based input filtering
- AI Security Judge
- Prompt injection protection
- Simple web interface

## Requirements

- Python 3.11+
- Gemini API Key

## Installation

Clone the repository:

```bash
git clone https://github.com/TusharPise/SecureAgent-Learning.git
cd SecureAgent-Learning
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python web.py
```

Open your browser:

```
http://127.0.0.1:5000
```

## Project Structure

```
agent/
├── brain.py
├── llm.py
├── security.py
└── security_ai.py

app.py
web.py
requirements.txt
```

## Security Architecture

1. System Prompt (Behavior Layer)
2. Rule-Based Input Filter
3. AI Security Judge

## Version

v1.0
