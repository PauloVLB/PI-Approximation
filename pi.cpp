#include <iostream>
#include <math.h>

using namespace std;

double randNum(double min, double max){
    double r =  (double)rand() / (double)RAND_MAX;
    return min + r * (max-min);
}

int main()
{
    
    srand(time(NULL));
    double nPoints;
    cin >> nPoints;
    
    double inPoints;
    
    for(int i = 0; i < nPoints; i++){
        double x = randNum(0,1);
        double y = randNum(0,1);
        
        double d = pow(x,2) + pow(y,2);
        
        if(d < 1) inPoints++;
    }
        
    double pi = 4 * (inPoints/nPoints);
    
    cout << pi << endl;

    return 0;
}
