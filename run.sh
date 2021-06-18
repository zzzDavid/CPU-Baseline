#!/bin/bash
for THREAD_NUM in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
    export OMP_NUM_THREADS=$THREAD_NUM
    python mbv1.py
done