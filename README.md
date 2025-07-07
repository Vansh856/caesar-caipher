# caesar-caipher
A beginner-friendly Caesar Cipher tool in Python for encrypting and decrypting text using custom alphabet shifting.
🔧 Features:
- Encrypts user input by shifting letters through a custom alphabet (includes space).
- Decrypts text using the same shift logic.
- Clear logic flow with helpful comments.
- User-friendly input prompts.
- No external libraries required — just pure Python!
   How It Works:
Each character in the message is converted to its index from a defined alphabet list. That index is then shifted (forward for encryption, backward for decryption) and mapped back to a character. Modular arithmetic ensures wrapping around the alphabet list for clean circular shifts.
   Ideal for:
- Beginners exploring cryptography concepts.
- Python learners experimenting with string manipulation and modular logic.
- Anyone curious about how classical encryption works!
