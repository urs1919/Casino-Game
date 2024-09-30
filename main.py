import random
import time

bet = 0
money = 5000

red_numbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

def main():
    print("CASINO")
    print("Your current balance is " + str(money))
    print("What do you want to do?")
    print("1 Gamble")

    
    if int(input()) == 1:
        gamble()
    else:
        print("Input a valid number")
        time.sleep(1)
        print()
        main()


def gamble():
    global money, bet
    print()
    print("What do you want to play?")
    print("1 Roulette")
    print("2 Slotmachines")
    print("3 Plinko")

    game_input = int(input())
    
    if game_input == 1:
        print()
        print("How much do you want to bet?")
        bet = int(input())
        money = money - bet
        print("New balance: " + str(money))
        roulette()
    
    elif game_input == 2:
        print()
        print("How much do you want to bet?")
        bet = int(input())
        money = money - bet
        print("New balance: " + str(money))
        slot_machine()

    elif game_input == 3:
        print()
        print("Currently unavailable")
        plinko()

    else:
        print("Input a valid number")
        time.sleep(1)
        print()
        gamble()




def roulette():
    print()
    print("Do you want to bet on ")
    print("1 a number")
    print("2 a colour")
    print("3 odd or even")
    
    roulette_number = random.randint(0, 36)
    roulette_input = int(input())
    number_bet = 0
    if roulette_input == 1:
        print()
        print("Which number do you want to bet on?")
        number_bet = int(input())
        if number_bet == roulette_number:
            print("You won " + (bet*36) + "$")
            money = money + bet*36
            main()
        else:
            print("You lost")
            main()

    elif roulette_input == 2:
        print()
        print("Do you want to bet on ")
        print("1 red")
        print("2 or black")
        if int(input()) == 1:
            if roulette_number in red_numbers:
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                main()
            else:
                print("You lost")
                main()
        else:
            if roulette_number in red_numbers and roulette_number != 0:
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                main()
            else:
                print("You lost")
                main()
    elif roulette_input == 3:
        print()
        print("Do you want to bet on ")
        print("1 odd")
        print("2 or even")
        if int(input()) == 1:
            if (roulette_number % 2) != 0:
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                main()
            else:
                print("You lost")
                main()
        else:
            if (roulette_number % 2) == 0:
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                main()
            else:
                print("You lost")
                main()



def slot_machine():
    pass

def plinko():
    pass




if __name__ == "__main__":
    main()