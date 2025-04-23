def pass1_assembler(source_code):
    opcode_table = {
        'LDA': 3, 'STA': 3, 'LDX': 3, 'ADD': 3, 'SUB': 3, 'MUL': 3, 'DIV': 3,
        'COMP': 3, 'J': 3, 'JEQ': 3, 'JGT': 3, 'JLT': 3
    }

    symbol_table = {}
    intermediate = []

    locctr = 0
    start_address = 0

    lines = source_code.strip().split('\n')

    for idx, line in enumerate(lines):
        if line.startswith('.'):  # skip comments
            continue

        parts = line.strip().split()
        label, opcode, operand = '', '', ''

        if len(parts) == 3:
            label, opcode, operand = parts
        elif len(parts) == 2:
            opcode, operand = parts
        elif len(parts) == 1:
            opcode = parts[0]

        if opcode == 'START':
            start_address = int(operand, 16)
            locctr = start_address
            intermediate.append((locctr, label, opcode, operand))
            continue

        if label:
            if label in symbol_table:
                raise ValueError(f"Duplicate symbol: {label}")
            symbol_table[label] = locctr

        intermediate.append((locctr, label, opcode, operand))

        if opcode in opcode_table:
            locctr += opcode_table[opcode]
        elif opcode == 'WORD':
            locctr += 3
        elif opcode == 'RESW':
            locctr += 3 * int(operand)
        elif opcode == 'RESB':
            locctr += int(operand)
        elif opcode == 'BYTE':
            if operand.startswith("C'"):
                locctr += len(operand) - 3  # subtract C'' wrapper
            elif operand.startswith("X'"):
                locctr += (len(operand) - 3) // 2
        elif opcode == 'END':
            break
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

    return symbol_table, intermediate


source = """
START 1000
FIRST   LDA     ALPHA
        ADD     ONE
        STA     BETA
ALPHA   RESW    1
ONE     WORD    1
BETA    RESW    1
        END     FIRST
"""

symtab, inter = pass1_assembler(source)

print("Symbol Table:")
for k, v in symtab.items():
    print(f"{k}: {hex(v)}")

print("\nIntermediate File:")
for row in inter:
    print(row)
