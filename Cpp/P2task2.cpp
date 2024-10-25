#include <iostream>
#include <fstream>

int main(void)
{
    int input_num;
    std:: ofstream squares;
    squares.open("squares.dat");
    std::cout << "Please enter the range you want" << std::endl;
    std::cin >> input_num;
    while (input_num<0)
    {
        std::cout << "Your number is stupid, please enter a positive number" << std::endl;
        std::cin >> input_num;
    }
    for (int i=0;i<=input_num;i++)
    {
        std::cout << "The square of " << i << " is: " << i*i << std::endl;
        squares << i << "   " << i*i << std::endl;
    }
    squares.close();
    return 0;
}