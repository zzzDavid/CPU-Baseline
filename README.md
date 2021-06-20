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

## Another result

```
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              40
On-line CPU(s) list: 0-39
Thread(s) per core:  2
Core(s) per socket:  10
Socket(s):           2
NUMA node(s):        2
Vendor ID:           GenuineIntel
CPU family:          6
Model:               79
Model name:          Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz
Stepping:            1
CPU MHz:             1202.777
CPU max MHz:         3100.0000
CPU min MHz:         1200.0000
BogoMIPS:            4399.94
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            25600K
NUMA node0 CPU(s):   0-9,20-29
NUMA node1 CPU(s):   10-19,30-39
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cdp_l3 invpcid_single pti intel_ppin ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a rdseed adx smap intel_pt xsaveopt cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat pln pts md_clear flush_l1d
```

```text
MobileNetV1 on CPU, core number = 1, latency = 138.65409907884896 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 2, latency = 76.5099098905921 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 3, latency = 58.21206858381629 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 4, latency = 49.735910538583994 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 5, latency = 43.96906797774136 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 6, latency = 39.891057601198554 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 7, latency = 41.4598701056093 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 8, latency = 38.08772130869329 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 9, latency = 37.76029008440673 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 10, latency = 36.78090148605406 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 11, latency = 45.91669971123338 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 12, latency = 48.85133542120457 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 13, latency = 45.942784287035465 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 14, latency = 50.748758809641004 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 15, latency = 45.78587883152068 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 16, latency = 50.691268499940634 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 17, latency = 48.15710713155568 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 18, latency = 51.276167994365096 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 19, latency = 50.558837316930294 ms, averaged over 10 runs.
MobileNetV1 on CPU, core number = 20, latency = 51.16348098963499 ms, averaged over 10 runs.
```
