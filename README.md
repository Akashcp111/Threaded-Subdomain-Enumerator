# 🔎 Threaded Subdomain Enumerator

A high-performance subdomain discovery tool built with Python to help security researchers, penetration testers, and bug bounty hunters enumerate live subdomains of a given domain.

The tool is designed for speed, stability, and clarity, combining multithreading, retry mechanisms with exponential backoff, SOC-style colored output, and structured logging. Unlike basic scanners, this project provides real-time visibility into scanning progress while maintaining a clean log of discovered subdomains.

## ✨ Key Features
* 🚀 Multithreaded Enumeration
Utilizes Python’s ThreadPoolExecutor to scan subdomains concurrently without overwhelming system resources.
* 🌐 HTTP & HTTPS Support
Checks both http:// and https:// versions of each subdomain for completeness.
* ⏳ Smart Retry System
Implements exponential backoff retries to handle unstable networks gracefully.
Example: waits 1s → 2s → 4s before retrying failed requests.

     - 🖥 SOC-Style Console Output
     - 🟢 Green → Found subdomain
     - 🟡 Yellow → Retrying request
     - 🔴 Red → Failed request

* 📊 Progress Tracking
Uses tqdm to display a real-time progress bar showing how many subdomains have been tested.
* 📝 Structured Logging
   - Saves only successful discoveries in scan_log.txt with timestamps
   - Produces a clean, audit-friendly log file for further analysis

* 📂 Result Export

All discovered subdomains are stored in discovered_subdomains.txt for easy integration with other security tools.

### 📸 Example Output
```
Console Output
Scanning:  63%|███████████████████▎      | 126/200 [00:14<00:08,  9.15subdomain/s]
[+] Discovered subdomain: http://mail.youtube.com
[!] Retrying https://vpn.youtube.com (attempt 2/3)
[-] Failed: http://fake.youtube.com
[+] Discovered subdomain: https://accounts.youtube.com

✅ Scan complete! 12 subdomains found. Results saved to discovered_subdomains.txt
```
Log File (scan_log.txt)
```
2025-08-29 22:05:12 - Discovered subdomain: http://mail.youtube.com
2025-08-29 22:05:14 - Discovered subdomain: https://vpn.youtube.com
2025-08-29 22:06:00 - ✅ Scan complete! 12 subdomains found. Results saved to discovered_subdomains.txt
```

## ⚡ Installation

Clone the repository:
```
git clone https://github.com/yourusername/subdomain-enumerator.git
cd subdomain-enumerator
```

Install dependencies:
```
pip install -r requirements.txt
```

Or manually install:
```
pip install requests tqdm colorama
```
## 🚀 Usage

Create a file named subdomains.txt containing potential subdomains:
```
mail
vpn
accounts
dev
api
```

Run the script:
```
python subdomain_enum.py
```

Results:
* Console output → live updates with colors
* discovered_subdomains.txt → list of found subdomains
* scan_log.txt → timestamped log of all discoveries

📦 Project Structure
```
📂 subdomain-enumerator/
 ├── subdomain_enum.py          # Main script
 ├── subdomains.txt             # Input subdomains wordlist
 ├── discovered_subdomains.txt  # Output: discovered subdomains
 ├── scan_log.txt               # Output: log file (with timestamps)
 └── requirements.txt           # Python dependencies
```
## 🔮 Roadmap / Future Enhancements

 * Asynchronous scanning (aiohttp) for ultra-fast performance
 * JSON/CSV output formats for SIEM/Splunk integration
 * Automatic wordlist fetch from SecLists / ProjectDiscovery
 * CNAME & DNS record resolution for deeper subdomain intel
 * Integration with third-party APIs (Shodan, SecurityTrails, VirusTotal)

## 🛡 Use Cases

* Bug bounty hunting → Find hidden subdomains & entry points
* Penetration testing → Map attack surface quickly
* Red Teaming → Automate reconnaissance in engagements
* Security monitoring → Track newly alive subdomains over time

## ⚠ Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Do not use it against systems you don’t own or have explicit permission to test.
The author is not responsible for any misuse of this tool.
