#Copy from http://mrbook.org/blog/tutorials/make/

CC=g++
CFLAGS=-c -Wall
SOURCES=print.c line_parser.c line_parser.h
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=print

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

