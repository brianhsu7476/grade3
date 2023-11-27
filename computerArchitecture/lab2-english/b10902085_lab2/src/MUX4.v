module MUX4(a0, a1, a2, sel, b);
input[31:0] a0, a1, a2;
input[1:0] sel;
output[31:0] b;

assign b=
	(sel==2'b00)?a0:
	(sel==2'b01)?a1:
	a2;

endmodule
