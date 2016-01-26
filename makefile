# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

PREP := ./scripts/prep.py
SECTION := ./scripts/section.py

# .............................................................................

PREPPED := $(wildcard *.md.prep)
PREPPED := $(PREPPED:%.prep=%)

SECTIONED := grades.py
SECTIONED := $(SECTIONED:%=.gen.%.section.all)

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all: $(SECTIONED) $(PREPPED)

clean:
	-rm -r gen.* .gen.* */gen.* */.gen.*

cleanall: clean
	-rm $(PREPPED)

# -----------------------------------------------------------------------------

%:: %.prep
	$(PREP) -o '$@' '$<'

# this generates more than the specified file
.gen.%.section.all: %
	cp '$<' '.gen.$<'; $(SECTION) '.gen.$<'

# -----------------------------------------------------------------------------

%:: makefile
$(PREPPED): common.prep

