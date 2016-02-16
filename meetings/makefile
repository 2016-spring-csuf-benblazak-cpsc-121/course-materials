# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

PREP := ../scripts/prep.py
SECTION := ../scripts/section.py

# .............................................................................

BUILDDIR := build.md

# .............................................................................

PREPPED := $(wildcard meetings/*.md.prep)
PREPPED := $(PREPPED:meetings/%.prep=$(BUILDDIR)/%)

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all: $(PREPPED)

clean:

cleanall: clean
	-rm -r $(BUILDDIR)

# -----------------------------------------------------------------------------

$(BUILDDIR)/%.md:: meetings/%.md.prep
	-rm -r '$(BUILDDIR)/$*'
	if [ -d 'meetings/$*' ]; then cp -R 'meetings/$*/' '$(BUILDDIR)/$*/'; fi
	mkdir -p $(BUILDDIR)
	( echo '!dnl,exec(self._filename="$<")'; \
	  echo '!dnl,exec(self._cwd="meetings")'; \
	  echo '!dws,input(common.prep)'; \
	  echo '# !(doc.title)'; \
	  echo ''; \
	  cat '$<'; \
	  echo ''; \
	  echo '-------------------------------------------------------------------------------'; \
	  echo '!(doc.license.md)'; \
	  echo ''; \
	) | $(PREP) -o '$@' --jobname '$*' -

# -----------------------------------------------------------------------------

%:: makefile
$(PREPPED): meetings/common.prep

