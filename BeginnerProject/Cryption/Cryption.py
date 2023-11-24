alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Encryption
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(text,shift,direction):  
    caesar_text = ""
    list_length = len(alphabet) - 1
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt
    for i in text:
        x = alphabet.index(i)   #get letter position

        if direction == "encode":
            encode = int(x+shift)   
            #return to the start if overflow
            if encode > list_length:           #check if encode out of range | MaybeBug: len(alphabet) count for      nht. But alphabet[int] count from 0
                encode = encode % len(alphabet)  #Reverse to 0 if encode exceed 26 -> len(alphabet) 
            caesar_text += alphabet[encode]  

        if direction == "decode":
            encode = int(x-shift)
            if encode < 0:
                encode = encode % len(alphabet)  # -101%25 -> 1 (not -1)  (calc overflow num -> simplified it using %. Loop through list n times and give remainder)   
            caesar_text += alphabet[encode]

    # print(f" encode {encode}")
    # print(f" % {encode % len(alphabet)}")
    
    print(f"the code is {caesar_text}")

#TODO-final: repeat the loop by asking to continue or not 

while True:
    wished = input("Press 'Y' to continue | Press 'N' to quit: ").lower()
    match wished:
        case "y":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            caesar(text,shift,direction)
        case "n":
            break

    