# Guía de Contribución

Gracias por tu interés en contribuir al Libro de Ejercicios. Esta guía te ayudará a mantener la consistencia y calidad del proyecto.

## 📋 Antes de Empezar

1. Asegúrate de que tu LaTeX compila correctamente
2. Familiarízate con la estructura actual del proyecto
3. Revisa los ejemplos de ejercicios existentes (especialmente `C1_E01_P01_hormiga_velocista.tex`)

## 🎯 Estándares de Código

### Nomenclatura de Archivos

**Archivos de Capítulo:**
```
CX_00_introduccion.tex          # Introducción
CX_0Y_tema.tex                  # Secciones teóricas
```

**Archivos de Ejercicios:**
```
CX_E[YY]_P[ZZ]_titulo.tex
  ↑    ↑     ↑     ↑
  |    |     |     └─ Nombre descriptivo (snake_case)
  |    |     └─────── Número de problema (01, 02, 03, ...)
  |    └───────────── Número de tema (01, 02, 03, ...)
  └────────────────── Capítulo (C0, C1, C2, ...)

Ejemplo: C1_E01_P02_barra_articulada.tex
```

**Archivos de Solución:**
```
CX_E[YY]_solucion.tex

Ejemplo: C1_E01_solucion.tex
```

### Estructura de Archivo de Ejercicio

```latex
% =========================================================================
% Capítulo X: [Nombre del Capítulo]
% Tema YY: [Nombre del Tema]
% Problema ZZ: [Nombre Descriptivo]
% =========================================================================
% Archivo: CX_E[YY]_P[ZZ]_nombre.tex
% Autor: [Tu nombre]
% Fecha: YYYY-MM-DD
% =========================================================================

\subsubsection{Nombre descriptivo del problema}

% --- ENUNCIADO DEL PROBLEMA ---
Descripción clara del problema. Usa variables bien definidas.
[Puedes usar una o dos oraciones para contexto]

\begin{enumerate}
    \item Pregunta o sub-problema 1
    \item Pregunta o sub-problema 2
    \item Pregunta o sub-problema 3
\end{enumerate}

% --- FIGURA PRINCIPAL (si aplica) ---
\begin{figure}[!ht]
    \centering
    \begin{tikzpicture}[>=Latex, scale=1.5]
        
        % --- CONFIGURACIÓN DE PARÁMETROS ---
        \def\R{2.0}      % Radio del círculo [cm]
        \def\L{1.8}      % Longitud de barra [cm]
        \def\Theta{40}   % Ángulo theta [grados]
        
        % --- SOPORTES Y ELEMENTOS FIJOS ---
        % Suelo, paredes, puntos de apoyo no movibles
        
        % --- GEOMETRÍA PRINCIPAL ---
        % Cuerpos rígidos, discos, barras
        
        % --- SISTEMAS DE COORDENADAS ---
        % Ejes, referencias de marcos
        
        % --- PUNTOS Y COORDENADAS ---
        \coordinate (O) at (0,0);
        \filldraw (O) circle (1.2pt) node[left] {$O$};
        
        % --- VECTORES Y FUERZAS ---
        % Flechas, magnitudes, velocidades
        
        % --- ANOTACIONES Y ETIQUETAS ---
        % Ángulos, distancias, textos
        
    \end{tikzpicture}
    \caption{Descripción clara de la figura (máx 70 caracteres)}
    \label{fig:cx_eyy_pzz_titulo}
\end{figure}

% --- NOTAS ADICIONALES (opcional) ---
% Comentarios sobre simplificaciones, hipótesis especiales, etc.
```

### Reglas para Figuras TikZ

**✅ OBLIGATORIO:**

1. **Parámetros al inicio** con `\def`:
   ```latex
   \def\R{2.0}      % Radio [unidades]
   \def\L{1.8}      % Longitud [unidades]
   ```

2. **Comentarios organizados**:
   ```latex
   % --- CONFIGURACIÓN ---
   % --- SOPORTES ---
   % --- GEOMETRÍA PRINCIPAL ---
   % --- COORDENADAS ---
   % --- VECTORES ---
   % --- ETIQUETAS ---
   ```

3. **Escala consistente**: `scale=1.5` (por defecto, ajustable según necesidad)

4. **Tamaño de puntos**: `circle (1.2pt)` para normales, `circle (2.5pt)` para principales

5. **Colores definidos en TikzDina.sty**:
   ```latex
   \definecolor{azul}{RGB}{0,160,255}
   \definecolor{azul2}{RGB}{7,74,163}
   \definecolor{gris1}{RGB}{44, 62, 80}
   \definecolor{myred}{RGB}{191, 0, 0}
   ```

6. **Caption y Label**:
   ```latex
   \caption{Descripción clara (45-70 caracteres)}
   \label{fig:cx_eyy_pzz_titulo}
   ```

**❌ NO HAGAS:**
- Figuras en archivos separados (usar inline)
- Parámetros sin `\def` al inicio
- Comentarios desorganizados
- Escalas inconsistentes
- Colores RGB personalizados (usar los definidos)

### Matemáticas

**Inline:**
```latex
La velocidad angular es $\omega = \dot{\theta}$
```

**Ecuaciones importantes:**
```latex
\begin{equation}
    \vec{v} = \vec{\omega} \times \vec{r}
    \label{eq:velocidad_angular}
\end{equation}
```

**Usar comandos personalizados** (definidos en Dinamica.sty):
```latex
\vec{a}              % Vector
\der{v}{t}           % Derivada
\transport{e}{A}     % Transporte de frame
\angvel              % Símbolo velocidad angular
```

## 🚀 Proceso de Contribución

### 1. Crear una rama para tu trabajo
```bash
git checkout -b feature/agregar-ejercicio-c1-tema-03
```

### 2. Agregar tu ejercicio

```bash
# Crear archivo
touch Contenidos/C1_Cinematica/Ejercicios/Problemas/C1_E03_P05_nuevo_problema.tex

# Editar y agregar contenido siguiendo plantilla
```

### 3. Actualizar archivos contenedores

Si es un nuevo tema, crear:
```
Contenidos/C[X]_[Nombre]/Ejercicios/C[X]_E[YY]_problemas.tex
```

Si es un tema existente, editar:
```latex
\input{Contenidos/C[X]_[Nombre]/Ejercicios/Problemas/C[X]_E[YY]_P[ZZ]_titulo.tex}
```

### 4. Crear archivo de solución

```bash
touch Contenidos/C[X]_[Nombre]/Ejercicios/Soluciones/C[X]_E[YY]_solucion.tex
```

Estructura:
```latex
\begin{sol}[Tema: Nombre del Tema]

\subsubsection*{Problema ZZ: Título}

% Solución paso a paso
\begin{equation}
    % Ecuaciones clave
\end{equation}

% Explicación de pasos

\end{sol}
```

### 5. Compilar y verificar

```bash
make clean-all
make pdf

# Revisar Build/main.pdf
# Verificar que:
# - PDF compila sin errores
# - Figuras TikZ se renderizan correctamente
# - Referencias están correctas (no "???")
# - Estilos visuales son consistentes
```

### 6. Agregar cambios a Git

```bash
git add Contenidos/C[X]_[Nombre]/Ejercicios/Problemas/
git add Contenidos/C[X]_[Nombre]/Ejercicios/Soluciones/
git add main.tex  # si es necesario actualizar rutas
```

### 7. Commit descriptivo

```bash
git commit -m "[TIPO] Descripción breve (máx 72 caracteres)

Descripción más detallada si es necesario.

- Línea 1
- Línea 2"
```

**Tipos de commits:**
- `[feat]` - Nuevo ejercicio o sección
- `[fix]` - Corrección de errores
- `[refactor]` - Reorganización de estructura
- `[docs]` - Documentación
- `[style]` - Cambios de formato (sin cambiar lógica)

### 8. Hacer Push

```bash
git push origin feature/agregar-ejercicio-c1-tema-03
```

### 9. Crear Pull Request

En GitHub, crear PR con descripción clara de:
- Qué ejercicios se agregan
- Qué tema cubren
- Nivel de dificultad
- Cualquier comentario importante

## ✅ Checklist Antes de Enviar

- [ ] El archivo `.tex` sigue la convención de nombres
- [ ] El archivo tiene encabezado comentado completo
- [ ] El ejercicio tiene `\subsubsection{...}`
- [ ] El ejercicio tiene al menos un `\enumerate` con preguntas
- [ ] Si hay figura TikZ:
  - [ ] Tiene parámetros `\def` al inicio
  - [ ] Tiene comentarios agrupados (`-- SECCIÓN --`)
  - [ ] Tiene `\caption` y `\label` únicos
  - [ ] Se renderiza correctamente
- [ ] La solución está en archivo `CX_E[YY]_solucion.tex`
- [ ] El PDF compila sin errores
- [ ] No hay referencias cruzadas rotas ("???")
- [ ] Los nombres y estilos son consistentes con ejemplos existentes

## 📊 Ejemplo Completo

Ver archivo: `Contenidos/C1_Cinematica/Ejercicios/Problemas/C1_E01_P03_hormiga_velocista.tex`

Este es el estándar de referencia. Si tus ejercicios se parecen a éste, vas bien.

## 🎨 Preservar la Energía

El proyecto tiene un estilo visual muy específico:
- Figuras claras y bien etiquetadas
- Parámetros explícitos
- Comentarios organizados
- Colores consistentes

**Mantén este estilo** al agregar nuevos ejercicios. Es lo que hace único este libro.

## 📚 Recursos

- **LaTeX Basics**: https://www.overleaf.com/learn
- **TikZ Manual**: https://tikz.dev/
- **Physics Package**: https://ctan.org/pkg/physics
- **IEEE Math**: https://tug.org/TUGboat/tb30-1/tb94vieth.pdf

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar figuras PNG en lugar de TikZ?**  
R: Prefiere TikZ, pero PNG es aceptable para fotografías o escaneos. Actualiza `manifest.json` del capítulo.

**P: ¿Cuántos ejercicios debo agregar por tema?**  
R: Sin límite específico, pero 3-10 ejercicios por tema es típico. Mantén coherencia temática.

**P: ¿Qué pasa si mi solución es muy larga?**  
R: Puedes dividirla en múltiples subproblemas o crear referencias a pasos intermedios.

**P: ¿Cómo agrego un nuevo tema (E[YY])?**  
R: Crea nuevo `C[X]_E[YY]_01.tex` y crea archivo contenedor `C[X]_E[YY]_problemas.tex`.

---

**¡Gracias por contribuir!** 🎉
