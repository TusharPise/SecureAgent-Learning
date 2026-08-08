# 🛡️ Secure AI Agent

A security-focused AI math agent with layered input protection, AI-based security validation, and a web interface for live testing.

## 🚀 Features

- 🔐 User-provided Gemini API key
- ✅ API-key validation before using the agent
- 🛡️ Regex-based prompt-injection filtering
- 🤖 AI-based security judge
- 🧮 Math-only AI agent
- 📐 LaTeX equation rendering
- 🧠 Lightweight session-based memory
- 🔒 Isolated memory between user sessions
- 🌐 Web-based chat interface
- 📱 Responsive interface

## 🏗️ Architecture

```text
User
 │
 ▼
Web Interface
 │
 ▼
Flask Backend
 │
 ├── API Key Validation
 │
 ▼
Input Security Filter
 │
 ▼
AI Security Judge
 │
 ▼
Math Agent
 │
 ▼
Gemini API
 │
 ▼
Response
