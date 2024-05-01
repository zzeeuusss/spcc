class Predicate:
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __str__(self):
        return f"{self.name}/{self.arity}"

class Sentence:
    def __init__(self, predicate, arguments):
        self.predicate = predicate
        self.arguments = arguments

    def __str__(self):
        return f"{self.predicate.name}({', '.join(self.arguments)})"

class KnowledgeBase:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def query(self, query_sentence):
        for sentence in self.sentences:
            if str(sentence) == str(query_sentence):
                return True
        return False

# Example usage:
# Define predicates
likes = Predicate("Likes", 2)
rich = Predicate("Rich", 1)

# Define sentences
sentence1 = Sentence(likes, ["Alice", "Bob"])
sentence2 = Sentence(rich, ["Alice"])

# Create knowledge base
kb = KnowledgeBase()
kb.add_sentence(sentence1)
kb.add_sentence(sentence2)

# Query the knowledge base
query1 = Sentence(likes, ["Alice", "Bob"])
query2 = Sentence(likes, ["Bob", "Alice"])
query3 = Sentence(rich, ["Alice"])

print("Does Alice like Bob?", kb.query(query1))  # True
print("Does Bob like Alice?", kb.query(query2))  # False
print("Is Alice rich?", kb.query(query3))       # True
