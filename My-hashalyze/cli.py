from main import check_hash, is_hex, is_base64,check_bcrypt
import json
from pyfiglet import figlet_format
from colorama import Fore, Style, init
import argparse

init(autoreset=True)  # Auto-reset colors

def display_banner():
    print(Fore.CYAN + figlet_format("Hashalyze", font="slant"))

def print_colored_text(result):
    print(Fore.YELLOW + f"[#] Input: {result['input']}")
    print(Fore.YELLOW + f"[#] Length: {result['length']}")
    print(Fore.YELLOW + f"[#] Format: {result['format']}")
    
    if result["valid"]:
        if result["possible_types"]:
            print(Fore.GREEN + f"[+] Possible Hash Type(s): {', '.join(result['possible_types'])}")
        else:
            print(Fore.RED + "[!] Hash length is valid, but type is uncommon.")
    else:
        print(Fore.RED + "[X] Invalid input: Not a valid hash format.")

def run_cli():
    parser = argparse.ArgumentParser(
        description="🔍 Hashalyze - Identify Hash Types Like a Pro 🧠",
        epilog="Example: hash-id --hash '$2b$12$abcdefghijklmnopqrstuvABCDEFGHIJKLMNO123456' --format json"
    )
    parser.add_argument('--hash', required=True, help="Hash string to identify (wrap bcrypt in quotes!)")
    parser.add_argument('--format', choices=["json", "text"], default="text", help="Output format")
    parser.add_argument('--version', action='version', version='Hashalyze v1.0.0')
    args = parser.parse_args()

    # ⚠️ Do NOT lowercase bcrypt hashes — they're case-sensitive
    raw_input = args.hash.strip()
    length = len(raw_input)

    # ✅ Optional debug
    print(Fore.BLUE + f"[DEBUG] Raw input: '{raw_input}' (Length: {length})")

    result = {
        "input": raw_input,
        "length": length,
        "format": None,
        "possible_types": [],
        "valid": False
    }

    # ✅ Check bcrypt first
    if check_bcrypt(raw_input):
        result["format"] = "bcrypt"
        result["valid"] = True
        result["possible_types"] = ["bcrypt"]

    # ✅ Check hex
    elif is_hex(raw_input)["is_hex"]:
        result["format"] = "hex"
        result["valid"] = True
        result["possible_types"] = check_hash(length, raw_input, return_types=True)

    # ✅ Check base64
    elif is_base64(raw_input):
        result["format"] = "base64"
        result["valid"] = True

    else:
        result["format"] = "unknown"

    display_banner()

    if args.format == "json":
        print(json.dumps(result, indent=4))
    else:
        print_colored_text(result)


if __name__ == "__main__":
    run_cli()
