# Libro de Ejercicios - Dinámica de Sistemas Mecánicos

Libro LaTeX con ejercicios y soluciones para el curso ICM2803: Dinámica de Sistemas Mecánicos.
Contiene teoría, ejercicios resueltos y figuras TikZ de alta calidad.

## 📚 Contenidos

- **Capítulo 0**: Repaso - Álgebra Vectorial y Cálculo Vectorial
- **Capítulo 1**: Cinemática - Sistemas de coordenadas y movimiento
- **Capítulo 2**: Cinética 1 - Dinámica de sistemas de partículas (Parte 1)
- **Capítulo 3**: Cinética 2 - Dinámica de sistemas de partículas (Parte 2)
- **Capítulo 4**: Cuerpos Rígidos - Rotación y movimiento de cuerpos rígidos
- **Capítulo 5**: Mecánica Lagrangiana - Formulación Lagrangiana

## 🚀 Compilación Rápida

### Requisitos
- **LaTeX** (TeX Live, MiKTeX o MacTeX - 2020 o superior)
- **latexmk** (incluido en la mayoría de distribuciones)

### Compilar PDF

```bash
# Opción 1: Usando Make (recomendado)
make pdf

# Opción 2: Usando latexmk directamente
latexmk -pdf main.tex

# Opción 3: Limpiar y recompilar
make clean-all
make pdf
```

### Resultado
El PDF se genera en: `Build/main.pdf`

## 📁 Estructura de Directorios

```
Libro_Ejercicios/
├── main.tex                    # Archivo maestro
├── Makefile                    # Compilación automatizada
├── .latexmkrc                  # Configuración de LaTeX
├── .gitignore
├── README.md
├── Paquetes/
│   ├── Dinamica.sty           # Estilos, colores, entornos
│   └── TikzDina.sty           # Comandos TikZ
├── Contenidos/
│   ├── C0_Repaso/             # Capítulo 0
│   ├── C1_Cinematica/         # Capítulo 1
│   ├── C2_Cinetica1/          # Capítulo 2
│   ├── C3_Cinetica2/          # Capítulo 3
│   ├── C4_CuerposRigidos/     # Capítulo 4
│   ├── C5_MecanicaLagrangiana/# Capítulo 5
│   └── Figuras/               # Figuras globales
├── Build/                     # Salida de compilación (generado)
│   └── main.pdf
└── Tools/                     # Scripts auxiliares
```

## 📝 Estructura de Cada Capítulo

```
CN_NombreCapitulo/
├── CN_00_introduccion.tex     # Introducción y conceptos clave
├── CN_0X_tema.tex            # Teoría de cada tema (si es necesario)
├── Ejercicios/
│   ├── Problemas/
│   │   ├── CN_E01_problema_01.tex
│   │   ├── CN_E01_problema_02.tex
│   │   └── ... (problemas agrupados por tema)
│   └── Soluciones/
│       ├── CN_E01_solucion.tex
│       └── ...
├── Figuras/
│   ├── CN_F01_descripcion.tikz.tex
│   └── manifest.json          # Registro de figuras
```

## 🎨 Convención de Nombres

### Archivos de Capítulo
- `CN_00_introduccion.tex` - Introducción del capítulo N
- `CN_0X_tema.tex` - Secciones teóricas

### Ejercicios y Problemas
- `CN_E[YY]_P[ZZ]_titulo.tex` - Ejercicio del tema YY, problema ZZ
  - Ejemplo: `C1_E01_P03_hormiga_velocista.tex`

### Soluciones
- `CN_E[YY]_solucion.tex` - Soluciones del tema YY
  - Ejemplo: `C1_E01_solucion.tex`

### Figuras
- `CN_FYY_descripcion.tikz.tex` - Figura YY (TikZ)
- `CN_FYY_descripcion.png` - Figura YY (rasterizada)

## 💡 Cómo Agregar un Nuevo Ejercicio

### 1. Crear el archivo
```
Contenidos/C[X]_[Nombre]/Ejercicios/Problemas/
    └── C[X]_E[YY]_P[ZZ]_titulo.tex
```

### 2. Estructura básica
```latex
% =========================================================================
% Capítulo X - Tema YY - Problema ZZ
% =========================================================================
\subsubsection{Título descriptivo}

% Enunciado del problema
[Texto del problema]

\begin{enumerate}
    \item Primera pregunta
    \item Segunda pregunta
\end{enumerate}

% Figura (si aplica)
\begin{figure}[!ht]
    \centering
    \begin{tikzpicture}[>=Latex, scale=1.5]
        % TikZ code aquí
    \end{tikzpicture}
    \caption{Descripción de la figura}
    \label{fig:c[x]_e[yy]_p[zz]_titulo}
\end{figure}
```

### 3. Agregar a contenedor de tema
Editar: `Contenidos/C[X]_[Nombre]/Ejercicios/C[X]_E[YY]_problemas.tex`
```latex
\input{Contenidos/C[X]_[Nombre]/Ejercicios/Problemas/C[X]_E[YY]_P[ZZ]_titulo.tex}
```

## 🔧 Comandos Disponibles (Makefile)

```bash
make pdf       # Compilar PDF
make clean     # Limpiar archivos auxiliares
make clean-all # Limpiar todo incluyendo PDF
make help      # Mostrar esta ayuda
```

## 🎨 Personalización

### Colores
Editar `Paquetes/TikzDina.sty` para cambiar:
```latex
\definecolor{azul}{RGB}{0,160,255}
\definecolor{azul2}{RGB}{7,74,163}
\definecolor{gris1}{RGB}{44, 62, 80}
\definecolor{myred}{RGB}{191, 0, 0}
```

### Márgenes y Geometría
Editar `main.tex`:
```latex
\geometry{left=2.5cm, right=2cm, top=2.5cm, bottom=2.5cm}
```

## 🐛 Solución de Problemas

### "File not found" al compilar
- Verificar que las rutas en `main.tex` usen guiones bajos (_) no espacios
- Verificar que no hay dos puntos (:) en las rutas
- Ejecutar: `make clean-all && make pdf`

### Figuras TikZ no se renderizan
- Validar sintaxis de `\begin{tikzpicture}...\end{tikzpicture}`
- Verificar que los parámetros `\def` están correctamente definidos
- Revisar compilación en primer pase: `pdflatex -interaction=nonstopmode main.tex`

### Referencias cruzadas muestran "???"
- Compilar dos veces: LaTeX necesita dos pasadas para referencias
- Comando: `make clean && make pdf`

## 📖 Contribuir

Ver `CONTRIBUTING.md` para guía de estilos y cómo agregar ejercicios.

## 📋 Historial de Versiones

- **v1.0.0** (2026-07-12) - Estructura estandarizada y reorganización completa

## 📧 Información

**Autor**: Pedro Taboada  
**Curso**: ICM2803 - Dinámica de Sistemas Mecánicos  
**Institución**: Pontificia Universidad Católica de Chile  
**Última actualización**: 2026-07-12

---

**Nota**: Este libro está en desarrollo activo. Los cambios se registran en el historial de Git.
