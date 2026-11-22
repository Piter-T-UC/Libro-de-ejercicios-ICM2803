# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Libro de Ejercicios - Dinámica de Sistemas Mecánicos** is a LaTeX-based exercise and solution book for ICM2803 (Dynamics of Mechanical Systems). The project contains 6 chapters with theory, exercises, and solutions, all compiled to a single PDF.

### Repository Structure

```
Contenidos/
├── C0_Repaso/              # Chapter 0: Review (Vector Algebra & Calculus)
├── C1_Cinematica/          # Chapter 1: Kinematics
├── C2_Cinetica1/           # Chapter 2: Kinetics Part 1
├── C3_Cinetica2/           # Chapter 3: Kinetics Part 2
├── C4_CuerposRigidos/      # Chapter 4: Rigid Bodies
├── C5_MecanicaLagrangiana/ # Chapter 5: Lagrangian Mechanics
├── Guia_de_lectura.tex     # Front-matter page that introduces the ducks
└── Figuras/                # Global figures (e.g., title page graphics)

Paquetes/                   # LaTeX packages and styling
├── Dinamica.sty            # Styles, switches, `solucion` env, \respuesta, kinematics macros
├── TikzDina.sty            # TikZ drawing macros and color definitions
└── Patos.sty               # Didactic ducks (tikzducks): tip / ojo / truco / resumen

Plantillas/CN_EYY_PZZ_plantilla.tex   # Problem template — start every new problem here

main.tex                    # Master file (includes all chapters)
Build/                      # Compiled PDF and temporary files (generated)
```

### Each Chapter Structure

Every chapter `CN_[Name]/` contains:
- `CN_00_introduccion.tex` - Introduction with key concepts and objectives
- `CN_0X_tema.tex` - Theoretical sections (if needed)
- `Ejercicios/CN_E0Y_problemas.tex` - Theme aggregator (`\input`s the problem files)
- `Ejercicios/Problemas/` - Individual exercise files (statement **and** solution)
- `Figuras/` - Chapter-specific figures (manifest.json + images)

### Solutions (inline) and switches

There is **no solutions chapter** and no `Soluciones/` folders. Each solution lives at the
end of its problem file, inside a single box:

```latex
\begin{solucion}{Título del problema}
...
\end{solucion}
```

`solucion` (Dinamica.sty) is a `+b` environment: when `\mostrarSolucionfalse` is set in
`main.tex`, its body is discarded entirely. The same mechanism hides the ducks:

| Command / env | Duck | Switch (in `main.tex` PANEL DE CONTROL) |
|---|---|---|
| `\patotip[acc]{texto}` | engineer (helmet) | `\mostrarTipsfalse` |
| `\patoojo[acc]{texto}` | signpost "!" | `\mostrarOjofalse` |
| `\patotruco[acc]{texto}` | wizard | `\mostrarTrucosfalse` |
| `\begin{resumen}[Título]...\end{resumen}` | graduate on a blue box | `\mostrarResumenfalse` |

`[acc]` = extra tikzducks keys (e.g. `squareglasses,shovel`, `tie=blue!70!black`).
Use `\respuesta{...}` for final results instead of `\boxed`. Because these environments
grab their body as an argument, a raw `#` inside them breaks (escape URLs as `\#`).

## Building & Compilation

### Quick Commands

```bash
# Compile PDF
make pdf

# Clean auxiliary files (keeps PDF)
make clean

# Full clean (removes everything including PDF)
make clean-all

# Help
make help
```

### Key Details

- **Tool**: latexmk (configured in `.latexmkrc`)
- **Output**: `Build/main.pdf` (27+ pages)
- **Compilation**: Two-pass to resolve references
- **Platform**: Windows (MiKTeX), but cross-platform compatible
- **Encoding**: UTF-8 with LF line endings (via .gitignore)

## File Naming Conventions

**Strict nomenclature** ensures consistency and scalability:

### Chapter Files
- `CN_00_introduccion.tex` - Chapter N introduction
- `CN_0X_tema.tex` - Theoretical section X

### Exercise Files (in `Ejercicios/Problemas/`)
```
CN_E[YY]_P[ZZ]_titulo.tex
```
- C0 = Repaso, C1 = Cinemática, ..., C5 = Mecánica Lagrangiana
- YY = Theme number (01, 02, ...) within chapter
- ZZ = Problem number within theme (01, 02, ...)
- `titulo` = snake_case descriptive name

**Example**: `C1_E01_P03_hormiga_velocista.tex` (Chapter 1, Theme 1, Problem 3)

### Solutions
Inline at the end of each problem file (`solucion` environment) — no separate files.

## Adding New Exercises

### Step 1: Create File
```
Contenidos/CX_[Name]/Ejercicios/Problemas/CX_E[YY]_P[ZZ]_titulo.tex
```

### Step 2: Copy the template
Copy `Plantillas/CN_EYY_PZZ_plantilla.tex`: standard comment header (capítulo, tema,
problema, origen), `\subsubsection{}`, statement + `enumerate`, TikZ figure with `\def`
parameters, and the `solucion` box with examples of every duck.

### Step 3: Key Requirements for TikZ Figures
- **Parameters first**: Use `\def\PARAM{value}` at top for all dimensions
- **Organized comments**: Group related drawing code with `-- SECTION --` headers
- **Consistent scale**: Default `scale=1.5` (adjust as needed)
- **Colors**: Use predefined colors from `TikzDina.sty` (azul, gris1, myred)
- **Labels**: Always include `\caption{}` and unique `\label{fig:...}`

### Step 4: Write the solution in the same file
At the end of the problem file, inside `\begin{solucion}{Título}...\end{solucion}`. Then wire
the problem into its theme aggregator `CN_EYY_problemas.tex` (`\input` + `\clearpage`).

**TikZ, not raster:** all figures — in both problems and solutions — must be native TikZ.
Do not use `\includegraphics`; if a source has a raster image, redraw it as a `tikzpicture`
in the house style. Note that Spanish `babel` makes `"` an active character, so the
`\pic [..., "$\theta$", ...] {angle=...}` quotes syntax breaks — draw angle arcs with
`\draw ... arc (...)` + a `\node` label instead.

### Step 5: Update Figure Manifest
Edit `Contenidos/CX_[Name]/Figuras/manifest.json` to register any new figures with metadata.

### Step 6: Compile & Test
```bash
make clean-all
make pdf
```
Verify:
- PDF compiles without errors
- Figures render correctly
- Cross-references resolve (no "???")
- Visual style is consistent with existing exercises

## Visual Style & Energy

The book maintains a specific visual identity (intentionally preserved):

- **Colors**: Orange-based TikZ (azul #00A0FF, gris1 #2C3E50, myred #BF0000)
- **Typography**: Sans-serif (lmodern) for modern, clean appearance
- **Figures**: TikZ-native with parameters explicitly defined
- **Environments**: one `solucion` box per solution; ducks for tips/ojo/trucos/resúmenes
- **Mathematics**: Inline LaTeX with physics package macros (`\vec{}`, `\der{}`, etc.)

**When adding exercises**: Match the style of existing problems (e.g., `C1_E01_P01_hormiga_velocista.tex` is the reference example). Do not deviate from this established visual pattern.

## Git Workflow

### Remote & repo root
The project is already pushed to GitHub:
`https://github.com/Piter-T-UC/Libro-de-ejercicios-ICM2803.git` (remote `origin`, branch `main`).

**Important:** the git repository root is the **parent** directory `E:/Claude`, not the book
folder `E:/Claude/Libro_Ejercicios`. Git commands therefore see paths prefixed with
`Libro_Ejercicios/`, and sibling folders (`MecaPy/`, `PDF-MD/`) are also inside the repo. When
committing book changes, stage explicit `Libro_Ejercicios/...` paths so unrelated sibling
changes are not swept in.

### Adding Exercises
```bash
# Create branch for new work
git checkout -b feature/add-exercises-c1-theme-02

# Make changes, compile, verify PDF

# Commit with clear message
git commit -m "[feat] Add C1 Theme 02 exercises: roller on disk problems"

# Push and create PR
git push origin feature/add-exercises-c1-theme-02
```

### Commit Message Format
```
[TYPE] Short description (max 72 chars)

Detailed explanation if needed.
- Bullet point 1
- Bullet point 2
```

**Types**: `[feat]`, `[fix]`, `[refactor]`, `[docs]`, `[style]`

## Chapter Summary

| Capítulo | Tema | Status | Ejercicios |
|----------|------|--------|-----------|
| C0 | Repaso (Álgebra & Cálculo) | Migrated | 12 (not yet wired into main.tex) |
| C1 | Cinemática | Migrated | ~30 across 5 temas |
| C2 | Cinética 1 (Partícula) | Migrated | 20 (P01–P20) |
| C3 | Cinética 2 (Sistema) | Migrated | 14 (P01–P14) |
| C4 | Cuerpo Rígido | Populated | 10 (P01–P10) |
| C5 | Mecánica Lagrangiana | Populated | 8 (P01–P08) |

**Solutions coverage**: inline in each problem file (`solucion` env). C3 has none yet
(Ayudantías 2026 import pending at the time of writing).

## Key Files to Know

- `main.tex` - Master file; update only if changing chapter includes or adding chapters
- `Paquetes/Dinamica.sty` - All style definitions, command macros, environment definitions
- `Paquetes/TikzDina.sty` - Color definitions and TikZ libraries
- `.latexmkrc` - Latexmk configuration; modify only if changing build process
- `Makefile` - Build automation; maps to latexmk
- `README.md` - User-facing documentation (compilation, structure, FAQ)
- `CONTRIBUTING.md` - Guidelines for contributors

## Common Tasks

### Verify compilation without opening PDF
```bash
make clean && make pdf 2>&1 | grep -i "error\|warning"
```

### Find all undefined references
```bash
grep "??" Build/main.log
```

### Update all figure paths in a chapter
Search-replace: `Capitulo X:` → `CX_` in all `.tex` files within that chapter directory.

### Rename a problem file
Remember to update:
1. The file itself
2. Any `\input{}` statements that reference it
3. The `manifest.json` in the chapter's `Figuras/` directory

## Next Steps

1. **Wire C0 into main.tex**: C0 Repaso is only partially included (C0_02 is commented).
2. **Expand solution coverage** for C1–C3 (inline `solucion` boxes).
3. **Chapters C2–C5 are commented out in `main.tex`**; uncomment when ready.

---

**Last Updated**: 2026-11-22 (Removed C6 chapter: solutions now inline in `solucion` boxes;
added Patos.sty ducks + switches, Guía de lectura and problem template)
