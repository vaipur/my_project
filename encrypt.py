import cv2
import os


img = cv2.imread("IMG-20240818-WA0235.jpg")

if img is None:
    print("Error: Image not found!")
    exit()


msg = input("Enter secret message: ")
password = input("Enter password: ")


with open("key.txt", "w") as f:
    f.write(password + "\n")  
    f.write(str(len(msg)) + "\n")  


m, n = 0, 0 

for char in msg:
    value = ord(char)  
    img[n, m, 0] = value
    
    m += 1
    if m >= img.shape[1]:
        m = 0
        n += 1


cv2.imwrite("Encryptedmsg.png", img)  
print("Message encrypted successfully! Image saved as 'Encryptedmsg.png'.")

os.system("start Encryptedmsg.png")  