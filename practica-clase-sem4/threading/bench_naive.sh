#!/bin/bash
echo "hilos,real_seg" > resultados_cpu_naive.csv
for n in $(seq 1 16); do
    t=$( { /usr/bin/time -f "%e" ./cpu-naive $n > /dev/null; } 2>&1 )
    echo "$n,$t" >> resultados_cpu_naive.csv
    echo "Hilos: $n -> $t s"
done
