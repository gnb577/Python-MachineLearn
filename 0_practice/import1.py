#import는 모듈을 가져오겠다는 뜻

import math
print(math.cos(1))

import random
random.randint(1,10)


#특정 모듈의 특정 함수만 가져오겠다
from random import randint
from math import floor,ceil