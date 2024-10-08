import numpy as np
import nashpy as nash

def get_input(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

def get_game_data():
    print("Welcome to the Zero-Sum Game Theory Nash Equilibrium Calculator!")
    
    # Step 1: Basic Information
    character1 = input("Enter name for Character 1: ")
    character2 = input("Enter name for Character 2: ")
    actions1 = get_input(f"Enter number of actions for {character1}: ", int)
    actions2 = get_input(f"Enter number of actions for {character2}: ", int)

    # Step 2: Action Names
    print(f"\nEnter action names for {character1}:")
    action_names1 = [input(f"Action {i+1}: ") for i in range(actions1)]
    
    print(f"\nEnter action names for {character2}:")
    action_names2 = [input(f"Action {i+1}: ") for i in range(actions2)]

    # Step 3: Reward Matrix
    print(f"\nEnter the reward matrix for {character1}:")
    matrix = np.zeros((actions1, actions2), dtype=float)
    for i in range(actions1):
        for j in range(actions2):
            matrix[i, j] = get_input(f"Reward for {character1}'s {action_names1[i]} vs {character2}'s {action_names2[j]}: ", float)

    return {
        'character1': character1,
        'character2': character2,
        'action_names1': action_names1,
        'action_names2': action_names2,
        'matrix': matrix
    }

def main():
    game_data = get_game_data()
    
    print("\nCollected Game Data:")
    print(f"Character 1: {game_data['character1']}")
    print(f"Character 2: {game_data['character2']}")
    print(f"{game_data['character1']}'s actions: {game_data['action_names1']}")
    print(f"{game_data['character2']}'s actions: {game_data['action_names2']}")
    print(f"\nReward Matrix for {game_data['character1']}:")
    print(game_data['matrix'])
    print(f"\nReward Matrix for {game_data['character2']} (automatically calculated as the opposite):")
    print(-game_data['matrix'])

    # Create the zero-sum game using nashpy
    game = nash.Game(game_data['matrix'])

    # Calculate Nash Equilibria
    equilibria = list(game.support_enumeration())

    # Print Nash Equilibrium results
    print("\nNash Equilibria:")
    if equilibria:
        for i, eq in enumerate(equilibria, 1):
            print(f"\nEquilibrium {i}:")
            print(f"{game_data['character1']}'s strategy:")
            for prob, action in zip(eq[0], game_data['action_names1']):
                print(f"  {action}: {prob:.4f}")
            print(f"{game_data['character2']}'s strategy:")
            for prob, action in zip(eq[1], game_data['action_names2']):
                print(f"  {action}: {prob:.4f}")
        
        # Calculate the value of the game
        value = eq[0] @ game_data['matrix'] @ eq[1]
        print(f"\nValue of the game: {value:.4f}")
    else:
        print("No Nash Equilibrium found.")

if __name__ == "__main__":
    main()
