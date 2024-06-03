# # string = input("Enter a string: ")

# # vowels = "aeiouAEIOU"
# # consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# string_without_vowels = ''.join(char for char in string if char not in vowels)
# string_without_consonants = ''.join(char for char in string if char not in consonants)

# print("String without vowels:", string_without_vowels)
# print("String without consonants:", string_without_consonants)





def remove_vowels_and_punctuation(text):
    vowels = "aeiouAEIOU"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    result = ""
    for char in text:
        if char not in vowels and char not in punctuation:
            result += char
    return result
text = (input("Enter string and punctuation:"))
result = remove_vowels_and_punctuation(text)

print("Original Text:", text)
print("Text without vowels and punctuation:", result)





# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# unctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# string_without_vowels = ''.join(char for char in string if char not in vowels)
#print("String without vowels:", string_without_vowels)