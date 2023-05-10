#modules
import random
def encrypt_file(encryption):
    '''
    sends encrypted phrase to a new file

    args:
        encryption:str = newly made encrypted message
    '''
    with open ("encrypted.txt", 'w') as file:
        file.write(encryption)
    file.close()
def caesar_cipher(phrase,shift):
    '''
    Encrypts a phrase with a randomized shift of lettering

    args:
        phrase:str = the message that will be encrypted
        shift:int = random shift for each letter
    return:
        :str = encrytped message
    '''
    result = ''
    for char in phrase:
        if char.isalpha():
            start=ord('A') if char.isupper() else ord('a')
            new_pos= (ord(char) - start +shift)% 26
            char = chr(start+new_pos)
        result += char
    return result
def main():
    phrase = "The quick brown fox jumps over the lazy dog"
    shift= random.randint(1,26)
    encryption=caesar_cipher(phrase,shift)
    encrypt_file(encryption)

if __name__=="__main__":
    main()