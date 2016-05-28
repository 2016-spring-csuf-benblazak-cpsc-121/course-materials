# -----------------------------------------------------------------------------
# Copyright &copy; 2016 Ben Blazak <bblazak@fullerton.edu>
# Released under the [MIT License] (http://opensource.org/licenses/MIT)
# -----------------------------------------------------------------------------

PREP := ../scripts/prep.py
SECTION := ../scripts/section.py

# .............................................................................

BUILDDIR := build.pdf

# .............................................................................

PDF := $(wildcard quizzes/*.tex.prep)
PDF := $(PDF:quizzes/%.tex.prep=$(BUILDDIR)/%.answers.pdf) \
       $(PDF:quizzes/%.tex.prep=$(BUILDDIR)/%.questions.pdf)

# -----------------------------------------------------------------------------
.PHONY: all clean cleanall

all:
	touch quizzes/*
	make $(PDF)

clean: cleanquestions cleanshuffle
	-rm -r .gen.* */.gen.*

cleanall: clean
	-rm -r $(BUILDDIR)

# -----------------------------------------------------------------------------
.PHONY: all-% clean-% allquestions cleanquestions

all-%:
	touch quizzes/$**
	make $(filter $(BUILDDIR)/$*%,$(PDF))

clean-%:
	-rm -r $(BUILDDIR)/$** quizzes/.gen.$**
	# questions are not cleaned

allquestions:
	for i in questions/*.prep; do \
		make "questions/.gen.$$(basename -s '.prep' $$i)"; \
	done

cleanquestions:
	-rm -r questions/.gen.*
	for i in questions/*; do \
		if [ -d "$$i/code" ]; then (cd "$$i/code"; make clean;); fi; \
	done

# -----------------------------------------------------------------------------
.PHONY: allshuffle cleanshuffle

allshuffle:
	for i in $(BUILDDIR)/*.answers.pdf; do \
		make "$${i/%.answers.pdf/.shuffle.pdf}"; \
	done

cleanshuffle:
	-rm -r $(BUILDDIR)/.gen.blank.pdf $(BUILDDIR)/*.shuffle.pdf

# .............................................................................

$(BUILDDIR)/.gen.blank.pdf:
	echo '' | ps2pdf -sPAPERSIZE=letter - '$@'

$(BUILDDIR)/%.shuffle.pdf: $(BUILDDIR)/.gen.blank.pdf \
			   $(BUILDDIR)/%.answers.pdf \
			   $(BUILDDIR)/%.questions.pdf
	pdftk B='$(BUILDDIR)/.gen.blank.pdf' \
	      A='$(BUILDDIR)/$*.answers.pdf' \
	      Q='$(BUILDDIR)/$*.questions.pdf' \
	      shuffle B A Q output '$@'

# -----------------------------------------------------------------------------

questions/.gen.%,,.tex:: questions/%,,.tex.prep
	if [ -d 'questions/$*/code' ]; then (cd 'questions/$*/code'; make); fi;
	$(PREP) -o '$@' '$<'

quizzes/.gen.%.tex:: quizzes/%.tex.prep
	( echo '!dnl,exec(self._filename="$<")'; \
	  echo '!dnl,exec(self._cwd = "quizzes")'; \
	  echo '!dnl,input(../common.prep)'; \
	  echo '!exec,prep,(doc.gen_quiz_tex)'; \
	) | $(PREP) -o '$@' '$<' -

quizzes/%.questions.tex: quizzes/%.tex
	( echo '\\long\\def \\question #1{#1}'; \
	  echo '\\long\\def \\answer #1{}'; \
	  echo '\\input{$*.tex}'; \
	  echo; \
	) > '$@'

quizzes/%.answers.tex: quizzes/%.tex
	( echo '\\long\\def \\question #1{}'; \
	  echo '\\long\\def \\answer #1{#1}'; \
	  echo '\\input{$*.tex}'; \
	  echo; \
	) > '$@'

quizzes/%.pdf: quizzes/%.tex
	make $$( i='$(notdir $<)'; \
		 i=$${i#*,,}; \
		 i=$${i%,,*}; \
		 i=($${i//,,/ }); \
		 i=($${i[@]/#/questions/.gen.}); \
		 i=($${i[@]/%/,,.tex}); \
		 echo $${i[@]}; )
	( cd quizzes; \
	  ulimit -S -n 512; \
	  latexmk --shell-escape -lualatex -pdf '$*.tex'; )
	touch '$@'  # for when latexmk does nothing

$(BUILDDIR)/%.pdf: quizzes/.gen.%.pdf
	mkdir -p $(BUILDDIR)
	cp '$<' '$@'

# -----------------------------------------------------------------------------

.SECONDARY:

%:: makefile
$(PDF): common.prep quizzes/common.tex

