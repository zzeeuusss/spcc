def minimax(low, high, depth):
    if depth == 0:
        return (low + high) // 2
    
    best_guess = -1
    best_score = -float('inf')
    for guess in range(low, high + 1):
        score = minimax_score(low, high, guess, False, depth - 1)
        if score > best_score:
            best_score = score
            best_guess = guess
    return best_guess

def minimax_score(low, high, guess, is_maximizing, depth):
    if low == high:
        return low
    
    if depth == 0:
        return (low + high) // 2
    
    if is_maximizing:
        return minimax(low, guess - 1, depth - 1)
    else:
        return minimax(guess + 1, high, depth - 1)

def play_guessing_game():
    low = 1
    high = 100
    depth = 5
    print("Guessing Game!")
    print("Think of a number between 1 and 100")
    
    while True:
        guess = minimax(low, high, depth)
        print(f"AI guesses: {guess}")
        response = input("Is it correct? (yes/no): ").lower()
        if response == "yes":
            print("AI wins!")
            break
        elif response == "no":
            response = input("Is it higher or lower? (higher/lower): ").lower()
            if response == "higher":
                low = guess + 1
            elif response == "lower":
                high = guess - 1
            else:
                print("Invalid response. Please enter 'higher' or 'lower'.")
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

play_guessing_game()
