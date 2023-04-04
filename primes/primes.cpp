#include <vector>

using namespace std;

// Function to check if a number is prime
extern "C" bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= n/2; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

// Function to generate a list of primes up to a given number
extern "C" int* generatePrimes(int maxNum, int* numPrimes) {
    // Allocate memory for the array
    int* primes = new int[maxNum];
    int count = 0;
    for (int i = 2; i <= maxNum; i++) {
        if (isPrime(i)) {
            primes[count++] = i;
        }
    }
    *numPrimes = count;
    return primes;
}
// Function to generate a list of primes up to a given number
int main(){
    return 0;
}

