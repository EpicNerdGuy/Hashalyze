import base64
import binascii

hash_filter = {
    32: ["MD5", "NTLM"],
    40: ["SHA1"],
    64: ["SHA256"],
    96: ["SHA384"],
    128: ["SHA512"],
}

# Hex Check
def is_hex(hashx):
    hashx = hashx.strip()
    hex_digits = "0123456789abcdefABCDEF"
    
    # Check every character
    for char in hashx:
        if char not in hex_digits:
            return {
                "is_hex": False,
                "reason": f"Invalid character '{char}' found",
                "length": len(hashx),
                "is_even": len(hashx) % 2 == 0
            }
    
    # If we get here, it's valid hex
    return {
        "is_hex": True,
        "reason": "Valid hex string",
        "length": len(hashx),
        "is_even": len(hashx) % 2 == 0
    }


# Base64 Check
def is_base64(hashx):
    try:
        base64.b64decode(hashx.encode('utf-8'), validate=True)
        return True
    except (binascii.Error, UnicodeDecodeError):
        return False

# Hash Type Check
def check_hash(length, hashx, return_types=False):
    types = hash_filter.get(length)
    if return_types:
        return types if types else []
    if types:
        print(f"HOOORAY {hashx} COULD BE {types}")
    else:
        print("NOT A COMMON HASH")


# Main Logic
def main():
    print("ENTER YOUR HASH:")
    hash_val = input()
    hashx = hash_val.strip().lower()
    hex_result = is_hex(hashx)
    length=len(hashx)
    if hex_result["is_hex"]:
            check_hash(length, hashx)
    elif is_base64(hashx):
        print(f"{hashx} is base64")
    else:
        print(hex_result["reason"])

if __name__ == "__main__":
    main()
