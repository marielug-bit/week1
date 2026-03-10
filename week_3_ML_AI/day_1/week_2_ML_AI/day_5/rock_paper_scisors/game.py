import random

class Game:
    def get_user_item(self):
        choice = input('rock/paper/scissors, which item do you want to select? ')
        return choice
    
    def get_computer_item(self):
        return random.choice(['rock','paper','scissors'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            print('it is a draw')
            return 'draw'
        if user_item == 'rock':
            if computer_item == 'paper':
                print('Computer wins. His choice wa paper.')
                return 'loss'
            else:
                print('You win. Computer choice was scissors.')
                return 'win'
        if user_item == 'paper':
            if computer_item == 'scissors':
                print('Computer wins. His choice was scissors.')
                return 'loss'
            else:
                print('You win. Computer choice was rock.')
                return 'win'
        if user_item == 'scissors':
            if computer_item == 'rock':
                print('Computer wins. His choice was rock.')
                return 'loss'
            else:
                print('You win. Computer choice was paper.')
                return 'win'


    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        return self.get_game_result(user_item, computer_item)

#game = Game()
#game.play()
        # ... code to get user and computer choices ...
        # ... code to determine game result ...
        # ... code to print game outcome ...
        # ... code to return game result ...