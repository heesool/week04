paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-%.png: %.dat plot.py
	python3 plot.py -i $*.dat -o $@

.PHONY: clean

clean:
	rm -f paper.pdf paper.aux paper.log paper.out paper.toc plot-data.png
