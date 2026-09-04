#!/usr/bin/env python3
"""
Grafica tiempo real, speedup y eficiencia vs numero de hilos a partir de
CSV generados por bench_affinity.sh / bench_naive.sh.

Uso:
    python3 graficar_resultados.py resultados_cpu_affinity.csv
    python3 graficar_resultados.py resultados_cpu_affinity.csv resultados_cpu_naive.csv

Cada CSV debe tener encabezado: hilos,real_seg (hilos ordenados de 1 a N).
Por cada CSV genera 3 PNG: tiempo real, speedup y eficiencia.

Formulas:
    Speedup(n)   = T(1) / T(n)
    Eficiencia(n) = Speedup(n) / n
"""

import sys
import os
import csv
import matplotlib.pyplot as plt


def leer_csv(path):
    hilos, tiempos = [], []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            hilos.append(int(row["hilos"]))
            tiempos.append(float(row["real_seg"]))
    return hilos, tiempos


def calcular_speedup_eficiencia(hilos, tiempos):
    t1 = tiempos[0]  # tiempo con 1 hilo (baseline secuencial)
    speedup = [t1 / t for t in tiempos]
    eficiencia = [s / n for s, n in zip(speedup, hilos)]
    return speedup, eficiencia


def graficar_linea(hilos, valores, titulo, ylabel, salida, linea_ideal=None):
    plt.figure(figsize=(8, 5))
    plt.plot(hilos, valores, marker="o", linewidth=2, label="Medido")
    if linea_ideal is not None:
        plt.plot(hilos, linea_ideal, linestyle="--", color="gray", label="Ideal")
        plt.legend()
    plt.title(titulo)
    plt.xlabel("Número de hilos")
    plt.ylabel(ylabel)
    plt.xticks(hilos)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(salida, dpi=150)
    plt.close()
    print(f"Guardado: {salida}")


def procesar_csv(path):
    hilos, tiempos = leer_csv(path)
    nombre = os.path.splitext(os.path.basename(path))[0]
    speedup, eficiencia = calcular_speedup_eficiencia(hilos, tiempos)

    # Tiempo real
    graficar_linea(
        hilos, tiempos,
        f"Tiempo real vs número de hilos - {nombre}",
        "Tiempo real (s)",
        f"{nombre}_tiempo.png",
    )

    # Speedup (con linea ideal = speedup lineal, speedup(n) = n)
    graficar_linea(
        hilos, speedup,
        f"Speedup vs número de hilos - {nombre}",
        "Speedup (T1 / Tn)",
        f"{nombre}_speedup.png",
        linea_ideal=hilos,
    )

    # Eficiencia (con linea ideal = 1.0)
    graficar_linea(
        hilos, eficiencia,
        f"Eficiencia vs número de hilos - {nombre}",
        "Eficiencia (Speedup / hilos)",
        f"{nombre}_eficiencia.png",
        linea_ideal=[1.0] * len(hilos),
    )

    # Resumen en consola, util para el README de analisis
    print(f"\n--- {nombre} ---")
    print(f"{'hilos':>5} {'tiempo(s)':>10} {'speedup':>8} {'eficiencia':>10}")
    for n, t, s, e in zip(hilos, tiempos, speedup, eficiencia):
        print(f"{n:>5} {t:>10.2f} {s:>8.2f} {e:>10.2f}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 graficar_resultados.py archivo1.csv [archivo2.csv ...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        procesar_csv(path)