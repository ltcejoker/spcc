from collections import defaultdict

productions = {
    'S': ['AB'],
    'A': ['aA', 'ε'],
    'B': ['bB', 'ε']
}

non_terminals = list(productions.keys())
terminals = {'a', 'b'}
first = {
    'S': {'a', 'b', 'ε'},
    'A': {'a', 'ε'},
    'B': {'b', 'ε'}
}

follow = defaultdict(set)
follow['S'].add('$')  # Start symbol gets '$'

def compute_follow():
    changed = True
    while changed:
        changed = False
        for head in productions:
            for body in productions[head]:
                for i, B in enumerate(body):
                    if B in non_terminals:
                        trailer = set()
                        if i + 1 < len(body):
                            for symbol in body[i+1:]:
                                if symbol in terminals:
                                    trailer = {symbol}
                                    break
                                elif symbol in non_terminals:
                                    trailer |= (first[symbol] - {'ε'})
                                    if 'ε' in first[symbol]:
                                        continue
                                    else:
                                        break
                                else:
                                    break
                            else:
                                trailer |= follow[head]
                        else:
                            trailer |= follow[head]

                        if not trailer.issubset(follow[B]):
                            follow[B] |= trailer
                            changed = True

compute_follow()

# Display results
for nt in non_terminals:
    print(f"FOLLOW({nt}) = {follow[nt]}")
