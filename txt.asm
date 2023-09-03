beq $t1,$t3,noteq
add $t2,$zero,$t5
noteq:
slr $t2,$s0,2
loop:
addi $t0, $t0, 1
j loop
sw $t8,4($t9)
lui $s4,3