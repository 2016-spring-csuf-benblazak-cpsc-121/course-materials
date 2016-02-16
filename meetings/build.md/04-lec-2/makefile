# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

TARGET := main

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall run

all: $(TARGET)

clean:
	-rm -r $(TARGET)

cleanall: clean

run: all
	./$(TARGET)

# -----------------------------------------------------------------------------

$(TARGET): $(wildcard *.h) $(wildcard *.cpp)
	clang++ -std=c++14 *.cpp -o $@

# -----------------------------------------------------------------------------

%:: makefile

