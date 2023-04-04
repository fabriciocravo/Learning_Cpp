import ctypes

# Load the shared library
calculator = ctypes.CDLL('./calculator.so')

# Define the argument and return types of the isPrime function
calculator.soma.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
calculator.soma.restype = ctypes.POINTER(ctypes.c_int)


def soma(a, b):
    result = ctypes.c_int(0)
    calculator.soma(a, b, ctypes.byref(result))
    return result.value

print(soma(10, 15))

