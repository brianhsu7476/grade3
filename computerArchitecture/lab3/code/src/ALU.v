module ALU(a, b, op, data_o);
input signed[31:0] a, b;
input[2:0] op;
output[31:0] data_o;
// 0:and 1:xor 2:sll 3:add 4:sub 5:mul 6:srai
assign data_o=
	(op==3'd0)?a&b:
	(op==3'd1)?a^b:
	(op==3'd2)?a<<b:
	(op==3'd3)?a+b:
	(op==3'd4)?a-b:
	(op==3'd5)?a*b:
	a>>>b[4:0];
endmodule
