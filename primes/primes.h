#ifndef PRIMECALCULATOR_H
#define PRIMECALCULATOR_H

#include <vector>

#ifdef __cplusplus
extern "C" {
#endif

bool isPrime(int n);
std::vector<int> generatePrimes(int maxNum);

#ifdef __cplusplus
}
#endif

#endif /* PRIMECALCULATOR_H */
