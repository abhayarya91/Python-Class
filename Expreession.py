import re
text = "The quick brown fox jumps over the lazy dog. The fox is quick and smart."

pattern = r'fox'
matches = re.findall(pattern, text)
print(f"Finding all occurrences of '{pattern}':")
print(matches)
print()

pattern = r'The'
match = re.match(pattern, text)
if match:
    print(f"Matching '{pattern}' at the beginning of the string:")
    print(match.group())
else:
    print(f"No match found for '{pattern}' at the beginning of the string.")
print()

pattern = r'quick'
search = re.search(pattern, text)
if search:
    print(f"Searching for '{pattern}' anywhere in the string:")
    print(search.group())
else:
    print(f"No match found for '{pattern}' in the string.")
print()

pattern = r'quick'
replacement = 'fast'
substituted_text = re.sub(pattern, replacement, text)
print(f"Substituting '{pattern}' with '{replacement}':")
print(substituted_text)
print()
