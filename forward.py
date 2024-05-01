def forward_chaining(facts,known):
    fixed=set(known)
    inferred_facts=set()
    
    while fixed:
        fact=fixed.pop()

        if fact in inferred_facts:
            continue    
        
        inferred_facts.add(fact)
        
        for rule in facts:
            if set(rule[0]).issubset(inferred_facts):
                fixed.add(rule[1])
        
    return inferred_facts

rules = [
    (['penguin', 'can_fly'], 'bird'),
    (['bird', 'lays_eggs'], 'canary'),
    (['bird', 'can_fly'], 'sparrow')
]

known_facts = ['penguin', 'can_fly']

inferred_facts = forward_chaining(rules, known_facts)
print("Inferred Facts:", inferred_facts)
