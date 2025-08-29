import requests
import time
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Logging configuration (only record discovered subdomains)
log_filename = "scan_log.txt"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Target domain
DOMAIN = "youtube.com"

# Read subdomains list
with open("subdomains.txt", "r") as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

# Session for connection reuse
session = requests.Session()

def fetch_url(url, retries=3, backoff=1):
    """Try a URL with retries + exponential backoff"""
    for attempt in range(retries):
        try:
            response = session.get(url, timeout=3)
            if response.status_code < 400:
                return True
        except requests.RequestException:
            if attempt < retries - 1:
                print(f"{Fore.YELLOW}[!] Retrying {url} (attempt {attempt+2}/{retries})")
            time.sleep(backoff * (2 ** attempt))  # exponential backoff
    print(f"{Fore.RED}[-] Failed: {url}")
    return False

def check_subdomain(subdomain):
    urls = [f"http://{subdomain}.{DOMAIN}", f"https://{subdomain}.{DOMAIN}"]
    for url in urls:
        if fetch_url(url):
            msg = f"Discovered subdomain: {url}"
            print(f"{Fore.GREEN}[+] {msg}")
            logging.info(msg)  # ✅ Only successful discoveries go to log
            return url
    return None

# Use thread pool with tqdm progress bar
with ThreadPoolExecutor(max_workers=50) as executor:
    futures = {executor.submit(check_subdomain, sub): sub for sub in subdomains}
    for future in tqdm(as_completed(futures), total=len(futures), desc="Scanning", unit="subdomain"):
        result = future.result()
        if result:
            discovered_subdomains.append(result)

# Save results
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        f.write(subdomain + "\n")

summary_msg = f"✅ Scan complete! {len(discovered_subdomains)} subdomains found. Results saved to discovered_subdomains.txt"
print(f"\n{Fore.GREEN}{summary_msg}{Style.RESET_ALL}")
logging.info(summary_msg)

