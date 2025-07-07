def encrypt():
    orignal_text=input("Enter the text to encrypt: ").lower()
    shift=int(input("Enter the shift value: "))
    alphaqbet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    #is list mae index store hoga har letter ka jo bhi allphabet mae hoga
    orignal_index=[alphaqbet.index(i) for i in orignal_text if i in alphaqbet]
    for i in range(len(orignal_index)):
        #ab ye pahle index ko shift value ke sath add karega aur phir uska mod len of alphaqbet se lega AUR FIR US INDEX KO ALPHAQBET MAE SE LEGA
        #is se hume encrypted letter milega
        print(alphaqbet[(orignal_index[i] + shift) % len(alphaqbet)], end="")
    
def decrypt():
    orignal_text=input("Enter the text to decrypt: ").lower()
    shift=int(input("Enter the shift value: "))
    alphaqbet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    orignal_index=[alphaqbet.index(i) for i in orignal_text if i in alphaqbet]
    for i in range(len(orignal_index)):
        print(alphaqbet[(orignal_index[i] - shift) % len(alphaqbet)], end="")
   
while True:
    
    command=input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    if command=="e":
        encrypt()
        break
    elif command=="d":
        decrypt()
        break
    else:
        print("Invalid command. Please enter 'e' to encrypt or 'd' to decrypt.")

         