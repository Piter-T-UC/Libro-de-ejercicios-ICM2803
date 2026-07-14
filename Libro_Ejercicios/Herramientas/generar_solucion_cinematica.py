#!/usr/bin/env python3
"""
Genera un archivo de solución .tex (cinemática de una partícula) a partir del
vector de posición del problema.

Calcula velocidad y aceleración por derivación simbólica (sympy) en
coordenadas cartesianas o cilíndricas/polares, y escribe el resultado en el
formato usado por el libro (ver Contenidos/C1_Cinematica/Ejercicios/Soluciones/
C1_E01_P04_solucion.tex como referencia de estilo).

Requiere: sympy (pip install sympy)

Ejemplos de uso
----------------

Coordenadas cilíndricas, con velocidad angular constante Omega y radio
r(t) = r0 + v*t (igual al ejemplo de estilo del libro):

    python3 generar_solucion_cinematica.py \
        --sistema cilindrico \
        --r "r0 + v*t" --theta "Omega*t" --z 0 \
        --capitulo C1 --tema E01 --problema P20 \
        --titulo "Disco Rotante con Punto en Movimiento Radial" \
        --out Contenidos/C1_Cinematica/Ejercicios/Soluciones/C1_E01_P20_solucion.tex

Coordenadas cartesianas:

    python3 generar_solucion_cinematica.py \
        --sistema cartesiano \
        --x "R*cos(Omega*t)" --y "R*sin(Omega*t)" --z "0" \
        --capitulo C1 --tema E02 --problema P05 \
        --titulo "Partícula en Trayectoria Circular" \
        --out Contenidos/C1_Cinematica/Ejercicios/Soluciones/C1_E02_P05_solucion.tex

También se puede usar como librería:

    from generar_solucion_cinematica import calcular_cilindrico, render_tex
    resultado = calcular_cilindrico("r0 + v*t", "Omega*t", "0")
    tex = render_tex(resultado, capitulo="C1", tema="E01", problema="P20",
                      titulo="...", sistema="cilindrico")
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field

import sympy as sp

t = sp.symbols("t", real=True)


@dataclass
class ResultadoCinematico:
    sistema: str
    # Posición, velocidad, aceleración expresadas por componente
    pos: dict = field(default_factory=dict)
    vel: dict = field(default_factory=dict)
    acc: dict = field(default_factory=dict)
    vel_mag: sp.Expr = None
    acc_mag: sp.Expr = None


def _sympify(expr_str: str) -> sp.Expr:
    """Convierte un string a expresión sympy, con 't' ya declarado como símbolo."""
    return sp.sympify(expr_str, locals={"t": t})


def _simplify(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand(expr))


def calcular_cartesiano(x_str: str, y_str: str, z_str: str) -> ResultadoCinematico:
    """Deriva la posición r(t) = x(t) i + y(t) j + z(t) k dos veces respecto a t."""
    x, y, z = _sympify(x_str), _sympify(y_str), _sympify(z_str)

    vx, vy, vz = (sp.diff(c, t) for c in (x, y, z))
    ax, ay, az = (sp.diff(c, t, 2) for c in (x, y, z))

    vx, vy, vz = (_simplify(c) for c in (vx, vy, vz))
    ax, ay, az = (_simplify(c) for c in (ax, ay, az))

    res = ResultadoCinematico(sistema="cartesiano")
    res.pos = {"x": x, "y": y, "z": z}
    res.vel = {"x": vx, "y": vy, "z": vz}
    res.acc = {"x": ax, "y": ay, "z": az}
    res.vel_mag = _simplify(sp.sqrt(vx**2 + vy**2 + vz**2))
    res.acc_mag = _simplify(sp.sqrt(ax**2 + ay**2 + az**2))
    return res


def calcular_cilindrico(r_str: str, theta_str: str, z_str: str) -> ResultadoCinematico:
    """
    Deriva la posición r(t) = r(t) e_r + z(t) e_z usando las fórmulas estándar
    de cinemática en coordenadas cilíndricas:

        v = rdot e_r + r*thetadot e_theta + zdot e_z
        a = (rddot - r*thetadot^2) e_r + (r*thetaddot + 2*rdot*thetadot) e_theta + zddot e_z
    """
    r, theta, z = _sympify(r_str), _sympify(theta_str), _sympify(z_str)

    rdot = sp.diff(r, t)
    rddot = sp.diff(r, t, 2)
    thetadot = sp.diff(theta, t)
    thetaddot = sp.diff(theta, t, 2)
    zdot = sp.diff(z, t)
    zddot = sp.diff(z, t, 2)

    v_r = _simplify(rdot)
    v_theta = _simplify(r * thetadot)
    v_z = _simplify(zdot)

    a_r = _simplify(rddot - r * thetadot**2)
    a_theta = _simplify(r * thetaddot + 2 * rdot * thetadot)
    a_z = _simplify(zddot)

    res = ResultadoCinematico(sistema="cilindrico")
    res.pos = {"r": r, "theta": theta, "z": z}
    res.vel = {"r": v_r, "theta": v_theta, "z": v_z}
    res.acc = {"r": a_r, "theta": a_theta, "z": a_z}
    res.vel_mag = _simplify(sp.sqrt(v_r**2 + v_theta**2 + v_z**2))
    res.acc_mag = _simplify(sp.sqrt(a_r**2 + a_theta**2 + a_z**2))
    return res


def _tex(expr: sp.Expr) -> str:
    return sp.latex(sp.nsimplify(expr) if expr.free_symbols else expr)


def _vector_tex(comp: dict, ejes: tuple[str, str, str]) -> str:
    """Arma 'a e1 + b e2 + c e3' omitiendo componentes nulas."""
    keys = list(comp.keys())
    terminos = []
    for k, eje in zip(keys, ejes):
        val = comp[k]
        if val == 0:
            continue
        terminos.append(f"({_tex(val)}) \\, {eje}")
    if not terminos:
        return "\\vec{0}"
    return " + ".join(terminos)


def render_tex(res: ResultadoCinematico, capitulo: str, tema: str, problema: str,
               titulo: str) -> str:
    if res.sistema == "cartesiano":
        ejes = (r"\hat{e}_x", r"\hat{e}_y", r"\hat{e}_z")
        pos_line = r"\vec{r} = " + _vector_tex(res.pos, ejes)
        formula_v = r"\vec{v} = \dot{x} \, \hat{e}_x + \dot{y} \, \hat{e}_y + \dot{z} \, \hat{e}_z"
        formula_a = r"\vec{a} = \ddot{x} \, \hat{e}_x + \ddot{y} \, \hat{e}_y + \ddot{z} \, \hat{e}_z"
        comp_labels = [("x", "componente en x"), ("y", "componente en y"), ("z", "componente en z")]
    else:
        ejes = (r"\hat{e}_r", r"\hat{e}_\theta", r"\hat{e}_z")
        pos_line = r"\vec{r} = r(t) \, \hat{e}_r + z(t) \, \hat{e}_z"
        formula_v = r"\vec{v} = \dot{r} \, \hat{e}_r + r \dot{\theta} \, \hat{e}_\theta + \dot{z} \, \hat{e}_z"
        formula_a = (
            r"\vec{a} = (\ddot{r} - r\dot{\theta}^2) \hat{e}_r "
            r"+ (r\ddot{\theta} + 2\dot{r}\dot{\theta}) \hat{e}_\theta + \ddot{z} \, \hat{e}_z"
        )
        comp_labels = [("r", "componente radial"), ("theta", "componente transversal"), ("z", "componente axial")]

    v_vec = _vector_tex(res.vel, ejes)
    a_vec = _vector_tex(res.acc, ejes)

    # Subíndices reales en LaTeX para v_r, v_theta, v_z / a_r, a_theta, a_z.
    def _sub(base: str, k: str) -> str:
        sub = "\\theta" if k == "theta" else k
        return f"{base}_{{{sub}}}"

    interp_v_items = "\n".join(
        f"    \\item \\textbf{{{label.capitalize()}}}: ${_sub('v', k)} = {_tex(res.vel[k])}$"
        for k, label in comp_labels
    )
    interp_a_items = "\n".join(
        f"    \\item \\textbf{{{label.capitalize()}}}: ${_sub('a', k)} = {_tex(res.acc[k])}$"
        for k, label in comp_labels
    )

    contenido = f"""% =========================================================================
% Solución: {capitulo}_{tema}_{problema} - {titulo}
% =========================================================================

\\begin{{sol}}[Tema: {titulo}]

\\subsubsection*{{Pregunta 1: Velocidad de la partícula}}

La posición de la partícula es:
$${pos_line}$$

La velocidad se obtiene derivando respecto al tiempo:
$${formula_v}$$

Sustituyendo nuestras funciones:
\\begin{{equation}}
\\boxed{{\\vec{{v}} = {v_vec}}}
\\end{{equation}}

Interpretación:
\\begin{{itemize}}
{interp_v_items}
    \\item \\textbf{{Magnitud de velocidad}}: $|\\vec{{v}}| = {_tex(res.vel_mag)}$
\\end{{itemize}}

\\subsubsection*{{Pregunta 2: Aceleración de la partícula}}

La aceleración se obtiene derivando la velocidad respecto al tiempo:
$${formula_a}$$

Sustituyendo nuestras funciones:
\\begin{{equation}}
\\boxed{{\\vec{{a}} = {a_vec}}}
\\end{{equation}}

Interpretación:
\\begin{{itemize}}
{interp_a_items}
    \\item \\textbf{{Magnitud de aceleración}}: $|\\vec{{a}}| = {_tex(res.acc_mag)}$
\\end{{itemize}}

\\end{{sol}}
"""
    return contenido


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sistema", choices=["cartesiano", "cilindrico"], required=True,
                         help="Sistema de coordenadas del vector de posición dado.")
    parser.add_argument("--x", help="Componente x(t) [cartesiano]")
    parser.add_argument("--y", help="Componente y(t) [cartesiano]")
    parser.add_argument("--z", default="0", help="Componente z(t) (ambos sistemas, default 0)")
    parser.add_argument("--r", help="Componente radial r(t) [cilíndrico]")
    parser.add_argument("--theta", help="Ángulo theta(t) [cilíndrico]. Para velocidad angular "
                                         "constante Omega usar, por ejemplo, 'Omega*t'.")

    parser.add_argument("--capitulo", required=True, help="Ej: C1")
    parser.add_argument("--tema", required=True, help="Ej: E01")
    parser.add_argument("--problema", required=True, help="Ej: P20")
    parser.add_argument("--titulo", required=True, help="Título descriptivo del problema")
    parser.add_argument("--out", help="Ruta de salida .tex. Si se omite, imprime a stdout.")

    args = parser.parse_args(argv)

    if args.sistema == "cartesiano":
        if not (args.x and args.y):
            parser.error("--sistema cartesiano requiere --x y --y (y opcionalmente --z)")
        resultado = calcular_cartesiano(args.x, args.y, args.z)
    else:
        if not (args.r and args.theta):
            parser.error("--sistema cilindrico requiere --r y --theta (y opcionalmente --z)")
        resultado = calcular_cilindrico(args.r, args.theta, args.z)

    tex = render_tex(resultado, args.capitulo, args.tema, args.problema, args.titulo)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(tex)
        print(f"Solución escrita en: {args.out}")
    else:
        print(tex)

    return 0


if __name__ == "__main__":
    sys.exit(main())
