# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

PREP := ../scripts/prep.py
SECTION := ../scripts/section.py

# .............................................................................

BUILDDIR := build.md

# .............................................................................

PREPPED := $(wildcard assignments/*.md.prep)
PREPPED := $(PREPPED:assignments/%.prep=$(BUILDDIR)/%)

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all: $(PREPPED)

clean:

cleanall: clean
	-rm -r $(BUILDDIR)

# -----------------------------------------------------------------------------

$(BUILDDIR)/%.md:: assignments/%.md.prep
	mkdir -p $(BUILDDIR)
	i='$*'; \
	i=$${i/,/ }; \
	i=$${i/,/ }; \
	i=($${i}); \
	( echo '!dnl,exec(self._filename="$<")'; \
	  echo '!dnl,exec(self._cwd="assignments")'; \
	  echo '!dws,input(common.prep)'; \
	  echo '# !(doc.title)'; \
	  echo ''; \
	) | $(PREP) -o '$@' '$<' - "questions/$${i[2]}.md.prep"; \
	if [ -d "../../$${i[0]}" ]; then cp '$@' "../../$${i[0]}/readme.md"; fi;

# -----------------------------------------------------------------------------

%:: makefile
$(PREPPED): questions assignments/common.prep

