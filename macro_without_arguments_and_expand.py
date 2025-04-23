def macro_processor(source_code):
    lines = source_code.strip().split('\n')
    macros = {}
    output = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        parts = line.split()

        if len(parts) >= 2 and parts[1] == 'MACRO':
            macro_name = parts[0]
            macro_body = []

            i += 1
            while not lines[i].strip().endswith('MEND'):
                macro_body.append(lines[i])
                i += 1
            macros[macro_name] = macro_body
        else:
            output.append(line)
        i += 1

    # Expand macros
    expanded = []
    for line in output:
        parts = line.split()
        if parts and parts[0] in macros:
            expanded.extend(macros[parts[0]])
        else:
            expanded.append(line)

    return expanded



source = """
INCR    MACRO
        LDA ALPHA
        ADD ONE
        STA ALPHA
        MEND
START 1000
INCR
END
"""

result = macro_processor(source)
print("\nExpanded Code:")
for line in result:
    print(line)
