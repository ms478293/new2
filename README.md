# 🛡️ ClearDNS Security Platform (Prototype)

> **AI-powered DNS security with advanced threat scoring and phishing-aware filtering.**

A lightweight, extensible DNS-over-HTTPS (DoH) resolver that blocks malware, phishing, and suspicious domains using real-time threat feeds and machine learning.

🔐 Protects against:
- Phishing & brand impersonation
- Malware & ransomware domains
- Typosquatting & homograph attacks
- Data exfiltration via DNS

---

## 🚀 Features

- ✅ DNS-over-HTTPS (DoH) proxy
- ✅ Real-time threat blocking (Abuse.ch, PhishTank)
- ✅ AI-powered domain risk scoring
- ✅ Sub-millisecond filtering
- ✅ Simple web dashboard
- ✅ Log & audit trail

---

## 🧰 Requirements

- Python 3.8+
- Internet connection

---

## 🔧 Setup

```bash
# Clone repo
git clone https://github.com/yourusername/cleardns.git
cd cleardns

# Setup environment
bash scripts/bootstrap.sh
```

---

## ▶️ Run

```bash
# 1. Update threat feeds
python src/threat_feed_loader.py

# 2. Train AI model
python src/ai_scoring.py

# 3. Start DNS proxy (port 8053)
python src/doh_proxy.py

# 4. Open dashboard (port 5000)
python src/dashboard.py
```

Then set your device DNS to:
```
https://127.0.0.1:8053/dns-query
```

> ⚠️ For real deployment, use a public server and TLS.

---

## 📊 Dashboard

Visit: `http://127.0.0.1:5000`

---

## 🤝 Contribute

PRs welcome! Ideas:
- Add homograph detection
- Support DoT
- Add Cloudflare/Quad9 upstream
- Improve UI with React

---

## 📄 License

MIT