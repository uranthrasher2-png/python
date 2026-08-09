text = input('')

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar(question, shift):
    result = ''
    for char in question:
        if char in alphabet_lower:
            idx = alphabet_lower.index(char)
            new_idx = (idx + shift) % len(alphabet_lower)
            result += alphabet_lower[new_idx]
        elif char in alphabet_upper:
            idx = alphabet_upper.index(char)
            new_idx = (idx + shift) % len(alphabet_upper)
            result += alphabet_upper[new_idx]
        else:
            result += char
    return result


encrypted_text=''
current_word=''
    
    
for char in text:
    if char.isalpha():
        current_word+=char
    else: 
        if current_word:
            encrypted_text+=caesar(current_word, len(current_word))
            current_word = ''
        encrypted_text += char
        
if current_word:
    encrypted_text += caesar(current_word, len(current_word))      

print(encrypted_text)