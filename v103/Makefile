all: build/main.pdf

# hier Python-Skripte:
build/probe1single.pdf: data_scripts/probe1single.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe1single.py

build/probe2single.pdf: data_scripts/probe2single.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe2single.py

build/probe3single.pdf: data_scripts/probe3single.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe3single.py

build/probe4single.pdf: data_scripts/probe4single.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe4single.py
	
build/probe1double.pdf: data_scripts/probe1double.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe1double.py	
		
build/probe2double.pdf: data_scripts/probe2double.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe2double.py

build/probe3double.pdf: data_scripts/probe3double.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe3double.py

build/probe4double.pdf: data_scripts/probe4double.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/probe4double.py					
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/probe1single.pdf build/probe2single.pdf build/probe3single.pdf build/probe4single.pdf build/probe1double.pdf build/probe2double.pdf build/probe3double.pdf build/probe4double.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
