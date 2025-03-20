def recursivecaesarcipher(text, shift):
    if text == "":
        return ""
    
    plaintext = ""
  
    for i, j in enumerate(text): #index, char
        if j == " ":
            continue
        plaintext = plaintext + chr(ord(j)+shift)
    return plaintext
