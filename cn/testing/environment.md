我们在一台x86_64架构，32核超线程CPU，E5-2630 v3 @ 2.40GHzCPU（2356K L2 Cache, 20MB L3 Cache），128G内存，1个500GB的SSD机器上对比了Redis、LevelDB，DezhouKV和SogouQDB。
DezhouKV（1+1+1），意味着后端节点包含（1DRAM+1SSD+1HDD,在这次实验，使用SSD后端替换HDD后端）。
SogouQDB上的测试，由于是内部使用的KV数据库，因此在此使用了HDD磁盘作为测量，并没做SSD对比测量。


#REDIS
##redis-benchmark -t set,get -p 6379 -n 1000000 -r 1000000 -c 50 -P 16 -d 1

###====== SET ======
___
      1000000 requests completed in 1.98 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    4.69% <= 1 milliseconds
    96.13% <= 2 milliseconds
    98.60% <= 3 milliseconds
    99.29% <= 4 milliseconds
    99.71% <= 5 milliseconds
    99.81% <= 6 milliseconds
    99.90% <= 7 milliseconds
    99.93% <= 8 milliseconds
    99.97% <= 9 milliseconds
    99.98% <= 10 milliseconds
    100.00% <= 10 milliseconds
    505050.50 requests per second
___
###====== GET ======
___
      1000000 requests completed in 1.49 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    45.90% <= 1 milliseconds
    99.66% <= 2 milliseconds
    100.00% <= 2 milliseconds
    670690.81 requests per second
___
#LEVELDB
##redis-benchmark -t set,get -p 10100 -n 1000000 -r 1000000 -c 50 -P 16 -d 1

###====== SET ======
___
      1000000 requests completed in 5.83 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 2 milliseconds
    0.01% <= 3 milliseconds
    2.40% <= 4 milliseconds
    97.88% <= 5 milliseconds
    98.13% <= 6 milliseconds
    98.51% <= 7 milliseconds
    98.73% <= 8 milliseconds
    99.00% <= 9 milliseconds
    99.82% <= 10 milliseconds
    99.84% <= 11 milliseconds
    99.97% <= 12 milliseconds
    100.00% <= 12 milliseconds
    171585.45 requests per second
___
###====== GET ======
___
      1000000 requests completed in 8.77 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 2 milliseconds
    0.00% <= 3 milliseconds
    0.00% <= 4 milliseconds
    0.01% <= 5 milliseconds
    2.88% <= 6 milliseconds
    89.51% <= 7 milliseconds
    93.10% <= 8 milliseconds
    93.12% <= 9 milliseconds
    96.43% <= 10 milliseconds
    97.44% <= 11 milliseconds
    98.01% <= 12 milliseconds
    98.24% <= 13 milliseconds
    98.26% <= 14 milliseconds
    98.32% <= 15 milliseconds
    98.36% <= 16 milliseconds
    98.55% <= 17 milliseconds
    98.80% <= 18 milliseconds
    98.88% <= 19 milliseconds
    99.36% <= 20 milliseconds
    99.52% <= 22 milliseconds
    99.54% <= 23 milliseconds
    99.60% <= 24 milliseconds
    99.68% <= 25 milliseconds
    99.76% <= 26 milliseconds
    99.83% <= 27 milliseconds
    99.92% <= 37 milliseconds
    99.97% <= 38 milliseconds
    100.00% <= 38 milliseconds
    113999.09 requests per second
___
#DEZHOUKV
#1+1+1
##redis-benchmark -t set,get -p 9999 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 37.75 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 19 milliseconds
    0.00% <= 20 milliseconds
    0.33% <= 21 milliseconds
    2.08% <= 22 milliseconds
    5.20% <= 23 milliseconds
    9.96% <= 24 milliseconds
    13.95% <= 25 milliseconds
    19.04% <= 26 milliseconds
    25.77% <= 27 milliseconds
    34.80% <= 28 milliseconds
    44.27% <= 29 milliseconds
    53.62% <= 30 milliseconds
    62.35% <= 31 milliseconds
    69.35% <= 32 milliseconds
    76.39% <= 33 milliseconds
    81.36% <= 34 milliseconds
    85.49% <= 35 milliseconds
    88.64% <= 36 milliseconds
    92.05% <= 37 milliseconds
    93.97% <= 38 milliseconds
    95.49% <= 39 milliseconds
    97.18% <= 40 milliseconds
    98.35% <= 41 milliseconds
    98.81% <= 42 milliseconds
    99.08% <= 43 milliseconds
    99.39% <= 44 milliseconds
    99.64% <= 45 milliseconds
    99.76% <= 46 milliseconds
    99.76% <= 47 milliseconds
    99.78% <= 48 milliseconds
    99.83% <= 49 milliseconds
    99.86% <= 50 milliseconds
    99.92% <= 53 milliseconds
    99.92% <= 57 milliseconds
    99.98% <= 58 milliseconds
    100.00% <= 58 milliseconds
    26491.47 requests per second
___
###====== GET ======
___
      1000000 requests completed in 37.53 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 21 milliseconds
    0.47% <= 22 milliseconds
    4.50% <= 23 milliseconds
    11.30% <= 24 milliseconds
    17.02% <= 25 milliseconds
    22.44% <= 26 milliseconds
    29.07% <= 27 milliseconds
    36.32% <= 28 milliseconds
    45.24% <= 29 milliseconds
    54.43% <= 30 milliseconds
    62.88% <= 31 milliseconds
    70.44% <= 32 milliseconds
    76.07% <= 33 milliseconds
    81.11% <= 34 milliseconds
    84.60% <= 35 milliseconds
    88.75% <= 36 milliseconds
    92.56% <= 37 milliseconds
    94.96% <= 38 milliseconds
    96.83% <= 39 milliseconds
    97.73% <= 40 milliseconds
    98.32% <= 41 milliseconds
    98.80% <= 42 milliseconds
    99.59% <= 43 milliseconds
    99.61% <= 44 milliseconds
    99.75% <= 45 milliseconds
    99.88% <= 46 milliseconds
    99.92% <= 47 milliseconds
    99.92% <= 48 milliseconds
    99.92% <= 50 milliseconds
    99.92% <= 54 milliseconds
    100.00% <= 54 milliseconds
    26644.64 requests per second
___

#DEZHOUKV
#2+2+2
##redis-benchmark -t set,get -p 9999 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 39.25 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 13 milliseconds
    0.00% <= 21 milliseconds
    0.00% <= 23 milliseconds
    0.22% <= 24 milliseconds
    2.52% <= 25 milliseconds
    8.53% <= 26 milliseconds
    15.93% <= 27 milliseconds
    24.48% <= 28 milliseconds
    36.14% <= 29 milliseconds
    45.60% <= 30 milliseconds
    54.95% <= 31 milliseconds
    63.06% <= 32 milliseconds
    69.88% <= 33 milliseconds
    75.39% <= 34 milliseconds
    80.87% <= 35 milliseconds
    85.74% <= 36 milliseconds
    89.18% <= 37 milliseconds
    92.38% <= 38 milliseconds
    94.30% <= 39 milliseconds
    95.77% <= 40 milliseconds
    97.17% <= 41 milliseconds
    98.08% <= 42 milliseconds
    98.74% <= 43 milliseconds
    99.30% <= 44 milliseconds
    99.51% <= 45 milliseconds
    99.76% <= 48 milliseconds
    99.76% <= 51 milliseconds
    99.82% <= 52 milliseconds
    99.90% <= 53 milliseconds
    99.92% <= 70 milliseconds
    99.92% <= 71 milliseconds
    99.97% <= 72 milliseconds
    100.00% <= 72 milliseconds
    25475.11 requests per second
___
###====== GET ======
___
      1000000 requests completed in 40.83 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 22 milliseconds
    0.04% <= 23 milliseconds
    0.18% <= 24 milliseconds
    1.19% <= 25 milliseconds
    3.96% <= 26 milliseconds
    10.07% <= 27 milliseconds
    17.00% <= 28 milliseconds
    25.37% <= 29 milliseconds
    33.75% <= 30 milliseconds
    41.35% <= 31 milliseconds
    48.24% <= 32 milliseconds
    57.22% <= 33 milliseconds
    65.42% <= 34 milliseconds
    72.58% <= 35 milliseconds
    78.65% <= 36 milliseconds
    83.89% <= 37 milliseconds
    88.07% <= 38 milliseconds
    91.48% <= 39 milliseconds
    94.39% <= 40 milliseconds
    96.58% <= 41 milliseconds
    97.52% <= 42 milliseconds
    98.40% <= 43 milliseconds
    98.96% <= 44 milliseconds
    99.20% <= 45 milliseconds
    99.42% <= 46 milliseconds
    99.48% <= 47 milliseconds
    99.56% <= 48 milliseconds
    99.60% <= 49 milliseconds
    99.68% <= 50 milliseconds
    99.68% <= 51 milliseconds
    99.76% <= 53 milliseconds
    99.84% <= 55 milliseconds
    99.92% <= 56 milliseconds
    100.00% <= 56 milliseconds
    24493.60 requests per second
___

#DEZHOUKV
#3+3+3
## redis-benchmark -t set,get -p 9999 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 54.34 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 25 milliseconds
    0.07% <= 26 milliseconds
    0.24% <= 27 milliseconds
    0.39% <= 28 milliseconds
    0.75% <= 29 milliseconds
    1.24% <= 30 milliseconds
    2.85% <= 31 milliseconds
    4.41% <= 32 milliseconds
    7.12% <= 33 milliseconds
    10.36% <= 34 milliseconds
    14.39% <= 35 milliseconds
    19.61% <= 36 milliseconds
    24.53% <= 37 milliseconds
    29.77% <= 38 milliseconds
    35.22% <= 39 milliseconds
    41.42% <= 40 milliseconds
    46.22% <= 41 milliseconds
    52.08% <= 42 milliseconds
    56.13% <= 43 milliseconds
    60.93% <= 44 milliseconds
    65.60% <= 45 milliseconds
    68.59% <= 46 milliseconds
    71.67% <= 47 milliseconds
    74.31% <= 48 milliseconds
    76.18% <= 49 milliseconds
    77.93% <= 50 milliseconds
    79.70% <= 51 milliseconds
    82.32% <= 52 milliseconds
    84.27% <= 53 milliseconds
    86.32% <= 54 milliseconds
    88.20% <= 55 milliseconds
    90.41% <= 56 milliseconds
    92.32% <= 57 milliseconds
    93.64% <= 58 milliseconds
    94.96% <= 59 milliseconds
    95.85% <= 60 milliseconds
    96.72% <= 61 milliseconds
    97.86% <= 62 milliseconds
    98.45% <= 63 milliseconds
    98.94% <= 64 milliseconds
    99.31% <= 65 milliseconds
    99.63% <= 66 milliseconds
    99.82% <= 67 milliseconds
    99.90% <= 68 milliseconds
    99.92% <= 69 milliseconds
    99.98% <= 70 milliseconds
    100.00% <= 70 milliseconds
    18404.01 requests per second
___
###====== GET ======
___
      1000000 requests completed in 42.79 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 23 milliseconds
    0.00% <= 24 milliseconds
    0.21% <= 25 milliseconds
    0.73% <= 26 milliseconds
    2.72% <= 27 milliseconds
    7.73% <= 28 milliseconds
    14.05% <= 29 milliseconds
    21.96% <= 30 milliseconds
    30.98% <= 31 milliseconds
    39.57% <= 32 milliseconds
    46.92% <= 33 milliseconds
    53.57% <= 34 milliseconds
    62.11% <= 35 milliseconds
    70.00% <= 36 milliseconds
    76.14% <= 37 milliseconds
    80.51% <= 38 milliseconds
    84.73% <= 39 milliseconds
    88.41% <= 40 milliseconds
    91.29% <= 41 milliseconds
    93.45% <= 42 milliseconds
    94.77% <= 43 milliseconds
    96.02% <= 44 milliseconds
    97.47% <= 45 milliseconds
    98.13% <= 46 milliseconds
    98.40% <= 47 milliseconds
    98.60% <= 48 milliseconds
    98.72% <= 49 milliseconds
    98.94% <= 50 milliseconds
    99.26% <= 51 milliseconds
    99.47% <= 52 milliseconds
    99.52% <= 54 milliseconds
    99.56% <= 55 milliseconds
    99.68% <= 56 milliseconds
    99.92% <= 57 milliseconds
    99.92% <= 58 milliseconds
    100.00% <= 58 milliseconds
    23372.13 requests per second
___

#DEZHOUKV
#4+4+4
## redis-benchmark -t set,get -p 9999 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 69.56 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 29 milliseconds
    0.00% <= 31 milliseconds
    0.04% <= 32 milliseconds
    0.16% <= 33 milliseconds
    0.77% <= 34 milliseconds
    1.65% <= 35 milliseconds
    2.45% <= 36 milliseconds
    4.13% <= 37 milliseconds
    6.75% <= 38 milliseconds
    9.65% <= 39 milliseconds
    13.00% <= 40 milliseconds
    15.41% <= 41 milliseconds
    19.40% <= 42 milliseconds
    23.96% <= 43 milliseconds
    27.42% <= 44 milliseconds
    32.07% <= 45 milliseconds
    35.97% <= 46 milliseconds
    39.28% <= 47 milliseconds
    41.79% <= 48 milliseconds
    44.14% <= 49 milliseconds
    46.06% <= 50 milliseconds
    48.39% <= 51 milliseconds
    49.99% <= 52 milliseconds
    51.21% <= 53 milliseconds
    53.04% <= 54 milliseconds
    54.70% <= 55 milliseconds
    56.48% <= 56 milliseconds
    59.03% <= 57 milliseconds
    62.44% <= 58 milliseconds
    66.55% <= 59 milliseconds
    69.70% <= 60 milliseconds
    72.66% <= 61 milliseconds
    75.95% <= 62 milliseconds
    78.38% <= 63 milliseconds
    80.36% <= 64 milliseconds
    81.52% <= 65 milliseconds
    82.82% <= 66 milliseconds
    83.47% <= 67 milliseconds
    83.60% <= 68 milliseconds
    83.83% <= 69 milliseconds
    84.30% <= 70 milliseconds
    84.53% <= 71 milliseconds
    84.99% <= 72 milliseconds
    85.21% <= 73 milliseconds
    85.63% <= 74 milliseconds
    86.41% <= 75 milliseconds
    86.65% <= 76 milliseconds
    87.07% <= 77 milliseconds
    87.55% <= 78 milliseconds
    87.89% <= 79 milliseconds
    88.55% <= 80 milliseconds
    89.63% <= 81 milliseconds
    90.70% <= 82 milliseconds
    91.59% <= 83 milliseconds
    92.53% <= 84 milliseconds
    93.58% <= 85 milliseconds
    93.87% <= 86 milliseconds
    94.66% <= 87 milliseconds
    95.06% <= 88 milliseconds
    95.64% <= 89 milliseconds
    96.21% <= 90 milliseconds
    96.64% <= 91 milliseconds
    96.83% <= 92 milliseconds
    96.90% <= 93 milliseconds
    97.07% <= 94 milliseconds
    97.15% <= 95 milliseconds
    97.20% <= 96 milliseconds
    97.25% <= 97 milliseconds
    97.51% <= 98 milliseconds
    97.60% <= 99 milliseconds
    97.88% <= 100 milliseconds
    98.00% <= 101 milliseconds
    98.20% <= 102 milliseconds
    98.43% <= 103 milliseconds
    98.84% <= 104 milliseconds
    99.04% <= 105 milliseconds
    99.35% <= 106 milliseconds
    99.44% <= 107 milliseconds
    99.54% <= 108 milliseconds
    99.67% <= 109 milliseconds
    99.76% <= 110 milliseconds
    99.82% <= 111 milliseconds
    99.92% <= 112 milliseconds
    99.92% <= 113 milliseconds
    99.92% <= 114 milliseconds
    100.00% <= 115 milliseconds
    100.00% <= 115 milliseconds
    14376.08 requests per second
___
###====== GET ======
___
      1000000 requests completed in 51.07 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 19 milliseconds
    0.00% <= 24 milliseconds
    0.16% <= 25 milliseconds
    0.55% <= 26 milliseconds
    1.22% <= 27 milliseconds
    2.41% <= 28 milliseconds
    4.84% <= 29 milliseconds
    6.94% <= 30 milliseconds
    10.43% <= 31 milliseconds
    15.00% <= 32 milliseconds
    18.61% <= 33 milliseconds
    23.00% <= 34 milliseconds
    28.79% <= 35 milliseconds
    34.84% <= 36 milliseconds
    40.59% <= 37 milliseconds
    46.41% <= 38 milliseconds
    51.17% <= 39 milliseconds
    55.59% <= 40 milliseconds
    59.25% <= 41 milliseconds
    63.04% <= 42 milliseconds
    65.89% <= 43 milliseconds
    69.03% <= 44 milliseconds
    71.37% <= 45 milliseconds
    73.67% <= 46 milliseconds
    76.01% <= 47 milliseconds
    77.94% <= 48 milliseconds
    80.64% <= 49 milliseconds
    82.62% <= 50 milliseconds
    84.93% <= 51 milliseconds
    87.12% <= 52 milliseconds
    89.37% <= 53 milliseconds
    91.74% <= 54 milliseconds
    93.34% <= 55 milliseconds
    94.83% <= 56 milliseconds
    96.31% <= 57 milliseconds
    97.35% <= 58 milliseconds
    98.31% <= 59 milliseconds
    98.84% <= 60 milliseconds
    99.11% <= 61 milliseconds
    99.12% <= 65 milliseconds
    99.20% <= 68 milliseconds
    99.24% <= 69 milliseconds
    99.40% <= 70 milliseconds
    99.49% <= 71 milliseconds
    99.56% <= 72 milliseconds
    99.67% <= 73 milliseconds
    99.68% <= 74 milliseconds
    99.68% <= 75 milliseconds
    99.75% <= 76 milliseconds
    99.80% <= 77 milliseconds
    99.87% <= 78 milliseconds
    99.96% <= 79 milliseconds
    100.00% <= 79 milliseconds
    19580.58 requests per second
___
#DEZHOUKV
#5+5+5

## redis-benchmark -t set,get -p 9999 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 72.25 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 31 milliseconds
    0.21% <= 32 milliseconds
    0.50% <= 33 milliseconds
    0.96% <= 34 milliseconds
    1.86% <= 35 milliseconds
    2.44% <= 36 milliseconds
    2.85% <= 37 milliseconds
    3.04% <= 38 milliseconds
    3.71% <= 39 milliseconds
    4.82% <= 40 milliseconds
    6.26% <= 41 milliseconds
    7.56% <= 42 milliseconds
    9.43% <= 43 milliseconds
    11.83% <= 44 milliseconds
    14.22% <= 45 milliseconds
    16.87% <= 46 milliseconds
    18.91% <= 47 milliseconds
    21.68% <= 48 milliseconds
    24.47% <= 49 milliseconds
    26.74% <= 50 milliseconds
    29.00% <= 51 milliseconds
    31.03% <= 52 milliseconds
    33.41% <= 53 milliseconds
    35.57% <= 54 milliseconds
    38.02% <= 55 milliseconds
    40.76% <= 56 milliseconds
    43.74% <= 57 milliseconds
    47.87% <= 58 milliseconds
    51.96% <= 59 milliseconds
    56.24% <= 60 milliseconds
    60.27% <= 61 milliseconds
    64.54% <= 62 milliseconds
    68.54% <= 63 milliseconds
    71.81% <= 64 milliseconds
    74.98% <= 65 milliseconds
    77.30% <= 66 milliseconds
    79.50% <= 67 milliseconds
    82.01% <= 68 milliseconds
    84.96% <= 69 milliseconds
    87.65% <= 70 milliseconds
    89.87% <= 71 milliseconds
    92.00% <= 72 milliseconds
    94.03% <= 73 milliseconds
    95.42% <= 74 milliseconds
    96.70% <= 75 milliseconds
    98.20% <= 76 milliseconds
    98.68% <= 77 milliseconds
    99.02% <= 78 milliseconds
    99.51% <= 79 milliseconds
    99.80% <= 80 milliseconds
    99.92% <= 104 milliseconds
    99.95% <= 105 milliseconds
    99.99% <= 106 milliseconds
    100.00% <= 106 milliseconds
    13841.02 requests per second
___
###====== GET ======
___
      1000000 requests completed in 65.99 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 28 milliseconds
    0.04% <= 29 milliseconds
    0.19% <= 30 milliseconds
    0.34% <= 31 milliseconds
    0.60% <= 32 milliseconds
    1.04% <= 33 milliseconds
    2.04% <= 34 milliseconds
    3.88% <= 35 milliseconds
    6.36% <= 36 milliseconds
    8.88% <= 37 milliseconds
    11.81% <= 38 milliseconds
    14.08% <= 39 milliseconds
    17.82% <= 40 milliseconds
    22.40% <= 41 milliseconds
    25.93% <= 42 milliseconds
    29.17% <= 43 milliseconds
    31.51% <= 44 milliseconds
    34.19% <= 45 milliseconds
    37.35% <= 46 milliseconds
    39.14% <= 47 milliseconds
    40.63% <= 48 milliseconds
    42.69% <= 49 milliseconds
    44.91% <= 50 milliseconds
    47.46% <= 51 milliseconds
    50.02% <= 52 milliseconds
    53.36% <= 53 milliseconds
    58.34% <= 54 milliseconds
    62.02% <= 55 milliseconds
    66.07% <= 56 milliseconds
    69.32% <= 57 milliseconds
    72.38% <= 58 milliseconds
    74.81% <= 59 milliseconds
    77.16% <= 60 milliseconds
    78.50% <= 61 milliseconds
    79.56% <= 62 milliseconds
    80.32% <= 63 milliseconds
    81.03% <= 64 milliseconds
    82.04% <= 65 milliseconds
    82.93% <= 66 milliseconds
    83.73% <= 67 milliseconds
    84.54% <= 68 milliseconds
    85.43% <= 69 milliseconds
    86.08% <= 70 milliseconds
    86.53% <= 71 milliseconds
    87.41% <= 72 milliseconds
    88.59% <= 73 milliseconds
    90.24% <= 74 milliseconds
    92.11% <= 75 milliseconds
    93.65% <= 76 milliseconds
    95.01% <= 77 milliseconds
    95.52% <= 78 milliseconds
    96.52% <= 79 milliseconds
    97.74% <= 80 milliseconds
    98.49% <= 81 milliseconds
    99.22% <= 82 milliseconds
    99.69% <= 83 milliseconds
    99.99% <= 84 milliseconds
    100.00% <= 86 milliseconds
    100.00% <= 86 milliseconds
    15152.89 requests per second
___
#DEZHOUKV
#6+6+6
##redis-benchmark -t set,get -p 9999 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 85.43 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 30 milliseconds
    0.00% <= 31 milliseconds
    0.08% <= 32 milliseconds
    0.16% <= 33 milliseconds
    0.39% <= 34 milliseconds
    0.53% <= 35 milliseconds
    0.56% <= 36 milliseconds
    0.87% <= 37 milliseconds
    1.12% <= 38 milliseconds
    1.68% <= 39 milliseconds
    2.04% <= 40 milliseconds
    2.80% <= 41 milliseconds
    3.19% <= 42 milliseconds
    3.64% <= 43 milliseconds
    4.45% <= 44 milliseconds
    5.38% <= 45 milliseconds
    6.19% <= 46 milliseconds
    6.95% <= 47 milliseconds
    7.90% <= 48 milliseconds
    9.50% <= 49 milliseconds
    10.62% <= 50 milliseconds
    11.61% <= 51 milliseconds
    12.39% <= 52 milliseconds
    13.84% <= 53 milliseconds
    14.99% <= 54 milliseconds
    16.24% <= 55 milliseconds
    17.84% <= 56 milliseconds
    19.72% <= 57 milliseconds
    21.86% <= 58 milliseconds
    24.25% <= 59 milliseconds
    27.19% <= 60 milliseconds
    30.42% <= 61 milliseconds
    33.94% <= 62 milliseconds
    37.98% <= 63 milliseconds
    41.65% <= 64 milliseconds
    44.48% <= 65 milliseconds
    46.73% <= 66 milliseconds
    49.40% <= 67 milliseconds
    52.41% <= 68 milliseconds
    55.63% <= 69 milliseconds
    58.96% <= 70 milliseconds
    61.17% <= 71 milliseconds
    63.22% <= 72 milliseconds
    65.79% <= 73 milliseconds
    67.64% <= 74 milliseconds
    69.67% <= 75 milliseconds
    71.80% <= 76 milliseconds
    73.73% <= 77 milliseconds
    75.50% <= 78 milliseconds
    77.42% <= 79 milliseconds
    79.00% <= 80 milliseconds
    80.60% <= 81 milliseconds
    81.88% <= 82 milliseconds
    84.17% <= 83 milliseconds
    85.95% <= 84 milliseconds
    87.82% <= 85 milliseconds
    89.06% <= 86 milliseconds
    90.24% <= 87 milliseconds
    91.53% <= 88 milliseconds
    92.57% <= 89 milliseconds
    93.18% <= 90 milliseconds
    93.52% <= 91 milliseconds
    94.31% <= 92 milliseconds
    94.78% <= 93 milliseconds
    95.31% <= 94 milliseconds
    96.03% <= 95 milliseconds
    96.99% <= 96 milliseconds
    97.20% <= 97 milliseconds
    97.38% <= 98 milliseconds
    97.52% <= 99 milliseconds
    97.83% <= 100 milliseconds
    98.14% <= 101 milliseconds
    98.74% <= 102 milliseconds
    99.03% <= 103 milliseconds
    99.24% <= 104 milliseconds
    99.41% <= 105 milliseconds
    99.51% <= 106 milliseconds
    99.68% <= 107 milliseconds
    99.84% <= 108 milliseconds
    99.84% <= 109 milliseconds
    99.92% <= 110 milliseconds
    99.92% <= 112 milliseconds
    99.94% <= 113 milliseconds
    99.99% <= 114 milliseconds
    100.00% <= 114 milliseconds
    11705.49 requests per second
___
###====== GET ======
___
      1000000 requests completed in 54.56 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 29 milliseconds
    0.31% <= 30 milliseconds
    0.45% <= 31 milliseconds
    1.46% <= 32 milliseconds
    2.77% <= 33 milliseconds
    4.98% <= 34 milliseconds
    8.44% <= 35 milliseconds
    12.71% <= 36 milliseconds
    17.65% <= 37 milliseconds
    22.78% <= 38 milliseconds
    29.32% <= 39 milliseconds
    36.41% <= 40 milliseconds
    45.12% <= 41 milliseconds
    52.61% <= 42 milliseconds
    59.34% <= 43 milliseconds
    65.47% <= 44 milliseconds
    70.26% <= 45 milliseconds
    73.85% <= 46 milliseconds
    76.25% <= 47 milliseconds
    77.69% <= 48 milliseconds
    79.71% <= 49 milliseconds
    80.82% <= 50 milliseconds
    82.11% <= 51 milliseconds
    83.97% <= 52 milliseconds
    86.02% <= 53 milliseconds
    87.34% <= 54 milliseconds
    88.72% <= 55 milliseconds
    90.24% <= 56 milliseconds
    92.07% <= 57 milliseconds
    93.69% <= 58 milliseconds
    94.63% <= 59 milliseconds
    96.56% <= 60 milliseconds
    97.64% <= 61 milliseconds
    98.41% <= 62 milliseconds
    98.70% <= 63 milliseconds
    98.88% <= 64 milliseconds
    99.07% <= 65 milliseconds
    99.28% <= 66 milliseconds
    99.43% <= 67 milliseconds
    99.52% <= 68 milliseconds
    99.71% <= 69 milliseconds
    99.76% <= 70 milliseconds
    99.84% <= 71 milliseconds
    99.85% <= 72 milliseconds
    99.91% <= 73 milliseconds
    99.92% <= 75 milliseconds
    99.92% <= 77 milliseconds
    99.92% <= 78 milliseconds
    100.00% <= 78 milliseconds
    18327.44 requests per second
___
#SOGOUQDB
## redis-benchmark -t set,get -p 8823 -n 1000000 -r 1000000 -c 50 -P 16 -d 1
###====== SET ======
___
      1000000 requests completed in 71.35 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 34 milliseconds
    0.00% <= 49 milliseconds
    0.09% <= 50 milliseconds
    1.70% <= 51 milliseconds
    11.19% <= 52 milliseconds
    22.59% <= 53 milliseconds
    30.89% <= 54 milliseconds
    40.62% <= 55 milliseconds
    52.74% <= 56 milliseconds
    60.83% <= 57 milliseconds
    67.24% <= 58 milliseconds
    74.44% <= 59 milliseconds
    81.00% <= 60 milliseconds
    85.41% <= 61 milliseconds
    89.57% <= 62 milliseconds
    92.39% <= 63 milliseconds
    93.66% <= 64 milliseconds
    95.06% <= 65 milliseconds
    96.15% <= 66 milliseconds
    97.08% <= 67 milliseconds
    97.77% <= 68 milliseconds
    98.22% <= 69 milliseconds
    98.41% <= 70 milliseconds
    98.77% <= 71 milliseconds
    98.88% <= 72 milliseconds
    99.14% <= 73 milliseconds
    99.20% <= 74 milliseconds
    99.32% <= 75 milliseconds
    99.36% <= 79 milliseconds
    99.44% <= 80 milliseconds
    99.44% <= 84 milliseconds
    99.47% <= 86 milliseconds
    99.52% <= 87 milliseconds
    99.54% <= 88 milliseconds
    99.60% <= 92 milliseconds
    99.60% <= 96 milliseconds
    99.68% <= 97 milliseconds
    99.71% <= 98 milliseconds
    99.74% <= 99 milliseconds
    99.76% <= 107 milliseconds
    99.80% <= 108 milliseconds
    99.83% <= 111 milliseconds
    99.84% <= 112 milliseconds
    99.84% <= 117 milliseconds
    99.84% <= 126 milliseconds
    99.85% <= 127 milliseconds
    99.87% <= 128 milliseconds
    99.92% <= 139 milliseconds
    99.97% <= 140 milliseconds
    99.98% <= 142 milliseconds
    100.00% <= 155 milliseconds
    100.00% <= 155 milliseconds
    14015.61 requests per second
___
###====== GET ======
___
      1000000 requests completed in 63.60 seconds
      50 parallel clients
      1 bytes payload
      keep alive: 1

    0.00% <= 29 milliseconds
    0.00% <= 36 milliseconds
    0.20% <= 37 milliseconds
    0.41% <= 38 milliseconds
    0.49% <= 39 milliseconds
    0.56% <= 40 milliseconds
    0.63% <= 41 milliseconds
    0.64% <= 42 milliseconds
    0.64% <= 43 milliseconds
    0.80% <= 44 milliseconds
    1.29% <= 45 milliseconds
    4.20% <= 46 milliseconds
    16.92% <= 47 milliseconds
    32.63% <= 48 milliseconds
    40.35% <= 49 milliseconds
    51.96% <= 50 milliseconds
    65.91% <= 51 milliseconds
    73.64% <= 52 milliseconds
    78.64% <= 53 milliseconds
    84.04% <= 54 milliseconds
    87.84% <= 55 milliseconds
    90.80% <= 56 milliseconds
    92.78% <= 57 milliseconds
    94.81% <= 58 milliseconds
    95.53% <= 59 milliseconds
    96.68% <= 60 milliseconds
    97.24% <= 61 milliseconds
    97.51% <= 62 milliseconds
    97.97% <= 63 milliseconds
    98.19% <= 64 milliseconds
    98.46% <= 65 milliseconds
    98.56% <= 66 milliseconds
    98.72% <= 67 milliseconds
    98.80% <= 68 milliseconds
    98.84% <= 69 milliseconds
    98.95% <= 70 milliseconds
    98.96% <= 71 milliseconds
    98.96% <= 72 milliseconds
    99.09% <= 73 milliseconds
    99.12% <= 74 milliseconds
    99.20% <= 75 milliseconds
    99.27% <= 76 milliseconds
    99.28% <= 77 milliseconds
    99.33% <= 78 milliseconds
    99.41% <= 79 milliseconds
    99.44% <= 83 milliseconds
    99.54% <= 85 milliseconds
    99.54% <= 86 milliseconds
    99.63% <= 87 milliseconds
    99.71% <= 88 milliseconds
    99.71% <= 89 milliseconds
    99.76% <= 90 milliseconds
    99.84% <= 93 milliseconds
    99.92% <= 97 milliseconds
    99.92% <= 106 milliseconds
    99.92% <= 116 milliseconds
    99.94% <= 117 milliseconds
    99.97% <= 118 milliseconds
    100.00% <= 118 milliseconds
    15722.03 requests per second
___