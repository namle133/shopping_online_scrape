# Define variables
PYTHON = python3
PIP = $(PYTHON) -m pip
MAIN_FILE = tiki/tiki_scraper.py

# Default target
all: run

# Install project dependencies
install:
	$(PIP) install -r requirements.txt

# Run the main Python script
run:
	$(PYTHON) $(MAIN_FILE)

# Clean up generated files or caches
clean:
	rm -rf __pycache__

.PHONY: all install run clean

shopping_online:
	$(PYTHON) gui_input_shopping_online.py




