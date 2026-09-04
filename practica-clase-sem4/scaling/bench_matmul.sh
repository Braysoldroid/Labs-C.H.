#!/bin/bash
# Uso: ./bench_matmul.sh
# Ejecuta ./matmul_tiled_openmp con hilos de 1 a 16, deja tamano matriz/tile/repeticiones por defecto.

BIN=./matmul_tiled_openmp
MATRIX_SIZE=512
TILE_SIZE=32
REPETICIONES=10

echo "hilos,real_seg" > resultados_matmul_tiled.csv

for n in $(seq 1 16); do
    salida=$("$BIN" "$n" "$MATRIX_SIZE" "$TILE_SIZE" "$REPETICIONES")
    t=$(echo "$salida" | grep "Tiempo:" | awk '{print $2}')
    echo "$n,$t" >> resultados_matmul_tiled.csv
    echo "Hilos: $n -> $t s"
done