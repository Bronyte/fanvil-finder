# Fanvil Finder 🔎📞

Fanvil Finder is a simple Python tool for scanning your local network and detecting **Fanvil VoIP phones**.  
It works by probing the `default_user_config.txt` endpoint — Fanvil devices respond with **401 Unauthorized**, which is used as a detection signature.

---

## 🚀 Features
- Discover Fanvil VoIP phones on a specified IP range
- Detects devices via HTTP response behavior
- Saves results to `fanvil_ips.txt`
- Lightweight and dependency-minimal (`requests` only)

---

## ⚙️ Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/bronyte/fanvil-finder.git
cd fanvil-finder
pip install -r requirements.txt
python3 main.py
