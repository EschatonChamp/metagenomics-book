#!/usr/bin/env python3
"""Show recominations"""

import os
import sys
from itertools import product, chain

args = sys.argv

if len(args) != 2:
    print('Usage: {} NUM_GENES'.format(os.path.basename(args[0])))
    sys.exit(1)

if not args[1].isdigit():
    print('"{}" does not look like an integer'.format(args[1]))
    sys.exit(1)

num_genes = int(args[1])
if not 2 <= num_genes <= 10:
    print('NUM_GENES must be greater than 1, less than 10')
    sys.exit(1)

promotors = ['P' + str(n + 1) for n in range(0, num_genes)]
coding = ['C' + str(n + 1) for n in range(0, num_genes)]
terminators = ['T' + str(n + 1) for n in range(0, num_genes)]

print('N = "{}"'.format(num_genes))
for i, combo in enumerate(chain(product(promotors, coding, terminators))):
    print('{:3}: {}'.format(i + 1, combo))