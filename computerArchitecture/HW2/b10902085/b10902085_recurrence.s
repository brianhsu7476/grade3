.globl __start
__start:
	li a0, 5
	ecall
	call recur
	mv a1, a0
	li a0, 1
	ecall
	li a0, 10
	ecall
recur:
	addi sp, sp, -12
	sw s0, 0(sp)
	sw s1, 4(sp)
	sw ra, 8(sp)
	mv s0, a0
	li s1, 0
	beq s0, s1, recur_ret
	li s1, 1
	beq s0, s1, recur_ret
	addi a0, s0, -1
	call recur
	mv s1, a0
	slli s1, s1, 1
	addi a0, s0, -2
	call recur
	add s1, s1, a0
recur_ret:
	mv a0, s1
	lw s0, 0(sp)
	lw s1, 4(sp)
	lw ra, 8(sp)
	addi sp, sp, 12
	ret
