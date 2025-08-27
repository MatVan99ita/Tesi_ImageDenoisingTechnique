@echo off
REM Compila il file .tex principale (modifica "main.tex" con il nome del tuo file)
set TEXFILE=main.tex

REM Compilazione con pdflatex (due volte per aggiornare riferimenti)
pdflatex "%TEXFILE%"
pdflatex "%TEXFILE%"

REM Compilazione della bibliografia (se usi BibTeX, decommenta la riga sotto)
REM biber "%~nTEXFILE%"

REM Compilazione finale per aggiornare riferimenti
pdflatex "%TEXFILE%"
pdflatex "%TEXFILE%"

pause