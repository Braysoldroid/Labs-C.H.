# Laboratorio: Vectorización SIMD (AVX2) vs. Implementación Escalar

## 1. Contexto general

- **Curso:** Computación Heterogénea
- **Laboratorio:** 2/Comprensión de instrucciones SIMD en el rendimiento de un programa
- **Estudiante:** Brayan Solís Rojas
- **Profesor:** Luis León Vega

### Objetivo

Comprender mediante el ejercicio práctico, los efectos de utilizar instrucciones vectoriales.

## 2. Metodología

- **Tamaño de las matrices:** `2048 x 2048` (`MATRIX_SIZE = 2048`, `VECTOR_SIZE = 2048`)
- **Repeticiones por ejecución:** `1`
- **Justificación de una sola corrida:** Se realizaron varias iteraciones de
  prueba antes de tomar el resultado final, y los tiempos obtenidos fueron
  consistentes entre ellas, por lo que se reporta el resultado de una única ejecución representativa en lugar de un promedio.
- **Compilador y flags:**
  - Escalar: `gcc -Wall -Wextra -O3`
  - AVX2: `gcc -Wall -Wextra -O3 -mavx2`
- **Entorno de ejecución:**
  - CPU: AMD Ryzen 7 5700U with Radeon Graphics (8 núcleos / 16 hilos, x86_64)
  - RAM: 14 GiB
  - Sistema operativo: Ubuntu 24.04.4 LTS

## 3. Resultados

| Versión | Tiempo (s) | Rendimiento (GFLOP/s) | Checksum | C[0][0] | C[1023][1023] |
|---|---|---|---|---|---|
| Escalar | [10.934819] | [1.571116] | [86972906452.000000] | [26800.500000] | [26836.500000] |
| AVX2 | [3.639731] | [4.720092] | [86972906452.000000] | [26800.500000] | [26836.500000] |

**Speedup obtenido:** `[tiempo_escalar / tiempo_avx2]` ≈ `[3.0x]`

## 4. Análisis del speedup

- **Speedup teórico máximo esperado:** `8x` (AVX2 procesa 8 floats de 32 bits
  por instrucción, frente a 1 float por instrucción en la versión escalar).
- **Speedup real obtenido:** `Aproximadamente 3x`
- **Discusión:** La ley de Amdahl dice que el speedup total está limitado por la fracción del programa que no se beneficia de la aceleracion. En el código de matmul_avx2.c hay funciones puramente escalares como por ejemplo, transpose_matrix_1024. Y, aunque simd_reduce_add_ps es código vectorizado, este se ejecuta a través de una cadena de dependiencias secuenciales que impiden el paralelismo pleno por latencia de instrucciones dependientes. Otro problema puede ser que el procesador espera datos de RAM, por lo que el tamaño de las matrices y de las caché de mi PC pueden generar limitantes aparte de las que indica Amdahl. 

**Repositorio completo:** https://github.com/Braysoldroid/Labs-C.H.
