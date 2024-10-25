#include <iostream>
#include <fstream>
#include <cmath>

double func(double y)
{
    return sqrt(y);
}

double sol(double t)
{
    return pow(t/2+1,2);
}

int main(void)
{
    double t=0,T,step_size,y0,y_eul,y_RK,k1,k2;
    int num_steps;
    char round_step;
    std::ofstream data,runs;
    data.open("ODE_solutions.dat");
    std::cout << "What is the initial value of y?" << std::endl;
    std::cin >> y0;
    y_RK=y0;
    y_eul=y0;
    std::cout << "What is the final time?" << std::endl;
    std::cin >> T;
    std::cout << "What is the step size?" << std::endl;
    std::cin >> step_size;
    num_steps= T/step_size;
    if (num_steps*step_size==T)
    {
        std::cout << "Good job, your final time is divisible by the step size.\nThere will be " << num_steps << " steps" << std::endl;
    }
    else 
    {
        std::cout << "Your final time is not divisible by the step size, this could also be due to rounding errors, this will cause the last step to be truncated. \nDo you want to round the step size so the output coincides with the final time? (y/n)" << std::endl;
        std::cin >> round_step;
        if (round_step='y')
        {
            step_size= T/double(num_steps);
        }
    }
    for (int i=0; i<num_steps;i++)
    {
        y_eul+= step_size*func(y_eul);
        k1= func(y_RK);
        k2= func(y_RK+step_size*k1);
        y_RK+= step_size*(k1+k2)/2;
        t+=step_size;
        data << t << "\t" << y_eul << "\t" << y_RK << "\t" << sol(t) << std::endl;
    }
    data.close();
    std::cout << "At time " << t << " The value of y is\n" << y_eul << " according to euler's method and \n" << y_RK << " according to RK2.\n" << sol(T) << " is the exact solution.\n" << fabs(y_eul-sol(T)) << " is the error while using eulers method." << std::endl;
    runs.open("step_size_variation.dat");
    for (step_size=0.0001;step_size<=1;step_size*=1.3)
    {
        num_steps= T/step_size;
        step_size= T/double(num_steps);
        t=0;
        y_eul=y0;
        y_RK=y0;
        for (int i=0; i<num_steps;i++)
        {
            y_eul+= step_size*func(y_eul);
            k1= func(y_RK);
            k2= func(y_RK+step_size*k1);
            y_RK+= step_size*(k1+k2)/2;
            t+=step_size;
        }
        runs << step_size << "\t" << "\t" << fabs(y_eul-sol(T)) << "\t" << fabs(y_RK-sol(T)) << std::endl;
    }
    runs.close();
    return 0;
}