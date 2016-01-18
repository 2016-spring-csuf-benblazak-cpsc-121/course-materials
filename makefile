# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

PREP := $(wildcard *.md.prep)
PREPPED := $(PREP:%.prep=%)

SECTION_PY := grades.py
SECTION_PY := $(SECTION_PY:%=.gen.%)

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all:
	make $(SECTION_PY)
	for i in $(SECTION_PY); do \
		./scripts/section.py $$i '#'; \
	done
	make $(PREPPED)

clean:
	-rm .gen.*

cleanall: clean
	-rm $(PREPPED)

# -----------------------------------------------------------------------------

%: %.prep
	./scripts/prep.py -o '$@' '$^'

.gen.%: %
	cp '$^' '$@'



