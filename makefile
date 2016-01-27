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

SUBMAKE := assignments meetings

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all: $(SECTIONED) $(PREPPED)
	for i in $(SUBMAKE); do (cd $$i; make $@;); done

clean:
	-rm -r .gen.*
	for i in $(SUBMAKE); do (cd $$i; make $@;); done

cleanall: clean
	-rm $(PREPPED)
	for i in $(SUBMAKE); do (cd $$i; make $@;); done

# -----------------------------------------------------------------------------

%:: %.prep
	$(PREP) -o '$@' '$<'

# this generates more than the specified file
.gen.%.section.all: %
	cp '$<' '.gen.$<'; $(SECTION) '.gen.$<'

# -----------------------------------------------------------------------------

%:: makefile
$(PREPPED): common.prep

