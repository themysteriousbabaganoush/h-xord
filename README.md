# h-xord

sha256
f579b208a55f312d9a8eb0f94884bbe56bcc89c34728e131774ef459b0465a51  h-xord
3db5eae9ef2e8595a9734f52c6d97d1788cafc27f0052168cab12ef5b8da1c2a  h-xord.py


**An Intelligent XOR Cipher Decryption Tool**  
_By Chairman Hellsing & Mun_

---

### 🧠 Overview

**h-xord** is a Python-based XOR decryption utility designed to reverse engineer ciphertexts encrypted with repeating-key XOR.  
It leverages partial knowledge of the plaintext—either the **beginning**, **end**, or both—to intelligently reconstruct the XOR key and recover the full original message.

Ideal for:
- CTFs
- Malware analysis
- Forensic recovery
- Quick XOR decoding jobs

---

### 🔑 Features

- 📥 Accepts ciphertext in **hexadecimal** format
- 🧩 Uses known **plaintext fragments** at start and/or end
- 🔁 Handles **repeating XOR keys** of any length
- 🔍 Uses **brute-force+backtracking** on missing key bytes using printable ASCII
- ⚠️ Detects **key byte conflicts** and warns user

---

### 🚀 How to Use

#### 1. **Run the Program**
```bash
python h_xord.py
```

#### 2. **Provide Inputs When Prompted**
```text
Enter ciphertext (hex): 672275011c020b54141876124c3b18475e5b110f72044a490d5f26411239411e
Enter known starting plaintext (leave empty if none): Hello,
Enter known ending plaintext (leave empty if none): Mun.
Enter the key length: 5
```

#### 3. **Output**
```text
Key found: alpha
Decrypted plaintext: Hello, Chairman Mun.
```

If a valid key cannot be determined based on your input, you'll receive:
```text
Failed to find key with given info.
```

---

### ⚙️ Requirements

- Python 3.6+
- No external dependencies

---

### 📜 Notes

- Key must repeat cyclically throughout the ciphertext.
- The more known plaintext you provide (start and/or end), the better the accuracy and speed.
- Unknown key bytes are guessed from printable ASCII (`0x20` to `0x7E`).
- Conflicts in guessed key bytes are warned but not automatically resolved.

---

### ✨ Example Use Case

Decrypt a CTF flag or malware string when you only know:

- It starts with `"FLAG{"`  
- It ends with `"}"`

You can input these hints and let **h-xord** fill in the blanks.

---

### 👑 Credits

Designed by **Chairman Hellsing & Mun**  
Built for security researchers, reverse engineers, and codebreakers.

> "Even the simplest cipher has a key—and the wise can always find it."

---
