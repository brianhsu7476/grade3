.globl __start

.rodata
    division_by_zero: .string "division by zero"

.text
__start:
    # Read first operand
    li a0, 5
    ecall
    mv s0, a0
    # Read operation
    li a0, 5
    ecall
    mv s1, a0
    # Read second operand
    li a0, 5
    ecall
    mv s2, a0

###################################
#  TODO: Develop your calculator  #
#                                 #
###################################
main:
    li a0, 0
    beq s1, a0, addition
    li a0, 1
    beq s1, a0, subtraction
    li a0, 2
    beq s1, a0, multiplication
    li a0, 3
    beq s1, a0, division
    li a0, 4
    beq s1, a0, minimum
    li a0, 5
    beq s1, a0, power
    li a0, 6
    beq s1, a0, factorial

addition:
    add s3, s0, s2
    jal x0, output

subtraction:
    sub s3, s0, s2
    jal x0, output
    
multiplication:
    mul s3, s0, s2
    jal x0, output

division:
    beq s2, x0, division_by_zero_except
    div s3, s0, s2
    jal x0, output

minimum:
    blt s0, s2, altb
    mv s3, s2
    jal x0, output
    altb:
        mv s3, s0
        jal x0, output

power:
    li s3, 1
    pfor:
        beq s2, x0, output
        li a0, 1
        and a1, s2, a0
        beq a1, x0, pforend
        mul s3, s3, s0
        pforend:
        srli s2, s2, 1
        mul s0, s0, s0
        jal x0, pfor

factorial:
    li s3, 1
    ffor:
        beq s0, x0, output
        mul s3, s3, s0
        addi s0, s0, -1
        jal x0, ffor

output:
    # Output the result
    li a0, 1
    mv a1, s3
    ecall

exit:
    # Exit program(necessary)
    li a0, 10
    ecall

division_by_zero_except:
    li a0, 4
    la a1, division_by_zero
    ecall
    jal zero, exit
