#include <iostream>
#include <cmath>
#include <complex>
#include <limits>

int main(void)
{
    double a,b,c,discriminant;
    std::cout << "Please enter the coefficients of your quadratic equation:" << std::endl;
    std::cin >> a ;
    std::cin >> b ;
    std::cin >> c ;
    discriminant= b*b-4*a*c;
    if (discriminant>0){
        double root1= (-b+sqrt(discriminant))/(2*a),root2= (-b-sqrt(discriminant))/(2*a);
        std::cout << "Congratulations! Your equation has distinct real roots. They are: " << root1 << " and " << root2 <<std::endl;  
    }
    else {
        if (discriminant==0){
            double root= -b/(2*a);
            std::cout << "Conngratulations! Your equation has one root, which is " << root << std::endl;
        }
        else {
            double re_bit= -b/(2*a), im_bit1= sqrt(-discriminant)/(2*a), im_bit2= -sqrt(-discriminant)/(2*a);
            std::cout << "Sadly Your equation has no real roots, but the complex roots are: " << re_bit << " + " << im_bit1 << "i and " << re_bit << " + " << im_bit2 << "i" << std::endl;
        }
    }
    return 0;
}