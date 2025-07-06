def xor_bytes(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def guess_key(cipher_bytes, known_start, known_end, key_length):
    key = [None] * key_length
    n = len(cipher_bytes)

    # Fill key from known start plaintext
    for i in range(min(len(known_start), n)):
        key[i % key_length] = cipher_bytes[i] ^ known_start[i]

    # Fill key from known end plaintext
    for i in range(1, min(len(known_end), n) + 1):
        pos = n - i
        key_pos = pos % key_length
        val = cipher_bytes[pos] ^ known_end[-i]
        # If key slot is empty, fill it
        if key[key_pos] is None:
            key[key_pos] = val
        # If conflict, leave for later resolution (or check consistency)
        elif key[key_pos] != val:
            # For now, just warn about conflict
            print(f"Warning: Key byte conflict at position {key_pos}")

    # For unknown key bytes, guess by trying printable ASCII chars and check if plaintext looks good
    # Since you want fast method, let's just guess printable ASCII for unknown key bytes

    import string
    printable = list(range(32, 127))  # printable ASCII codes

    # For ambiguous key bytes, try all printable ASCII
    def backtrack(pos):
        if pos == key_length:
            # Full key assigned, try decrypt
            decrypted = xor_bytes(cipher_bytes, key)
            # Simple heuristic: decrypted must contain known_start and known_end if given
            if known_start and not decrypted.startswith(known_start):
                return None
            if known_end and not decrypted.endswith(known_end):
                return None
            return decrypted
        if key[pos] is not None:
            return backtrack(pos + 1)
        else:
            for guess in printable:
                key[pos] = guess
                result = backtrack(pos + 1)
                if result is not None:
                    return result
            key[pos] = None
            return None

    result = backtrack(0)
    if result:
        return key, result
    else:
        return key, None

def main():
    import binascii

    ciphertext_hex = input("Enter ciphertext (hex): ").strip()
    cipher_bytes = binascii.unhexlify(ciphertext_hex)

    known_start_str = input("Enter known starting plaintext (leave empty if none): ")
    known_start = known_start_str.encode() if known_start_str else b""

    known_end_str = input("Enter known ending plaintext (leave empty if none): ")
    known_end = known_end_str.encode() if known_end_str else b""

    key_length = int(input("Enter the key length: "))

    key, plaintext = guess_key(cipher_bytes, known_start, known_end, key_length)
    if plaintext:
        print(f"Key found: {bytes(key).decode('ascii')}")
        print(f"Decrypted plaintext: {plaintext.decode(errors='replace')}")
    else:
        print("Failed to find key with given info.")

if __name__ == "__main__":
    main()
