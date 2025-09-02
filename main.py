import requests
from ipaddress import ip_network

# ---------- CONFIGURATION ----------
IP_RANGE = "[IP RANGE]"  #Insert IP Range e.g. 192.168.0.0/24
TIMEOUT = 1

OUTPUT_FILE = "fanvil_ips.txt"

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ",
        "Accept": "text/html,application/xhtml+xml,application/xml;"
                  "q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

# ---------- FANVIL DETECTION ----------
def is_ip_phone(ip):
    """Check if the device is a Fanvil IP phone by testing the default_user_config endpoint."""
    url = f"http://{ip}/default_user_config.txt"
    try:
        r = requests.get(url, timeout=TIMEOUT, headers=HEADERS)
        # Fanvil devices respond with 401 Unauthorized when accessed without login
        if r.status_code == 401:
            return True
    except requests.RequestException:
        return False
    return False

# ---------- MAIN ----------
def main():
    # clear file at start
    open(OUTPUT_FILE, "w").close()

    for ip in ip_network(IP_RANGE, strict=False).hosts():
        ip = str(ip)
        print(f"[+] Scanning {ip} ...")
        if is_ip_phone(ip):
            print(f"    [✓] Found Fanvil IP Phone at {ip}")
            with open(OUTPUT_FILE, "a") as f:
                f.write(ip + "\n")

    print(f"\n[✓] Scan complete. Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
