import sys
A = 0
B = 0
C = 0

POINTER = 0


def adv(x):
    global A, B, C, POINTER
    bot = 2 ** x
    A //= bot
    POINTER += 2
    
def bxl(x):
    global A, B, C, POINTER

    B ^= x
    POINTER += 2

def bst(x):
    global A, B, C, POINTER
    B = x % 8
    POINTER += 2
    
def jnz(x):
    global A, B, C, POINTER
    # print("jump", A)
    if A == 0: 
        POINTER += 2
    else: POINTER = x
    
def bxc(x):
    global A, B, C, POINTER
    B = B ^ C
    POINTER += 2
    
def out(x):
    global A, B, C, POINTER
    print(x % 8, ",", sep="", end="")
    POINTER += 2

def bdv(x):
    global A, B, C, POINTER
    bot = 2 ** x
    B =  A//bot
    POINTER += 2

def cdv(x):
    global A, B, C, POINTER
    bot = 2 ** x
    C = A // bot
    POINTER += 2

f = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
combo = [1, 0, 1, 0, 0, 1, 1, 1]

def val(x):
    if x <= 3: return x
    if x == 4: return A
    if x == 5: return B
    if x == 6: return C
    assert False


A = int(input().split(":")[-1])
B = int(input().split(":")[-1])
C = int(input().split(":")[-1])
input()
moves = list(map(int, input().split(":")[-1].split(",")))

while POINTER + 2 <= len(moves):    
    a = moves[POINTER]
    x = moves[POINTER + 1]
    
    if combo[a]:
        x = val(x)
    f[a](x)
