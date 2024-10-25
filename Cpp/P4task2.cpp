#include <iostream>
#include <cmath>
#include <vector>
#include <array>

void p_sum(const std::array<int,20>& a,std::array<int,20>& b)
{
    b[0]=a[0];
    for(int i=1;i< 20; i++)
    {
        b[i]= b[i-1]+a[i];
    }
}

int main(void)
{
    std::array<int,20> input,sums;
    for(int i=0; i<20;i++)
    {
        input[i]=i;
        std::cout << " ,"<< input[i];
    }
    std::cout << std::endl;
    p_sum(input,sums);
    for(int i=0;i<20;i++)
    {
        std::cout << " ,"<< sums[i];
    }
    std::cout << std::endl;
    return 0;
}