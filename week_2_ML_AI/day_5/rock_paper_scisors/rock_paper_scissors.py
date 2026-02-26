# rock-paper-scissors.py
from game import Game

def get_user_menu_choice():
    # ... code to display menu and get user choice ...
    user_choice_str = input('MENU \n 1) Play a new game \n 2) Show scores \n 3) Quit')
    try:# ... code to validate user input ...
        user_choice = int(user_choice_str)
        if user_choice in {1,2,3}:
            return user_choice # ... code to return user choice ..
        print('Number should be between 1 and 3')
        return False
    except:
        print('Invalid input')
        return False
    
   

def print_results(results):
   print(f"Wins : {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
   print('Thank you.')

def main():
   results = {"win": 0, "loss": 0, "draw": 0}
   while True:
        user_action = get_user_menu_choice()
        if not user_action:
           continue
        if user_action == 1:
           game = Game()
           result = game.play()
           results[result]+=1
           continue
        elif user_action == 2:
           print_results(results)
           continue
        elif user_action == 3:
            print_results(results)
            break


           
           
       


if __name__ == "__main__":
    main()
