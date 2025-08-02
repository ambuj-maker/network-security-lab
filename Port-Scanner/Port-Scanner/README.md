# 🔍 Port Scanner

This is a simple Python-based port scanner that checks for open TCP ports on a given IP address.

---

## 📁 File Information

- `port_scanner.py`: The main script that performs the port scan.

---

## ⚙️ How It Works

The script uses Python’s built-in `socket` module to attempt TCP connections on each port in the range 1–1024.  
If a connection is successful, the port is considered open.

---

## ▶️ How to Run

```bash
python3 port_scanner.py
```

---

## 🧪 Sample Output

```
Enter the target IP: 127.0.0.1

Scanning 127.0.0.1...

Port 22 is OPEN  
Port 80 is OPEN  
Port 443 is OPEN
```

---

## 📌 Notes

- Default port range: 1 to 1024  
- Timeout per port: 0.5 seconds  
- Ensure you have permission to scan the target

---

## 👤 Author

**Ambuj Pandey**  
GitHub: [@ambuj-maker](https://github.com/ambuj-maker)
