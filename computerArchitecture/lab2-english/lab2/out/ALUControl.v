module ALUControl(inst, aluop, aluop3);
input[9:0] inst;
input[1:0] aluop;
output[2:0] aluop3;

// 0:and 1:xor 2:sll 3:add 4:sub 5:mul 6:srai
assign aluop3=
	(aluop==2'b11&&inst[2:0]==3'b000)?3'd3: // addi
	(aluop==2'b11&&inst[2:0]==3'b101)?3'd6: // srai
	(aluop==2'b00||inst==10'b0000000000)?3'd3:
	(aluop==2'b01||inst==10'b0100000000)?3'd4:
	(inst==10'b0000000111)?3'd0:
	(inst==10'b0000000100)?3'd1:
	(inst==10'b0000000001)?3'd2:
	3'd5;

endmodule
