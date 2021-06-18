#!/bin/bash
for ((CORE_NUM=1; CORE_NUM<=20; CORE_NUM++))
do
    export MKL_NUM_THREADS=$CORE_NUM
    taskset -c 1-$CORE_NUM python mbv1.py
done
