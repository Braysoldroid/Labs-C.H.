#!/bin/bash
# Uso: ./bench_softmax.sh
# Ejecuta ./softmax_openmp con hilos de 1 a 16, deja repeticiones por defecto.

BIN=./softmax_openmp
REPETICIONES=100000

echo "hilos,real_seg" > resultados_softmax.csv

for n in $(seq 1 16); do
    salida=$("$BIN" "$n" "$REPETICIONES")
    t=$(echo "$salida" | grep "Tiempo:" | awk '{print $2}')
    echo "$n,$t" >> resultados_softmax.csv
    echo "Hilos: $n -> $t s"
done