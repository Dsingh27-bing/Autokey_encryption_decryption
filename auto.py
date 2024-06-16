import sys

def key_generation(key,text):
    global key_final
    key_final = key + text[0:(len(text)-len(key))]
    return key_final

def encryption_autokey(msg): 
    global key_final
    ciphertext = ""
    for i in range(len(msg)):
        key1 = (ord(key_final[i]))-97
        plaintext = (ord(msg[i]))-97
        ciphertext += chr((plaintext + key1)%26+97)
    return ciphertext

def decryption_autokey(msg, key): 
    plaintext = ""
    for i in range(len(msg)):
        key1 = (ord(key[i]))-97
        ciphertext = (ord(msg[i]))-97
        temp = chr((ciphertext - key1)%26+97)
        plaintext += temp
        key += temp
    return plaintext


n = len(sys.argv)
#if (".txt" not in sys.argv[1]):
    #sys.argv[1] += ".txt"
with open(sys.argv[1], 'r') as file:
    plntxt = file.read().rstrip()
key = sys.argv[3]
if (sys.argv[4])== "0":
    opt = decryption_autokey(plntxt, key)
else:
    key_generation(key,plntxt)
    opt= encryption_autokey(plntxt) 

#if(".txt" not in sys.argv[2]):
    #sys.argv[2] += ".txt"
outputf = open(sys.argv[2], "w")  # write mode
outputf.write(opt)
outputf.close()
