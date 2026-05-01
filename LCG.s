li x1, 17 # define m
li x2, 7 # define a
li x3, 3 # define c
li x15, 6 # define x0
li x4, 20 # define n
li x5, 0 # define i
loop:
    slli x6, x5, 3
    mul x15, x15, x2
    add x15, x15, x3
    remu x15, x15, x1
    addi x5, x5, 1
    blt x5, x4, loop