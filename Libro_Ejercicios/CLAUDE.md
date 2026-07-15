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
├── C6_Soluciones/          # Chapter 6: Solutions (consolidated, one section per chapter)
└── Figuras/                # Global figures (e.g., title page graphics)

Paquetes/                   # LaTeX packages and styling
├── Dinamica.sty            # Main styles, colors, tcolorbox environments
└── TikzDina.sty            # TikZ drawing macros and color definitions

main.tex                    # Master file (includes all chapters)
Build/                      # Compiled PDF and temporary files (generated)
```

### Each Chapter Structure

Every chapter `CN_[Name]/` contains:
- `CN_00_introduccion.tex` - Introduction with key concepts and objectives
- `CN_0X_tema.tex` - Theoretical sections (if needed)
- `Ejercicios/CN_E0Y_problemas.tex` - Theme aggregator (`\input`s the problem files)
- `Ejercicios/Problemas/` - Individual exercise files
- `Ejercicios/Soluciones/` - Solution files (physically live here, but their `\input`
  wiring is centralized in the C6 Soluciones chapter — see below)
- `Figuras/` - Chapter-specific figures (manifest.json + images)

### Solutions Chapter (C6)

All worked solutions are consolidated into **`C6_Soluciones/`**, a dedicated chapter at the
end of the book, with **one `\section` per source chapter** (Cinemática, Cinética partícula,
Cinética sistemas, Cuerpo Rígido, Lagrangiana). The solution `.tex` files themselves stay in
each chapter's `Ejercicios/Soluciones/` folder; only the `\input` wiring lives in
`C6_Soluciones/C6_soluciones.tex`. The per-theme aggregators (`CN_E0Y_problemas.tex`) therefore
wire **problems only** — do NOT re-add inline "Soluciones" subsections to them.

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

### Solution Files
```
CN_E[YY]_solucion.tex
```
**Example**: `C1_E01_solucion.tex`

## Adding New Exercises

### Step 1: Create File
```
Contenidos/CX_[Name]/Ejercicios/Problemas/CX_E[YY]_P[ZZ]_titulo.tex
```

### Step 2: Use Standard Template
```latex
% =========================================================================
% Capítulo X - Tema YY - Problema ZZ
% =========================================================================
\subsubsection{Título descriptivo}

% Enunciado
[Problem statement with variables clearly defined]

\begin{enumerate}
    \item Question 1
    \item Question 2
\end{enumerate}

% Figura principal (si aplica)
\begin{figure}[!ht]
    \centering
    \begin{tikzpicture}[>=Latex, scale=1.5]
        
        % --- CONFIGURACIÓN DE PARÁMETROS ---
        \def\R{2.0}  % Parameter [units]
        
        % --- SOPORTES Y ELEMENTOS FIJOS ---
        % Fixed supports, walls, ground
        
        % --- GEOMETRÍA PRINCIPAL ---
        % Main bodies, discs, bars
        
        % --- SISTEMAS DE COORDENADAS ---
        % Axes, reference frames
        
        % --- PUNTOS Y COORDENADAS ---
        \coordinate (O) at (0,0);
        
        % --- VECTORES Y FUERZAS ---
        % Arrows, forces, velocities
        
        % --- ANOTACIONES Y ETIQUETAS ---
        % Angles, distances, text
        
    \end{tikzpicture}
    \caption{Clear, concise figure description (45-70 chars)}
    \label{fig:cx_eyy_pzz_titulo}
\end{figure}
```

### Step 3: Key Requirements for TikZ Figures
- **Parameters first**: Use `\def\PARAM{value}` at top for all dimensions
- **Organized comments**: Group related drawing code with `-- SECTION --` headers
- **Consistent scale**: Default `scale=1.5` (adjust as needed)
- **Colors**: Use predefined colors from `TikzDina.sty` (azul, gris1, myred)
- **Labels**: Always include `\caption{}` and unique `\label{fig:...}`

### Step 4: Create Solution
```
Contenidos/CX_[Name]/Ejercicios/Soluciones/CX_E[YY]_P[ZZ]_solucion.tex
```
```latex
\begin{sol}[Título descriptivo del problema]
\subsubsection*{Pregunta 1: ...}
[Step-by-step solution]
\end{sol}
```
Then wire it into the matching chapter section of
`Contenidos/C6_Soluciones/C6_soluciones.tex` (with a `\clearpage` after it), NOT into the
per-theme `CN_E0Y_problemas.tex` aggregator. The `sol` environment (defined in `Dinamica.sty`)
is a numbered `tcolorbox` that takes the title as an optional argument.

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
- **Environments**: tcolorbox for solutions (`\begin{sol}...\end{sol}`)
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
| C6 | Soluciones | Active | Consolidated solutions, 1 section/chapter |

**Solutions coverage**: Full worked solutions currently exist for C4 (P01–P10) and
C5 (P01–P08); partial for C1 (P13, P14) and C2 (P20 + a model solution). C3 has none yet.
All of these are wired through the C6 chapter.

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

1. **Wire C0 into main.tex**: C0 Repaso has exercises/solutions on disk but is not yet included.
2. **Expand solution coverage**: author solutions for C1 (beyond P13/P14), C2 and C3, and add
   their `\input` wiring to the matching section of `C6_Soluciones/C6_soluciones.tex`.
3. **Grow C4/C5**: continue adding rigid-body and Lagrangian problems as new `P[ZZ]` entries.
4. **Keep C6 in sync**: every new solution file must be wired into its chapter section in C6.

---

**Last Updated**: 2026-07-14 (Added C6 Soluciones chapter; imported non-duplicate Ayudantías
exercises into C2/C4/C5; consolidated all solution wiring into C6)
