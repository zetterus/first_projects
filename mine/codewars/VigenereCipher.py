class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.shift = tuple(alphabet.find(c) for c in key)

    def encode(self, text):
        result = ""
        index = 0
        for char in text:
            if char in self.alphabet:
                if index > len(self.shift) - 1:
                    index = index - len(self.shift)
                char_position = self.alphabet.find(char)
                new_char_position = char_position + self.shift[index]
                if new_char_position > len(self.alphabet) - 1:
                    new_char_position -= len(self.alphabet)
                result += self.alphabet[new_char_position]
                index += 1
            else:
                index += 1
                result += char
        return result

    def decode(self, text):
        result = ""
        index = 0
        for char in text:
            if char in self.alphabet:
                if index > len(self.shift) - 1:
                    index = index - len(self.shift)
                char_position = self.alphabet.find(char)
                new_char_position = char_position - self.shift[index]
                if new_char_position < 0:
                    new_char_position += len(self.alphabet)
                result += self.alphabet[new_char_position]
                index += 1
            else:
                index += 1
                result += char
        return result


# abc = "アィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴ"
# key = "カタカナ"

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"

c = VigenereCipher(key, abc)

print(c.encode("codewars"))
print(c.decode('rovwsoiv'))

