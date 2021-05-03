all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py

build/Bragg.pdf: data_scripts/Bragg.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/Bragg.py

build/Kupfer.pdf: data_scripts/Kupfer.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/Kupfer.py

build/zink.pdf: data_scripts/zink.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/zink.py
	
build/gallium.pdf: data_scripts/gallium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/gallium.py

build/brom.pdf: data_scripts/brom.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/brom.py	

build/rubidium.pdf: data_scripts/rubidium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/rubidium.py	

build/strontium.pdf: data_scripts/strontium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/strontium.py

build/zirkonium.pdf: data_scripts/zirkonium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/zirkonium.py		

build/rydberg.pdf: data_scripts/energie.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/energie.py		
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/Kupfer.pdf build/Bragg.pdf build/zink.pdf build/gallium.pdf build/brom.pdf build/rubidium.pdf build/strontium.pdf build/zirkonium.pdf build/rydberg.pdf

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
