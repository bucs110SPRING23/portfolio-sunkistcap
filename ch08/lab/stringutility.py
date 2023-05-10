class StringUtility:
    def __init__(self, string):
        self.string = (string)
    def __str__(self):
        return self.string
    def vowels(self):
        return str(len([char for char in self.string if char.lower() in "aeiou"])) if len ([char for char in self.string if char.lower() in "aeiou"]) < 5 else 'many'
    def bothEnds(self):
        return self.string[:2]+ self.string[-2:] if len(self.string) > 2 else ''
    def fixStart(self):
        return self.string if len(self.string) <= 1 else self.string[0] + self.string[1:].replace(self.string[0], '*')
    def asciiSum(self):
        return sum(ord(char) for char in self.string)
    def cipher(self):
        return '' .join(chr((ord(char)+ len(self.string) - (65 if char.isupper() else 97)) % 26 + (65 if char.isupper() else 97)) if char.isalpha() else char for char in self.string)