#include "calculator.h"
#include <iostream>

using namespace std;

int* soma(int a, int b, int* result){
    *result = a + b;
    return result;
}

int main(){
    int r;
    soma(1, 2, &r);
    std::cout << "r is equal to " << r << std::endl;
    return 0;
}