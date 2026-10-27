#include <iostream>
#include <string>
#include <vector> // Included for arrays

int main() {
    int choice = 0;
    std::vector<std::string> tasks;
    while (choice != 3) {
        std::cout << "\n=== CLI TASK TRACKER ===\n";
        std::cout << "1. Add Task\n";
        std::cout << "2. View Tasks\n";
        std::cout << "3. Exit\n";
        std::cout << "Enter choice: " << std::flush; // Force menu prompt to print immediately
        std::cin >> choice;
        switch (choice) {
            case 1: {
                std::string task;

                std::cout << "Please enter your task: " << std::flush;
                std::getline(std::cin >> std::ws, task);

                tasks.push_back(task);

                std::cout << "Task added successfully!\n";
                break;
            }
            case 2: 
                if (tasks.empty()){
                    std::cout << "Your TO-DO list is empty. \n";
                } else {
                    std::cout << "=== Your Tasks === \n";
                    for (size_t i = 0;i < tasks.size(); ++i) {
                        std::cout << (i+1) << ". " << tasks[i] << "\n";
                    }
                }
                break;
            case 3:
                std::cout << "Goodbye!\n";
                break;
            default:
                std::cout << "Invalid Option! \n";
                break;
        }
    
    }
    return 0;

}