module HazardDetectionUnit(rs1, rs2, rd, memread, pcwrite, Stall_o, noop);
input[4:0] rs1, rs2, rd;
input memread;
output pcwrite, Stall_o, noop;

assign Stall_o=memread&&(rs1==rd||rs2==rd)&&rd!=5'd0;
assign noop=Stall_o;
assign pcwrite=~Stall_o;

endmodule
