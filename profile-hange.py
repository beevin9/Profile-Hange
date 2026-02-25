import requests
import time
import sys
import os

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system("clear")
    print("\033[1;32m")
    slow_print("██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗")
    slow_print("██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝")
    slow_print("██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗  ")
    slow_print("██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝  ")
    slow_print("██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████╗")
    slow_print("╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝")
    print("\033[0m")
    slow_print(">> Authenticated Upload Testing Tool")
    slow_print(">> Session Based Request Automation\n")
    time.sleep(1)

def main():
    banner()

    url = input("Target URL: ")
    phpsessid = input("PHPSESSID: ")
    file_path = input("File Path: ")

    if not os.path.exists(file_path):
        print("\n[!] File not found.")
        return

    headers = {
        "Cookie": f"PHPSESSID={phpsessid}"
    }

    files = {
        "profile_pic": (file_path, open(file_path, "rb"), "image/jpeg"),
    }

    data = {
        "upload": "Upload"
    }

    slow_print("\n[+] Sending Request...\n", 0.02)

    try:
        response = requests.post(url, headers=headers, files=files, data=data)
        print("\nStatus Code:", response.status_code)
        print("\n--- Server Response Preview ---\n")
        print(response.text[:1000])

    except Exception as e:
        print("\n[!] Error:", e)

if __name__ == "__main__":
    main()
