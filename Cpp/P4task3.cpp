#include <iostream>
#include <cmath>
#include <array>
#include <format>

template<const std::size_t dimension>

double determinant(const std::array<std::array<double,dimension>,dimension>& M,int dim)
{
    double det=0;
    if (dim>2)
    {
        std::array<std::array<double,dimension>,dimension> new_M;
        for (int i=0;i<dim;i++)
        {
            for (int j=1;j<dim;j++)
            {   
                int index=0;
                for (int k=0;k<dim;k++)
                {
                    if (k!=i)
                    {
                        new_M[j-1][index]=M[j][k];
                        index++;
                    }
                }                
            }
            det+= pow(-1,i) * M[0][i]*determinant(new_M,dim-1);
        }
    }
    else
    {
        det= M[0][0]*M[1][1]-M[0][1]*M[1][0];
    }
    return det;
}

template<const std::size_t dimension>
double trace(const std::array<std::array<double,dimension>,dimension>& M,int dim)
{
    double tr=0;
    for (int i=0;i<dim;i++)
    {
        tr+= M[i][i];
    }
    return tr;
}

int main(void)
{
    const std:: size_t dimension=3;
    int dim= 3;
    std::array<std::array<double,dimension>,dimension> M;
    std::cout << "Dimension is:" << dim << std::endl;
    for (int i=0;i<dim;i++)
    {
        for (int j=0;j<dim;j++)
        {
            std::cout << std::format ("Element in position [{},{}]",i,j) << std::endl;
            std::cin >> M[i][j];
        }
    }

    std::cout << std::format ("The determinant is: {} and the trace is: {}",determinant(M,dim),trace(M,dim)) << std::endl;
    return 0;
    
}