import cv2


img = cv2.imread("Encryptedmsg.png")  

if img is None:
    print("Error: Encrypted image not found!")
    exit()
try:
    with open("key.txt", "r") as f:
        saved_password = f.readline().strip()  
        msg_length = int(f.readline().strip())  
except FileNotFoundError:
    print("Error: key.txt not found! Run encrypt.py first.")
    exit()
except ValueError:
    print("Error: Invalid message length in key.txt!")
    exit()


pas = input("Enter passcode for decryption: ")


if pas != saved_password:
    print("Invalid password! Decryption failed.")
    exit()


message = ""
ascii_values = []  
m, n = 0, 0  

for i in range(msg_length):
    if n >= img.shape[0] or m >= img.shape[1]:  
        print(f"Error: Image too small or corruption detected at pixel ({n}, {m})!")
        break

    char_value = img[n, m, 0]  
    message += chr(char_value)  
    ascii_values.append(char_value)  

    
    m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1


print(f"Extracted ASCII values: {ascii_values}")


print("Decrypted message:", message)