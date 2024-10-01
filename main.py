import random
import time

bet = 0
money = 5000

red_numbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

slots_characters = ["0", "§", "=", "!", "&", "$", "7"]

def main():
    print("CASINO")
    print("Your current balance is " + str(money))
    print("What do you want to do?")
    print("1 Gamble")
    print("2 Exit")

    menu_input = int(input())
    if menu_input == 1:
        gamble()
    elif menu_input == 2:
        exit()
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
        time.sleep(1)
        roulette()
    
    elif game_input == 2:
        print()
        print("How much do you want to bet?")
        bet = int(input())
        money = money - bet
        print("New balance: " + str(money))
        time.sleep(1)
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
    global money, bet
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
            print()
            print("You won " + str((bet*36)) + "$")
            money = money + bet*36
            time.sleep(1)
            print()
            main()
        else:
            print()
            print("You lost")
            time.sleep(1)
            print()
            main()

    elif roulette_input == 2:
        print()
        print("Do you want to bet on ")
        print("1 red")
        print("2 or black")
        if int(input()) == 1:
            if roulette_number in red_numbers:
                print()
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                time.sleep(1)
                print()
                main()
            else:
                print()
                print("You lost")
                time.sleep(1)
                print()
                main()
        else:
            if roulette_number in red_numbers and roulette_number != 0:
                print()
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                time.sleep(1)
                print()
                main()
            else:
                print()
                print("You lost")
                time.sleep(1)
                print()
                main()
    elif roulette_input == 3:
        print()
        print("Do you want to bet on ")
        print("1 odd")
        print("2 or even")
        if int(input()) == 1:
            if (roulette_number % 2) != 0:
                print()
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                time.sleep(1)
                print()
                main()
            else:
                print()
                print("You lost")
                time.sleep(1)
                print()
                main()
                
        else:
            if (roulette_number % 2) == 0:
                print()
                print("You won " + str((bet*2)) + "$")
                money = money + bet*2
                time.sleep(1)
                print()
                main()
            else:
                print()
                print("You lost")
                time.sleep(1)
                print()
                main()


def slot_machine():
    global money, bet

    print("Current balance: " + str(money))
    print("Current bet: " + str(bet))
    print("Type p to play or q to exit")

    slots_input = input()

    if slots_input == "p":
        print()
        slot1 = random.randint(0,6)
        slot2 = random.randint(0,6)
        slot3 = random.randint(0,6)

        print(slots_characters[slot1], slots_characters[slot2], slots_characters[slot3])
        if slot1 == slot2 and slot2 == slot3:
            print()
            print("JACKPOT!!! You won " + str((bet*300)) + "$")
            money = money + bet*300
            time.sleep(1)
            print()
            
        elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            print()
            print("You won " + str((bet*4)) + "$")
            money = money + bet*4
            time.sleep(1)
            print()
        else:
            print()
            

        slot_machine()
    elif slots_input == "q":
        main()
    else:
        print("Enter a valid character")
        slot_machine()

def plinko():
    pass




if __name__ == "__main__":
    main()