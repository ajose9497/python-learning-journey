"""
Python If-Else
"""

import math
import os
import random
import re
import sys

n = int(input())
if (n % 2 == 0 and 2 <= n <= 5) or (n % 2 == 0 and 20 < n <= 100):
    print ("Not Weird")
else:
    print ("Weird")
