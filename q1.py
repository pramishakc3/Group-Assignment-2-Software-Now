# Q1 Software Now

import os

# Define the output directory as specified
output_dir = 'output_directory_q1'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def encrypt(raw, n, m):
    """Encrypt the input text using values n and m."""
    encrypted = ''
    for c in raw:
        if 'a' <= c <= 'm':
            encrypted += chr((ord(c) - ord('a') + (n * m)) % 13 + ord('a'))
        elif 'n' <= c <= 'z':
            encrypted += chr((ord(c) - ord('n') - (n + m)) % 13 + ord('n'))
        elif 'A' <= c <= 'M':
            encrypted += chr((ord(c) - ord('A') - n) % 13 + ord('A'))
        elif 'N' <= c <= 'Z':
            encrypted += chr((ord(c) - ord('N') + (m ** 2)) % 13 + ord('N'))
        else:
            encrypted += c
    return encrypted

def decrypt(encrypted, n, m):
    """Decrypt text back using the same n and m values."""
    decrypted = ''
    for c in encrypted:
        if 'a' <= c <= 'm':
            decrypted += chr((ord(c) - ord('a') - (n * m)) % 13 + ord('a'))
        elif 'n' <= c <= 'z':
            decrypted += chr((ord(c) - ord('n') + (n + m)) % 13 + ord('n'))
        elif 'A' <= c <= 'M':
            decrypted += chr((ord(c) - ord('A') + n) % 13 + ord('A'))
        elif 'N' <= c <= 'Z':
            decrypted += chr((ord(c) - ord('N') - (m ** 2)) % 13 + ord('N'))
        else:
            decrypted += c
    return decrypted

def verify(raw, decrypted):
    """Just checks if the decrypted text matches the original raw one."""
    return raw == decrypted

def main():
    try:
        # Ask the user for n and m values
        n = int(input('Enter integer n: '))
        m = int(input('Enter integer m: '))

        # Validate values
        if n < 0 or m < 0:
            raise ValueError("n and m must be non-negative integers.")

        # Read the original text
        with open('raw_text.txt', 'r', encoding='utf-8') as f:
            raw_text = f.read()

        # Encrypt the text
        encrypted_text = encrypt(raw_text, n, m)

        # Save encrypted text
        with open(f'{output_dir}/encrypted_text.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

        # Decrypt the text
        decrypted_text = decrypt(encrypted_text, n, m)

        # Save decrypted text
        with open(f'{output_dir}/decrypted_text.txt', 'w', encoding='utf-8') as f:
            f.write(decrypted_text)

        # Verify and print results
        is_correct = verify(raw_text, decrypted_text)
        print("Decryption Correct:", is_correct)

        print("\nDecrypted Text:")
        print(decrypted_text)

    except ValueError as ve:
        print("Invalid input:", ve)
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Start the program
if __name__ == '__main__':
    main()