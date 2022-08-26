# Caesar Cipher
from re import A
from CC_logo import logo1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo1)


#def encrypt(p_text,shift_amt):   ->>>>> Code To Encrypt Text
#    cipher_text = ""
#    for i in p_text:
#        position = alphabet.index(i)
#        new_p = position + shift_amt
#        new_letter = alphabet[new_p]
#        cipher_text += new_letter
#    print(f"The encoded text is --> {cipher_text}")

#def decrypt(p_text1,shift_amt1):   ->>>>> Code To Decrypt Text
#    decipher_text = ""
#    for i in p_text1:
#        position = alphabet.index(i)
#        new_p = position - shift_amt1
#        new_letter = alphabet[new_p]
#        decipher_text += new_letter
#    print(f"The decoded text is --> {decipher_text}")
    
def caesar(start_text, shift_amt,cipher_direction):   # ->>>> Combining Above Two Methods
    end_text=""
    if cipher_direction =="decode":
            shift_amt*= -1
    for char in start_text:
        if char in alphabet:
            position= alphabet.index(char)
            new_p=position+shift_amt
            end_text+=alphabet[new_p]
        else :
            end_text += char

    print(" \(^-^)/ "+f"Your {cipher_direction}d text is {end_text}\n")    
should_continue =True
while should_continue:
    user_input=input("Type 'encode' to encrypt or 'decode' to decrypt : \n")
    #if user_input== 'encode':
    #    text=input("Type your message: \n").lower()
    #    shift=int(input("Type the shift number: \n"))
    #    encrypt(p_text=text,shift_amt=shift)
    #elif user_input =='decode':
    #    text1=input("Type message you want to decode: \n").lower()
    #    shift1=int(input("Type the shift number: \n"))
    #    decrypt(p_text1=text1,shift_amt1=shift1)
    text=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    shift=shift%26 
    caesar(start_text=text, shift_amt=shift,cipher_direction= user_input)
    result= input("Type 'yes' if you want to go again. Othewise type 'no.\n")
    if result=='no':
        should_continue=False
