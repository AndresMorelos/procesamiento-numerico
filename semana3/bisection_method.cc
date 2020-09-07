#include <functional>
#include <iostream>
using namespace std;
#define EPSILON 0.01

double func1(double x)
{
    return (-25182 * x) - (90 * (x * x)) + (44 * (x * x * x)) - (8 * (x * x * x * x)) + (0.7 * (x * x * x * x * x));
}

double func2(double x)
{
    return (5 * (x * x * x)) - (5 * (x * x)) + (6 * x) - 2;
}

void bisection(double xi, double xu, std::function<double(double)> function)
{
    if (function(xi) * function(xu) >= 0)
    {
        std::cout << "el valor Xi y Xu no son los requeridos\n";
        return;
    }

    double xr = xi;

    while ((xu - xi) >= EPSILON)
    {
        xr = (xi + xu) / 2;

        if (function(xr) == 0.0)
            break;
        else if (function(xr) * function(xi) < 0)
            xu = xr;
        else
            xi = xr;
    }

    std::cout << "La raíz es : " << xr << "\n";
}

int main()
{
    std::cout << "Función 1: ";
    double xi = 0.5, xu = 1;
    bisection(xi, xu, &func1);

    std::cout << "\nFunción 2: ";
    double xii = 0, xuu = 1;
    bisection(xii, xuu, &func2);
    return 0;
}