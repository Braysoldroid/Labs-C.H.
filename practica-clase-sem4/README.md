# Semana 4 — Lab Individual Brayan Solís Rojas

## Detalles del equipo de pruebas

| Componente | Detalle |
|---|---|
| CPU | AMD Ryzen 7 5700U with Radeon Graphics |
| Núcleos físicos | 8 |
| Hilos lógicos (SMT/hyperthreading) | 16 (2 hilos por núcleo) |
| Caché L1d / L1i | 256 KiB (8 instancias c/u) |
| Caché L2 | 4 MiB (8 instancias) |
| Caché L3 | 8 MiB (2 instancias) |
| Frecuencia máx. | 4373.86 MHz |
| Arquitectura | x86_64, AuthenticAMD |
| NUMA | 1 nodo (0-15) |

---

## Práctica Clase 3

### Ejercicio A — cpu-affinity vs cpu-naive (`threading/`)

#### Resultados — cpu-affinity

| Hilos | Tiempo real (s) | Speedup (T1/Tn) | Eficiencia (Speedup/n) |
|------:|-----------------:|-----------------:|------------------------:|
| 1     | 4.93              | 1.00              | 1.00                    |
| 2     | 4.89              | 1.01              | 0.50                    |
| 3     | 2.65              | 1.86              | 0.62                    |
| 4     | 2.63              | 1.87              | 0.47                    |
| 5     | 2.78              | 1.77              | 0.35                    |
| 6     | 3.20              | 1.54              | 0.26                    |
| 7     | 3.82              | 1.29              | 0.18                    |
| 8     | 4.39              | 1.12              | 0.14                    |
| 9     | 4.91              | 1.00              | 0.11                    |
| 10    | 5.43              | 0.91              | 0.09                    |
| 11    | 5.97              | 0.83              | 0.08                    |
| 12    | 6.55              | 0.75              | 0.06                    |
| 13    | 7.17              | 0.69              | 0.05                    |
| 14    | 7.60              | 0.65              | 0.05                    |
| 15    | 8.25              | 0.60              | 0.04                    |
| 16    | 9.00              | 0.55              | 0.03                    |

#### Resultados — cpu-naive

| Hilos | Tiempo real (s) | Speedup (T1/Tn) | Eficiencia (Speedup/n) |
|------:|-----------------:|-----------------:|------------------------:|
| 1     | 4.93              | 1.00              | 1.00                    |
| 2     | 5.06              | 0.97              | 0.49                    |
| 3     | 2.85              | 1.73              | 0.58                    |
| 4     | 2.93              | 1.68              | 0.42                    |
| 5     | 3.22              | 1.53              | 0.31                    |
| 6     | 3.71              | 1.33              | 0.22                    |
| 7     | 4.40              | 1.12              | 0.16                    |
| 8     | 5.01              | 0.98              | 0.12                    |
| 9     | 5.93              | 0.83              | 0.09                    |
| 10    | 6.51              | 0.76              | 0.08                    |
| 11    | 7.31              | 0.67              | 0.06                    |
| 12    | 7.83              | 0.63              | 0.05                    |
| 13    | 8.43              | 0.58              | 0.04                    |
| 14    | 9.08              | 0.54              | 0.04                    |
| 15    | 10.06             | 0.49              | 0.03                    |
| 16    | 10.76             | 0.46              | 0.03                    |

---

### Ejercicio B — matmul tiled / softmax OpenMP (`scaling/`)

#### Resultados — matmul tiled OpenMP

| Hilos | Tiempo (s) | Speedup | Eficiencia |
|------:|-----------:|--------:|-----------:|
| 1  | 1.369504 | 1.00 | 1.00 |
| 2  | 0.676755 | 2.02 | 1.01 |
| 3  | 0.456194 | 3.00 | 1.00 |
| 4  | 0.339113 | 4.04 | 1.01 |
| 5  | 0.275652 | 4.97 | 0.99 |
| 6  | 0.228815 | 5.99 | 0.99 |
| 7  | 0.200951 | 6.82 | 0.97 |
| 8  | 0.176029 | 7.78 | 0.97 |
| 9  | 0.296667 | 4.62 | 0.51 |
| 10 | 0.267693 | 5.12 | 0.51 |
| 11 | 0.248306 | 5.51 | 0.50 |
| 12 | 0.226728 | 6.04 | 0.50 |
| 13 | 0.209442 | 6.54 | 0.50 |
| 14 | 0.197656 | 6.93 | 0.49 |
| 15 | 0.183910 | 7.45 | 0.50 |
| 16 | 0.224813 | 6.09 | 0.38 |

#### Resultados — softmax OpenMP

| Hilos | Tiempo (s) | Speedup | Eficiencia |
|------:|-----------:|--------:|-----------:|
| 1  | 1.436424 | 1.00 | 1.00 |
| 2  | 1.239501 | 1.16 | 0.58 |
| 3  | 0.954119 | 1.51 | 0.50 |
| 4  | 0.695129 | 2.07 | 0.52 |
| 5  | 0.561642 | 2.56 | 0.51 |
| 6  | 0.580265 | 2.48 | 0.41 |
| 7  | 0.583345 | 2.46 | 0.35 |
| 8  | 0.563145 | 2.55 | 0.32 |
| 9  | 0.692999 | 2.07 | 0.23 |
| 10 | 0.737819 | 1.95 | 0.19 |
| 11 | 0.773436 | 1.86 | 0.17 |
| 12 | 0.812192 | 1.77 | 0.15 |
| 13 | 0.815802 | 1.76 | 0.14 |
| 14 | 0.843992 | 1.70 | 0.12 |
| 15 | 0.925473 | 1.52 | 0.10 |
| 16 | 1.008894 | 1.42 | 0.09 |

---

## Práctica Clase 4

### Ejercicio A — Biblioteca estática (`libraries/`)

### Ejercicio B — Biblioteca dinámica (`libraries/`)

### Ejercicio C — Funciones static inline (`libraries/`)

## Resumen comparativo estático / dinámico / inline

## Conclusiones generales

`[completar]`