#include <iostream>
#include <random>

int main() {
    int guess = 0;


    std::random_device rd;  // The system will generate a random seed stored in an object called rd
    std::mt19937 gen(rd()); // the system will now generate a random big number using an algorithm such that it used the random seed gained from rd 
    std::uniform_int_distribution<int> distrib(1, 100); // the system will now tone down/scale up the value to match the parsamter 1,100 which is stored as an object

    int answer = distrib(gen); // object distrib constraints the value while object gen generates the number    
    while (answer != guess) {
        std::cout << "Please guess your number: \n";
        

        if (!(std::cin >> guess))  { // checks if the value guess is an integer, if NOT then the if statement will be true
            std::cin.clear(); // clearing the mode as error would stay there forever
            std::cin.ignore(10000, '\n'); // Ignores up to 10,000 characters or until the user pressed Enter ('\n') as it resets the memory 
            std::cout << "Invalid, please input an integer. \n" ;
            continue; // restarts loop
        }

        std::cout << "You've guessed, " << guess << "\n";
        if (guess < answer) {
            std::cout << "Your number was too low! \n";
        }
        else if (guess > answer){
            std::cout << "Your number was too high! \n";
        }
        else {
            std::cout << "You've guessed it! \n";
        }

    }
    return 0;
}