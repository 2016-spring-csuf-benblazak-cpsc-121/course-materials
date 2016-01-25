# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

PREP := ../scripts/prep.py
SECTION := ../scripts/section.py

# .............................................................................

PREPPED := $(wildcard *.md.prep)
PREPPED := $(PREPPED:%.prep=%)

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all: $(PREPPED)

clean:

cleanall:
	-rm -r $(PREPPED)

# -----------------------------------------------------------------------------

%:: %.prep
	$(PREP) -o '$@' '$<'

# -----------------------------------------------------------------------------

%:: makefile

