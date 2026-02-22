import random
import time

def number_guessing_game():
    """
    A simple number guessing game where the player tries to guess a random number.
    """
    print("=" * 50)
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < 1 or guess > 100:
                print("⚠️  Please enter a number between 1 and 100!\n")
                continue
            
            if guess < secret_number:
                print("📈 Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("📉 Too high! Try a lower number.\n")
            else:
                print("\n" + "🎉" * 20)
                print(f"🏆 CONGRATULATIONS! You guessed it right! 🏆")
                print(f"The number was {secret_number}")
                print(f"You won in {attempts} attempts!")
                print("🎉" * 20)
                return
            
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"💡 You have {remaining} attempts remaining.\n")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
    
    # Game over - ran out of attempts
    print("\n" + "💔" * 20)
    print(f"😢 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")
    print("Better luck next time!")
    print("💔" * 20)

def snake_game_text():
    """
    A simple text-based snake game where you collect food and avoid boundaries.
    """
    print("=" * 50)
    print("🐍 Welcome to Text Snake Game! 🐍")
    print("=" * 50)
    print("\nControls: w=up, s=down, a=left, d=right")
    print("Collect the food (🍎) and avoid hitting the walls!")
    print("Press Enter after each move.\n")
    
    # Game setup
    width, height = 10, 10
    snake = [[5, 5]]  # Starting position
    food = [random.randint(0, height-1), random.randint(0, width-1)]
    direction = [0, 1]  # Start moving right
    score = 0
    
    def print_board():
        for y in range(height):
            for x in range(width):
                if [y, x] == food:
                    print("🍎", end=" ")
                elif [y, x] in snake:
                    if [y, x] == snake[0]:
                        print("🐍", end=" ")
                    else:
                        print("🟢", end=" ")
                else:
                    print("⬜", end=" ")
            print()
        print(f"\nScore: {score} | Length: {len(snake)}")
    
    print("Starting in 3 seconds...")
    time.sleep(1)
    
    while True:
        print("\n" + "=" * 50)
        print_board()
        
        # Get input
        move = input("\nYour move (w/a/s/d) or 'q' to quit: ").lower()
        
        if move == 'q':
            print("\n👋 Thanks for playing! Final score:", score)
            break
        
        # Update direction
        if move == 'w' and direction != [1, 0]:
            direction = [-1, 0]
        elif move == 's' and direction != [-1, 0]:
            direction = [1, 0]
        elif move == 'a' and direction != [0, 1]:
            direction = [0, -1]
        elif move == 'd' and direction != [0, -1]:
            direction = [0, 1]
        else:
            print("Invalid move! Use w/a/s/d")
            continue
        
        # Move snake
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        
        # Check collision with walls
        if (new_head[0] < 0 or new_head[0] >= height or 
            new_head[1] < 0 or new_head[1] >= width):
            print("\n💥 GAME OVER! You hit the wall!")
            print(f"Final Score: {score}")
            break
        
        # Check collision with self
        if new_head in snake:
            print("\n💥 GAME OVER! You hit yourself!")
            print(f"Final Score: {score}")
            break
        
        # Add new head
        snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == food:
            score += 10
            print("\n🎉 Yum! Food collected! +10 points")
            # Generate new food
            food = [random.randint(0, height-1), random.randint(0, width-1)]
            while food in snake:
                food = [random.randint(0, height-1), random.randint(0, width-1)]
        else:
            # Remove tail if no food eaten
            snake.pop()

def rock_paper_scissors():
    """
    Classic Rock, Paper, Scissors game against the computer.
    """
    print("=" * 50)
    print("✊ Rock, Paper, Scissors Game! ✋")
    print("=" * 50)
    
    choices = ['rock', 'paper', 'scissors']
    emojis = {'rock': '✊', 'paper': '✋', 'scissors': '✌️'}
    
    player_score = 0
    computer_score = 0
    rounds = 0
    
    print("\nBest of 5 rounds! Let's play!\n")
    
    while rounds < 5:
        print(f"\n--- Round {rounds + 1} ---")
        print(f"Score - You: {player_score} | Computer: {computer_score}")
        
        player_choice = input("\nChoose (rock/paper/scissors) or 'q' to quit: ").lower()
        
        if player_choice == 'q':
            print("\n👋 Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        rounds += 1
        
        print(f"\nYou chose: {emojis[player_choice]} {player_choice}")
        print(f"Computer chose: {emojis[computer_choice]} {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 You win this round!")
            player_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1
    
    # Final results
    if rounds == 5:
        print("\n" + "=" * 50)
        print("🏁 GAME OVER! 🏁")
        print(f"Final Score - You: {player_score} | Computer: {computer_score}")
        
        if player_score > computer_score:
            print("🏆 YOU WIN THE GAME! 🏆")
        elif computer_score > player_score:
            print("💻 COMPUTER WINS THE GAME! 💻")
        else:
            print("🤝 IT'S A TIE GAME! 🤝")
        print("=" * 50)

def main_menu():
    """
    Main menu to select which game to play.
    """
    while True:
        print("\n" + "=" * 50)
        print("🎮 PYTHON GAME COLLECTION 🎮")
        print("=" * 50)
        print("\nChoose a game to play:")
        print("1. 🎯 Number Guessing Game")
        print("2. 🐍 Text Snake Game")
        print("3. ✊ Rock, Paper, Scissors")
        print("4. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            snake_game_text()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()
