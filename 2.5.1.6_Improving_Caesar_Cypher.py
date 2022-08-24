# Caesar cipher.
#text = input("Enter your message: ")
#cipher = ''
#for char in text:
 #   if not char.isalpha():
 #       continue
 #   char = char.upper()
#    code = ord(char) + 1
#    if code > ord('Z'):
#        code = ord('A')
#    cipher += chr(code)

#print(cipher)

def handle_text(string:str) -> str:
    ''' returns stripped input string '''
    string = string.strip()
    return string
    
def validate_shift(input_shift:str) -> int :
    '''validates input range'''
    shift = 0
    try:
        shift = int(input_shift)
    except ValueError:
        print("The range is not a valid value")
        return 
    if shift >= 1 and shift <= 25:
        return shift
    else:
        print("The number must be between 1 and 25, try again")
        return 
    
    
    
def caesar_cypher(text, shift):
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        code = ord(char) + shift
        if char.islower():
            if code > ord('z'):
                code = ord('a') + code - ord('z') - 1
        else:
            if code > ord('Z'):
                code = ord('A') + code - ord('Z') - 1
            
        cipher += chr(code)
    return cipher
    
    
if __name__ == '__main__':
    text = input("Give me the text you want to decrypt: " )
    text = handle_text(text)
    shift = ''
    
    while not isinstance(shift,int):
        shift = input("How many characters do you want to shift? ( Must be an integer between 1 and 25, inclusively )")
        shift = validate_shift(shift)
    print(caesar_cypher(text,shift))
