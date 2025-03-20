def recursivecaesarcipher(text, shift):
    if text == "":
        return ""
    
    plaintext = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            shiftedchar = ord(char) + shift
            if shiftedchar > ord('z'):
                


            plaintext += shiftedchar

    return plaintext



print(recursivecaesarcipher("abc", 3))
