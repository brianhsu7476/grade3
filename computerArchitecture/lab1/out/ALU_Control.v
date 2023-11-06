module ALU_Control(inst, ALUOp, ALUOp3);
input [9:0]inst;
input [1:0]ALUOp;
output [2:0]ALUOp3;
// 0:and 1:xor 2:sll 3:add 4:sub 5:mul 6:srai
assign ALUOp3=
	(ALUOp==2'b01&&inst[2:0]==3'b000)?3'd3:
	(ALUOp==2'b01)?3'd6:
	(inst==10'b0000000111)?3'd0:
	(inst==10'b0000000100)?3'd1:
	(inst==10'b0000000001)?3'd2:
	(inst==10'b0000000000)?3'd3:
	(inst==10'b0100000000)?3'd4:
	3'd5;
endmodule
