module Control(inst, ALUOp, ALUSrc, RegWrite);
input [6:0]inst;
output [1:0]ALUOp;
output ALUSrc;
output RegWrite;
assign ALUOp[1:0]=inst[5:4];
assign ALUSrc=~inst[5];
assign RegWrite=1'b1;
endmodule
