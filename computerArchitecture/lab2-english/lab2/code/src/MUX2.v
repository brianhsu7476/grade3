module MUX2(a0, a1, sel, b);
input[31:0] a0, a1;
input sel;
output[31:0] b;

assign b=sel?a1:a0;

endmodule
