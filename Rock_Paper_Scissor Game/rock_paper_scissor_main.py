import tkinter as tk
from tkinter import ttk
import random


class RockPaperScissors:
    def __init__(self):
        self.style = None
        self.result_label = None
        self.score_label = None
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("500x600")
        self.window.resizable(True, True)
        self.window.configure(bg='#f0f0f0') # #222222        # #f0f0f0
        # Initialize scores
        self.player_score = 0
        self.computer_score = 0
        self.games_played = 0
        self.match_winner = None

        # Create styles
        self.create_styles()
        # Create and pack widgets
        self.create_widgets()

    def create_styles(self):
        # Configure ttk styles
        style = ttk.Style()
        style.configure('Title.TLabel',
                        font=('Helvetica', 24, 'bold'),
                        background='#f0f0f0',
                        padding=10)
        style.configure('Score.TLabel',
                        font=('Helvetica', 14),
                        background='#f0f0f0',
                        padding=5)
        style.configure('Result.TLabel',
                        font=('Helvetica', 12),
                        background='#f0f0f0',
                        padding=10)
        style.configure('Game.TButton',
                        font=('Helvetica', 12),
                        padding=10)

    def create_widgets(self):
        # Title
        title = ttk.Label(
            self.window,
            text="Rock Paper Scissors",
            style='Title.TLabel'
        )
        title.pack(pady=20)

        # Match status
        self.match_status = ttk.Label(
            self.window,
            text="Best of 3 - First to win 2 games!",
            style='Score.TLabel'
        )
        self.match_status.pack(pady=5)


        # Score display
        self.score_label = ttk.Label(
            self.window,
            text=self.get_score_text(),
            style='Score.TLabel'
        )
        self.score_label.pack(pady=10)

        # Result display
        self.result_label = ttk.Label(
            self.window,
            text="Choose your move!",
            style='Result.TLabel',
            wraplength=400  # Wrap long text
        )
        self.result_label.pack(pady=20)

        # Buttons frame with custom styling
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=20)

        # Choice buttons with improved styling
        choices = ['Rock', 'Paper', 'Scissors']
        for choice in choices:
            btn=ttk.Button(
                button_frame,
                text=choice,
                style='Game.TButton',
                command=lambda c=choice: self.play_round(c))
            btn.pack(side='left', padx=10)

        # Reset button
        self.reset_button = ttk.Button(
            self.window,
            text = "New Match",
            style='Game.TButton',
            command=self.reset_match
        )
        self.reset_button.pack(pady=20)

    def get_score_text(self):
        return f"Score - Player: {self.player_score} Computer: {self.computer_score}"

    def get_computer_choice(self):
        return random.choice(['Rock', 'Paper', 'Scissors'])

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Tie"

        winning_moves = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }

        if winning_moves[player_choice] == computer_choice:
            return "Player"
        return "Computer"

    def check_match_winner(self):
        if self.player_score >= 2:
            self.match_winner = "Player"
            return True
        elif self.computer_score >= 2:
            self.match_winner = "Computer"
            return True
        return False


    def play_round(self, player_choice):
        if self.match_winner:  # If match is already over
            return
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        # Update display
        if result == "Player":
            self.player_score += 1
            message = "You won this round! 🎉"
        elif result == "Computer":
            self.computer_score += 1
            message = "Computer wins this round! 😔"
        else:
            message = "It's a tie! 🤝"

        self.games_played += 1
        # Check for match winner
        if self.check_match_winner():
            winner_text = "🏆 Congratulations! You've won the match!" if self.match_winner == "Player" else "Game Over - Computer wins the match!"
            self.result_label.config(
                text=f"Computer chose {computer_choice}\n{message}\n\n{winner_text}"
            )
        else:
            remaining = 2 - max(self.player_score, self.computer_score)
            status = f"Need {remaining} more {'win' if remaining == 1 else 'wins'} to win the match!"
            self.match_status.config(text=status)
            self.result_label.config(
                text=f"Computer chose {computer_choice}\n{message}"
            )
        # Update score display
        self.score_label.config(text=self.get_score_text())

    def reset_match(self):
        self.player_score = 0
        self.computer_score = 0
        self.games_played = 0
        self.match_winner = None
        self.score_label.config(
            text=f"Score - Player: {self.player_score} Computer: {self.computer_score}"
        )
        self.result_label.config(text="Choose your move!")
        self.match_status.config(text="Best of 3 - First to win 2 games!")
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
