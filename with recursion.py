def recursivecaesarcipher(text, shift):
    if text == "":
        return ""
    
    char = text[0]
    if char.islower():
        shifted = ord(char) + shift

        if shifted > ord('z'):
            shifted -= 26

        elif shifted < ord('a'):
            shifted += 26

        result = chr(shifted)
    elif char.isupper():
        shifted = ord(char) + shift

        if shifted > ord('Z'):
            shifted -= 26

        elif shifted < ord('A'):
            shifted += 26

        result = chr(shifted)
        
    else:
        result = char

    return result + recursivecaesarcipher(text[1:], shift)
    


print(recursivecaesarcipher("abc", -3))
