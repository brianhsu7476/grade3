module Sign_Extend(inst, res);
input [11:0]inst;
output [31:0]res;
assign res={{20{inst[11]}}, inst};
//assign res[11:0]=inst;
//assign res[31:12]=inst[11]?20'hfffff:20'h00000;
endmodule
