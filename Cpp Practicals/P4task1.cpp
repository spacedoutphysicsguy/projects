#include <iostream>
#include <cmath>

int sum(int a,int b)
{
    return (a+b);
}

void decrease(int& a, int& b)
{
    a-=b;
}

int q(double a, double b, double c, double& x1, double& x2)
{
    double discriminant= b*b-4*a*c;
    if (discriminant<0)
    {
        return 0;
    }
    else 
    {
        if (discriminant==0)
        {
            x1=x2= -b/(2*a);
            return 1;
        }
        else
        {
            x1= (-b+sqrt(discriminant))/(2*a);
            x2= (-b-sqrt(discriminant))/(2*a);
            return 2;
        }
    }

}

int main(void)
{
    int a=8,b=6,c=2;
    double x1=0,x2=0;
    std::cout << "First task:" << sum(a,b) << std::endl;
    decrease(a,b);
    std::cout << "Second task:" << a << std::endl;
    std::cout << "Third task: Number of real roots: " << q(a,b,c,x1,x2);
    if (q(a,b,c,x1,x2)==2)
    {
        std::cout << " which are: " << x1 << " and " << x2 << std::endl;
    }
    else
    {
        if (q(a,b,c,x1,x2)==1)
        {
            std::cout << " which is: " << x1 << std::endl;
        }
    }

    return 0;

}