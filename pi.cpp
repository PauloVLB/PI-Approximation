#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

double randNum(double min, double max){
    double r =  (double)rand() / (double)RAND_MAX;
    return min + r * (max-min);
}

int main() {
    
    srand(time(NULL));
    double power;

    cout << "Number of points = 10^";
    cin >> power;
    
    double nPoints = pow(10.0, power);
    double inPoints;
    
    for(unsigned long long int i = 0; i < nPoints; i++){
        double x = randNum(0,1);
        double y = randNum(0,1);
        
        double d = pow(x,2) + pow(y,2);
        
        if(d < 1) inPoints++;
    }
    double pi = 4 * (inPoints/nPoints);
    cout << fixed << setprecision(power) << pi << endl;

    return 0;
}
