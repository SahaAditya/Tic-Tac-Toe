import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='black')
        self.root.geometry("428x926")
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_turn = 'X'
        self.turn_count = {'X': 0, 'O': 0}
        self.moves = {'X': [], 'O': []}
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.create_first_intro_screen()

    def create_first_intro_screen(self):
        self.clear_screen()
        intro_frame = tk.Frame(self.root, bg='black')
        intro_frame.pack(expand=True, fill=tk.BOTH)

        game_name_label = tk.Label(intro_frame, text="Tic Tac Toe", font=('Arial', 40), fg='white', bg='black')
        game_name_label.place(x=36, y=253, width=356)

        proceed_button = tk.Button(intro_frame, text="Let's Play", font=('Arial', 20), fg='black', bg='lightgrey',
                                   borderwidth=2, command=self.create_second_intro_screen)
        proceed_button.place(x=36, y=503, width=356)

        footer_label = tk.Label(intro_frame,
                                text="This is an experimental application made by Saha Aditya Kushal Orion.\nAll the rules are same as normal games except this game can be too long to play.",
                                font=('Arial', 7), fg='white', bg='black', justify=tk.CENTER)
        footer_label.place(x=36, y=821, width=356)

    def create_second_intro_screen(self):
        self.clear_screen()
        intro_frame = tk.Frame(self.root, bg='black')
        intro_frame.pack(expand=True, fill=tk.BOTH)

        game_name_label = tk.Label(intro_frame, text="Tic Tac Toe", font=('Arial', 40), fg='white', bg='black',
                                   anchor='w')
        game_name_label.place(x=36, y=110, width=356)

        rules_title_label = tk.Label(intro_frame, text="Game rules are as follows*", font=('Arial', 13), fg='white',
                                     bg='black', anchor='w')
        rules_title_label.place(x=36, y=171, width=356)

        rules_text = (
            "1. The game is played on a 3x3 grid.\n"
            "2. Players take turns putting their marks (X or O) in empty squares.\n"
            "3. The first player to get 3 of their marks in a row (up, down, across,\n or diagonally) is the winner.\n"
            "4. When all 9 squares are full, the game is over.\n"
            "5. Each player can only place their mark 4 times.\n"
            "6. If the fourth move does not result in a win, the first move of that player \nwill be removed."
        )

        rules_label = tk.Label(intro_frame, text=rules_text, font=('Arial', 8), fg='white', bg='black', justify=tk.LEFT)
        rules_label.place(x=36, y=234)

        proceed_button = tk.Button(intro_frame, text="Let's BEGIN", font=('Arial', 20), fg='black', bg='lightgrey',
                                   borderwidth=2, command=self.create_buttons)
        proceed_button.place(x=36, y=543, width=356)

        footer_label = tk.Label(intro_frame,
                                text="This is an experimental application made by Saha Aditya Kushal Orion.\nAll the rules are same as normal games except this game can be too long to play.",
                                font=('Arial', 7), fg='white', bg='black', justify=tk.CENTER)
        footer_label.place(x=36, y=821, width=356)

    def create_buttons(self):
        self.clear_screen()
        self.root.configure(bg='black')

        # Calculate button sizes and grid positions
        grid_width = 356
        grid_height = 356
        button_size = grid_width // 3

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 40), width=button_size // 10, height=2,
                                   fg='white', bg='black', borderwidth=2, highlightbackground='white',
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.place(x=36 + j * button_size, y=200 + i * button_size, width=button_size, height=button_size)
                self.buttons[i][j] = button

        self.display_turn_label()

    def display_turn_label(self):
        turn_label = tk.Label(self.root, text=f"Turn: {self.current_turn}", font=('Arial', 20), fg='white', bg='black')
        turn_label.place(x=160, y=570)

    def on_button_click(self, row, col):
        if self.buttons[row][col].cget('text') == "" and self.turn_count[self.current_turn] < 4:
            color = 'red' if self.current_turn == 'X' else 'blue'
            self.buttons[row][col].config(text=self.current_turn, fg=color)
            self.board[row][col] = self.current_turn
            self.moves[self.current_turn].append((row, col))
            self.turn_count[self.current_turn] += 1

            if self.check_winner():
                self.show_winner(self.current_turn)
                return

            if self.turn_count[self.current_turn] == 4:
                self.handle_fourth_move()

            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            self.update_turn_label()

    def update_turn_label(self):
        turn_label = tk.Label(self.root, text=f"Turn: {self.current_turn}", font=('Arial', 20), fg='white', bg='black')
        turn_label.place(x=160, y=570)

    def handle_fourth_move(self):
        first_move = self.moves[self.current_turn].pop(0)
        row, col = first_move
        self.buttons[row][col].config(text="", fg='white')
        self.board[row][col] = None
        self.turn_count[self.current_turn] -= 1

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_turn:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_turn:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_turn:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_turn:
            return True
        return False

    def show_winner(self, winner):
        self.clear_screen()
        result_frame = tk.Frame(self.root, bg='black')
        result_frame.pack(expand=True, fill=tk.BOTH)

        winner_label = tk.Label(result_frame, text=f"{winner} \nWON", font=('Arial', 40), fg='white', bg='black',justify=tk.CENTER)
        winner_label.place(x=166, y=312)

        play_again_button = tk.Button(result_frame, text="Play Again", font=('Arial', 20), fg='black', bg='lightgrey',
                                      borderwidth=2, command=self.reset_board)
        play_again_button.place(x=36, y=543, width=356)

        footer_label = tk.Label(result_frame, text="Thank you playing.",
                                font=('Arial', 10), fg='white', bg='black', justify=tk.CENTER)
        footer_label.place(x=36, y=821, width=356)

    def reset_board(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_turn = 'X'
        self.turn_count = {'X': 0, 'O': 0}
        self.moves = {'X': [], 'O': []}

        # Clear the screen first
        self.clear_screen()

        # Recreate buttons and display whose turn it is
        self.create_buttons()
        self.display_turn_label()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
