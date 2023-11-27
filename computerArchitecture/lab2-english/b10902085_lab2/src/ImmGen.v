module ImmGen(inst, res);
input[31:0] inst;
output[31:0] res;

wire[9:0] func;
assign func={inst[14:12], inst[6:0]};
assign res=
	(func==10'b0000010011)?{{20{inst[31]}}, inst[31:20]}: // addi
	(func==10'b1010010011)?{27'b0, inst[24:20]}: // srai
	(func==10'b0100000011)?{{20{inst[31]}}, inst[31:20]}: // lw
	(func==10'b0100100011)?{{20{inst[31]}}, inst[31:25], inst[11:7]}: // sw
	{{19{inst[31]}}, inst[31], inst[7], inst[30:25], inst[11:8], 1'b0}; // beq
endmodule
