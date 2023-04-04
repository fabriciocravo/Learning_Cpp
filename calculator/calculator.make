CC=g++
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=calculator.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=calculator

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(EXECUTABLE) $(OBJECTS)