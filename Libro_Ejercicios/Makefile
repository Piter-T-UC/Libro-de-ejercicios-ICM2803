.PHONY: all pdf clean clean-all help

MAIN := main
OUTPUT_DIR := Build
TEMP_DIR := $(OUTPUT_DIR)/temp
LOGS_DIR := $(OUTPUT_DIR)/logs

all: pdf

pdf:
	@if not exist "$(OUTPUT_DIR)" mkdir "$(OUTPUT_DIR)"
	@if not exist "$(TEMP_DIR)" mkdir "$(TEMP_DIR)"
	@if not exist "$(LOGS_DIR)" mkdir "$(LOGS_DIR)"
	latexmk -pdf -output-directory=$(OUTPUT_DIR) -auxdir=$(TEMP_DIR) -interaction=nonstopmode -synctex=1 $(MAIN).tex

clean:
	latexmk -c -output-directory=$(OUTPUT_DIR) -auxdir=$(TEMP_DIR) $(MAIN).tex
	@if exist "$(TEMP_DIR)" rmdir /s /q "$(TEMP_DIR)" 2>nul || true

clean-all:
	@if exist "$(OUTPUT_DIR)" rmdir /s /q "$(OUTPUT_DIR)" 2>nul || true
	latexmk -C $(MAIN).tex

help:
	@echo Comandos disponibles:
	@echo   make pdf       - Compilar PDF
	@echo   make clean     - Limpiar archivos auxiliares
	@echo   make clean-all - Eliminar todos los archivos generados
	@echo   make help      - Mostrar esta ayuda
