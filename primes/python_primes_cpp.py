import ctypes

# Load the shared library
primes_lib = ctypes.CDLL('./primes.so')

# Define the argument and return types of the isPrime function
primes_lib.isPrime.argtypes = [ctypes.c_int]
primes_lib.isPrime.restype = ctypes.c_bool

# Define the argument and return types of the generatePrimes function
primes_lib.generatePrimes.argtypes = [ctypes.c_int]
primes_lib.generatePrimes.restype = ctypes.POINTER(ctypes.c_int)

# Call the isPrime function
print(primes_lib.isPrime(7)) # True


def prime_calculator(n):
    num_primes = ctypes.c_int(0)
    primes_ptr = primes_lib.generatePrimes(n, ctypes.byref(num_primes))

    to_return = [primes_ptr[i] for i in range(num_primes.value)]

    primes_lib.free(primes_ptr)
    return to_return


# Convert the pointer to a Python list
print(prime_calculator(150))

