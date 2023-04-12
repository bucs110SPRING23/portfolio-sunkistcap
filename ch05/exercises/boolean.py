def remove_vowels(string):
    """
    Function removes vowels from the provided string
    args: mystring(str)
    return: result (str)
    """
    vowels="aeiou"
    vowels += vowels.upper()
    result=""
    for ch in string:
        if ch not in vowels:
            result += ch
    return result
def main():
    mystring= "Hello World"
    mystring=remove_vowels(mystring)
    print(mystring)

main()