# Smash-Nash
A user-friendly nash equilibrium solver for determining the best moves given reward matrices in two-player zero-sum games

This Python script calculates Nash Equilibria for two-player zero-sum games using the nashpy library.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.6 or later.
* You have a Windows/Linux/Mac machine.

## Installing Nash Equilibrium Calculator

To install the Nash Equilibrium Calculator, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/nash-equilibrium-calculator.git
   cd nash-equilibrium-calculator
   ```
   Or you can download the python file directly

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Using Nash Equilibrium Calculator

To use the Nash Equilibrium Calculator, follow these steps:

1. Run the script:
   ```
   python zero_sum_nash_equilibrium_calculator.py
   ```

2. Follow the prompts to input your game data:
   - Enter names for both players
   - Specify the number of actions for each player
   - Name each action for both players
   - Input the payoff matrix for Player 1 (Player 2's payoffs are automatically the negative of Player 1's in a zero-sum game)

3. The program will output:
   - The input game data
   - The calculated Nash Equilibria
   - The value of the game

To determine the value of a cell (player 1 action vs player 2 action), the best metric to use is the change in win probability for player 1. In practice, it is often easier to use a proxy that is heavily correlated with win percentage. In the case of SSBM, that would be change in stocks. If the Nash equilibrium can not be found, try using a smaller reward matrix by reducing or grouping (treating two actions as the same class of actions) actions from one or both players.

## Sample Input/Output

Here's an example of how to use the calculator:

```
Welcome to the Zero-Sum Game Theory Nash Equilibrium Calculator!
Enter name for Character 1: Alice
Enter name for Character 2: Bob
Enter number of actions for Alice: 3
Enter number of actions for Bob: 3

Enter action names for Alice:
Action 1: Rock
Action 2: Paper
Action 3: Scissors

Enter action names for Bob:
Action 1: Rock
Action 2: Paper
Action 3: Scissors

Enter the reward matrix for Alice:
Reward for Alice's Rock vs Bob's Rock: 0
Reward for Alice's Rock vs Bob's Paper: -1
Reward for Alice's Rock vs Bob's Scissors: 1
Reward for Alice's Paper vs Bob's Rock: 1
Reward for Alice's Paper vs Bob's Paper: 0
Reward for Alice's Paper vs Bob's Scissors: -1
Reward for Alice's Scissors vs Bob's Rock: -1
Reward for Alice's Scissors vs Bob's Paper: 1
Reward for Alice's Scissors vs Bob's Scissors: 0

Collected Game Data:
Character 1: Alice
Character 2: Bob
Alice's actions: ['Rock', 'Paper', 'Scissors']
Bob's actions: ['Rock', 'Paper', 'Scissors']

Reward Matrix for Alice:
[[ 0. -1.  1.]
 [ 1.  0. -1.]
 [-1.  1.  0.]]

Reward Matrix for Bob (automatically calculated as the opposite):
[[ 0.  1. -1.]
 [-1.  0.  1.]
 [ 1. -1.  0.]]

Nash Equilibria:

Equilibrium 1:
Alice's strategy:
  Rock: 0.3333
  Paper: 0.3333
  Scissors: 0.3333
Bob's strategy:
  Rock: 0.3333
  Paper: 0.3333
  Scissors: 0.3333

Value of the game: 0.0000
```

## Acknowledgments

This project uses the following open-source packages:

- [Nashpy](https://github.com/drvinceknight/Nashpy): A library for the computation of equilibria of 2 player normal form games.
- [NumPy](https://numpy.org/): The fundamental package for scientific computing with Python.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-party Licenses

Nashpy is licensed under the MIT License. The full text of the license can be found [here](https://github.com/drvinceknight/Nashpy/blob/main/LICENSE).
