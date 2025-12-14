memori = {}
ACC = 0

def LOAD(alamat):
    global ACC
    ACC = memori[alamat]

def OUT():
    print(chr(ACC), end='')

def HALT():
    print("\nProgram selesai")

text = "Teknik Informatika"
start_addr = 20

for i, char in enumerate(text):
    memori[start_addr + i] = ord(char)

for i in range(len(text)):
    LOAD(start_addr + i)
    OUT()

HALT()