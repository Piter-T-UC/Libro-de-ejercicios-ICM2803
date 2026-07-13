$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode';
$pdf_mode = 1;
$postscript_mode = 0;
$dvi_mode = 0;

# Directorios de salida
$out_dir = 'Build';
$aux_dir = 'Build/temp';

# Viewer (Windows)
$pdf_previewer = 'start %O %S';

# Directorios a ignorar
@generated_exts = qw(aux fls fdb_latexmk log synctex);
