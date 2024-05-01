def backward_chaining(rules, goal, known_facts):
    if goal in known_facts:
        return True

    for rule in rules:
        if rule[1] == goal:
            if all(backward_chaining(rules, condition, known_facts) for condition in rule[0]):
                return True

    return False

rules = [
    (['penguin', 'can_fly'], 'bird'),
    (['bird', 'lays_eggs'], 'canary'),
    (['bird', 'can_fly'], 'sparrow')
]

known_facts = ['penguin', 'can_fly']
goal = 'bird'

result = backward_chaining(rules, goal, known_facts)
print("Can the goal be inferred?", result)
