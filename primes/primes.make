CC=g++
CFLAGS=-c -Wall
LDFLAGS=-lm

all: libprimecalculator.so

libprimecalculator.so: PrimeCalculator.o
	$(CC) -shared -o $@ $^ $(LDFLAGS)

PrimeCalculator.o: PrimeCalculator.cpp
	$(CC) $(CFLAGS) -fPIC $< -o $@

clean:
	rm -f *.o *.so
