from collections import Counter
import string

FREQUENCIES = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022, 
    'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002, 'K': 0.008, 'L': 0.040, 
    'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 'Q': 0.001, 'R': 0.060, 
    'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.010, 'W': 0.023, 'X': 0.001, 
    'Y': 0.020, 'Z': 0.001
}

def vigenere_decrypt(ciphertext, key_length):
    def shift(c, d):
        return chr(((ord(c) - ord('A') - d) % 26) + ord('A'))

    def frequency_analysis(block):
        chi_squared_values = []
        for d in range(26):
            chi_squared_value = sum(frequency * FREQUENCIES[shift(char, d)] 
                                    for char, frequency in Counter(block).items())
            chi_squared_values.append(chi_squared_value)
        return chi_squared_values.index(max(chi_squared_values))

    blocks = [ciphertext[i::key_length] for i in range(key_length)]
    key = ""

    for block in blocks:
        best_shift = frequency_analysis(block)
        key += string.ascii_uppercase[best_shift]
        
    return key


