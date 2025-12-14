MEMORY = {
    14: 2, 
    15: 3,
    13: 0
}

ACC = 0

PC = 0

OPCODES = {
    '0001': 'LOAD',
    '0010': 'ADD',
    '0011': 'STORE',
    '1111': 'HALT'
}

PROGRAM_MACHINE_CODE = [
    "000101110",  
    "001001111", 
    "001101101",  
    "111100000"  
]

def execute_instruction(instruction_9bit):
    global ACC, PC, MEMORY
    
    opcode_bin = instruction_9bit[:4]    
    address_bin = instruction_9bit[4:]  
    
    
    operation = OPCODES.get(opcode_bin, "UNKNOWN")
    address = int(address_bin, 2)  
    
    print(f"\nPC: {PC} | Instruksi: {instruction_9bit} (Op: {operation}, Alamat: {address})")
    
   
    if operation == 'LOAD':
        value = MEMORY.get(address, 0)
        ACC = value
        print(f"  -> Aksi: Memuat nilai {value} dari [Memori {address}] ke ACC.")
        
    elif operation == 'ADD':
        value_to_add = MEMORY.get(address, 0)
        ACC += value_to_add
        print(f"  -> Aksi: Menambahkan {value_to_add} dari [Memori {address}] ke ACC. (ACC baru: {ACC})")
        
    elif operation == 'STORE':
        MEMORY[address] = ACC
        print(f"  -> Aksi: Menyimpan nilai {ACC} dari ACC ke [Memori {address}].")
        
    elif operation == 'HALT':
        print("\n*** HALT: Program selesai dieksekusi. ***")
        return True 
        
    else:
        print(f"  -> ERROR: Opcode tidak dikenal: {opcode_bin}")
    
    PC += 1
    return False 

print("--- SIMULASI EKSEKUSI PROGRAM ASSEMBLY SEDERHANA (9-bit) ---")
print(f"Status Awal: ACC={ACC}, Memori 14={MEMORY[14]}, Memori 15={MEMORY[15]}, Memori 13={MEMORY[13]}")
print("----------------------------------------------------------")

halted = False
while not halted and PC < len(PROGRAM_MACHINE_CODE):
    current_instruction = PROGRAM_MACHINE_CODE[PC]
    halted = execute_instruction(current_instruction)

print("\n----------------------------------------------------------")
print(f"Status Akhir: ACC={ACC}")
print(f"Hasil Akhir di Memori 13: {MEMORY[13]}")