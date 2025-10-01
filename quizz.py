#!/usr/bin/python3

class Quizz:
    def __init__(self, quizz:dict):
        self.quizz = quizz

    def ask_user(self, q:str,r:str):
        user_input = input(q)    
        if user_input.lower() == r.lower():
            return 0
        else:
            return -1

    def start_quizz(self, attempts:int=3):
        for q in self.quizz.keys():
            r = self.quizz[q]
            q_result = self.ask_user(q,r)
            print(f"q_result:{q_result}")
            attempts += q_result
            print(f"Sorry, you have {attempts} chances left")
            while (attempts>0 and q_result<0) :
                q_result = self.ask_user(q,r)
                attempts += q_result
                print(f"Sorry, you have {attempts} chances left")
            if attempts == 0:
                break
        return attempts

def main():
    MAX_ATTEMPTS = 3
    quizz = { "Question 1: Combien de fois la France a gagné la coupe du monde ? ":"2", 
        "Question 2: Quand a été fondé Apple ? ":"1976",
        "Question 3: Qui a fondé SpaceX ? ":"Elon Musk" }
    
    print("Welcome to our quizz!")
    print(f"You have {MAX_ATTEMPTS} lives")
    game = Quizz(quizz)
    attempts = game.start_quizz(MAX_ATTEMPTS)
    
    if attempts > 0:
        print("Well done! You are the quiz winner!")
    else:
        print("Oh no, you lost the quiz...")

if __name__ == '__main__':
    main()