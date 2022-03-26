# CPU-Baseline

Test MobileNet-V1 latency on different number of CPU cores, see when it becomes communication-bound.

## CPU Info
```bash
$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                40
On-line CPU(s) list:   0-39
Thread(s) per core:    2
Core(s) per socket:    10
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 85
Model name:            Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz
Stepping:              4
CPU MHz:               1000.938
CPU max MHz:           2401.0000
CPU min MHz:           1000.0000
BogoMIPS:              4802.02
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              1024K
L3 cache:              14080K
NUMA node0 CPU(s):     0-9,20-29
NUMA node1 CPU(s):     10-19,30-39
```

## Method
The bash script uses `taskset` command to assign a list of CPUs to the python process.
The test is implemented with Python's multiprocessing package.

## Result
```bash
$ ./run.sh
MobileNetV1 on CPU, core number = 1, latency = 96.90836970694363 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 2, latency = 87.45878878980875 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 3, latency = 79.75820992141962 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 4, latency = 71.23094699345529 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 5, latency = 154.0113527327776 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 6, latency = 200.6550207734108 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 7, latency = 218.93502422608435 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 8, latency = 242.63878031633794 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 9, latency = 293.14806149341166 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 10, latency = 3818.4753553941846 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 11, latency = 4155.328413657844 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 12, latency = 3953.801923803985 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 13, latency = 3771.3194217998534 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 14, latency = 3607.7484861947596 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 15, latency = 3034.1190627776086 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 16, latency = 1608.978587668389 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 17, latency = 693.9090805128217 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 18, latency = 618.5869241598994 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 19, latency = 806.7370967939496 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 20, latency = 841.2491333205253 ms, averaged over 10 runs.
```

CPU usage can be validated with `htop`:
![](https://res.cloudinary.com/dxzx2bxch/image/upload/v1624010944/github/Screen_Shot_2021-06-18_at_18.07.40_bmj7n2.png)
