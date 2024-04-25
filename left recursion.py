def separate_productions(productions, non_terminal):
    alpha_productions = []
    beta_productions = []
    for production in productions:
        if production.startswith(non_terminal):
            alpha_productions.append(production[len(non_terminal):])
        else:
            beta_productions.append(production)
        return alpha_productions, beta_productions
def remove_left_recursion(grammar):
    new_grammar = {}
    for non_terminal, productions in grammar.items():
        alpha_productions, beta_productions = separate_productions(productions, non_terminal)
        if alpha_productions:
            new_non_terminal = non_terminal + "'"
            new_grammar[new_non_terminal] = [alpha + new_non_terminal for alpha in
alpha_productions]
            new_grammar[non_terminal] = [beta + new_non_terminal for beta in beta_productions]
        else:
            new_grammar[non_terminal] = productions
    return new_grammar
def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(non_terminal, '->', ' | '.join(productions))
# Example usage:
grammar = {
'E': ['E+T', 'T'],
'T': ['T*F', 'F'],
'F': ['(E)', 'id']
}
print("Original Grammar:")
print_grammar(grammar)
new_grammar = remove_left_recursion(grammar)
print("\nGrammar after removing left recursion:")
print_grammar(new_grammar)
