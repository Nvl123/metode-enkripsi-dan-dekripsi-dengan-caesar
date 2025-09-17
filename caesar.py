alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    '"', "'", '<', '>', ',', '.', '?', '/', '\\', '|', '`', '~'
]

def caesar(text, nilai_geser):
    new_text = ''
    text.lower()
    panjang_text = len(text)
    
    for i in range(panjang_text) :
        if text[i] != ' ' and text[i] not in special_chars:    
            for j in range(len(alphabet)):
                if alphabet[j] == text[i]:
                    nilai = j + nilai_geser

                    if nilai > len(alphabet) - 1 :
                        nilai = nilai % len(alphabet)
                        
                        new_text += (alphabet[nilai])

                    else :
                        new_text +=(alphabet[nilai])
        else:
            new_text += text[i]
                
    return new_text


plaintext= str(input("Masuukan teks anda :"))
enkripsi = caesar(plaintext, 12)
deskripsi = caesar(enkripsi, -12)


print(f"""

ini adalah plain text nya  "{plaintext}" 
dan setelah di enkripsi menjadi text chiper seperti ini "{enkripsi}"
kemudian setelah di deskripsi menjadi seperti ini "{deskripsi}"
""")




