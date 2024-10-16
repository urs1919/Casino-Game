#include <iostream>
#include <ctime>
#include <string>

using namespace std;

int bet;
int money = 5000;

void gamble() {
    
}

int main() {
    srand(time(0));
    int* menu_input = new int;
    cout << "CASINO" << endl;
    cout << "Your current balance is " << money << endl;
    cout << "What do you want to do?" << endl;
    cout << "1 Gamble" << endl;
    cout << "2 Exit" << endl;
    cin >> *menu_input;
    if(*menu_input == 1) {
        delete menu_input;
        gamble();
    } else if(*menu_input == 2) {
        delete menu_input;
        return 0;
    } else {
        cout << "Input a valid number" << endl;
        main();
    }

    return 0;
}