from collections import defaultdict

productions = {
    'S': ['AB'],
    'A': ['aA', 'ε'],
    'B': ['bB', 'ε']
}

non_terminals = list(productions.keys())
terminals = {'a', 'b'}
first = defaultdict(set)

# Initialize FIRST sets for terminals
for terminal in terminals:
    first[terminal].add(terminal)

def compute_first():
    changed = True
    while changed:
        changed = False
        for head in productions:
            for body in productions[head]:
                i = 0
                while i < len(body):
                    symbol = body[i]
                    if symbol in terminals:  # Terminal symbols
                        if symbol not in first[head]:
                            first[head].add(symbol)
                            changed = True
                        break
                    else:  # Non-terminal symbols
                        temp = first[symbol] - {'ε'}
                        if temp - first[head]:
                            first[head] |= temp
                            changed = True
                        if 'ε' not in first[symbol]:
                            break
                    i += 1
                else:
                    # If the whole body is ε
                    if 'ε' not in first[head]:
                        first[head].add('ε')
                        changed = True

compute_first()

# Display results
for nt in non_terminals:
    print(f"FIRST({nt}) = {first[nt]}")
