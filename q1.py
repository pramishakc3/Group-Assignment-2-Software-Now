#Q1 Software Now
def encrypt(raw, n, m):
    """Encrypt the input text using values n and m."""
    encrypted = ''
    for c in raw:
        # If the character is a lowercase letter between 'a' and 'm'
        if 'a' <= c <= 'm':
            # Shift it forward using a formula based on n and m, wrapping within the 13-letter half-range
            encrypted += chr((ord(c) - ord('a') + (n * m)) % 13 + ord('a'))
        # If it's a lowercase letter between 'n' and 'z'
        elif 'n' <= c <= 'z':
            # Shift it backward a bit differently, again staying in the 'n' to 'z' half
            encrypted += chr((ord(c) - ord('n') - (n + m)) % 13 + ord('n'))
        # Uppercase letters from 'A' to 'M'
        elif 'A' <= c <= 'M':
            # Shift backward using just 'n'
            encrypted += chr((ord(c) - ord('A') - n) % 13 + ord('A'))
        # Uppercase letters from 'N' to 'Z'
        elif 'N' <= c <= 'Z':
            # Shift forward using square of m (just to make it spicy)
            encrypted += chr((ord(c) - ord('N') + (m ** 2)) % 13 + ord('N'))
        else:
            # For any non-alphabet character (space, symbols, numbers), leave it as is
            encrypted += c
    return encrypted


def decrypt(encrypted, n, m):
    """Decrypt text back using the same n and m values."""
    decrypted = ''
    for c in encrypted:
        # Basically doing the reverse of what we did in encrypt
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

        # Throw an error if any of them are negative
        if n < 0 or m < 0:
            raise ValueError("n and m must be non-negative integers.")

        # Read the original text from a file named 'raw_text.txt'
        with open('raw_text.txt', 'r', encoding='utf-8') as f:
            raw_text = f.read()

        # Encrypt the text using our funky rules
        encrypted_text = encrypt(raw_text, n, m)

        # Save the encrypted result in a new file
        with open('encrypted_text.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

        # Now decrypt the encrypted text back to original
        decrypted_text = decrypt(encrypted_text, n, m)

        # Check if decryption was actually correct
        is_correct = verify(raw_text, decrypted_text)
        print("Decryption Correct:", is_correct)

        # Print the decrypted text to see what it looks like
        print("\nDecrypted Text:")
        print(decrypted_text)

    except ValueError as ve:
        print("Invalid input:", ve)
    except FileNotFoundError:
        # This happens if the input file doesn't exist
        print("Error: 'raw_text.txt' not found.")
    except Exception as e:
        # Catch anything else weird that might happen
        print("An unexpected error occurred:", e)


# Start the program
if __name__ == '__main__':
    main()
