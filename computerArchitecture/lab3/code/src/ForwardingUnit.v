module ForwardingUnit(exrs1, exrs2, wbrd, wbregwrite, memrd, memregwrite, fa, fb);
input[4:0] exrs1, exrs2, wbrd, memrd;
input wbregwrite, memregwrite;
output[1:0] fa, fb;

assign fa=
	(memregwrite&&memrd!=5'd0&&memrd==exrs1)?2'b10:
	(wbregwrite&&wbrd!=5'd0&&wbrd==exrs1)?2'b01:
	2'b00;
assign fb=
	(memregwrite&&memrd!=5'd0&&memrd==exrs2)?2'b10:
	(wbregwrite&&wbrd!=5'd0&&wbrd==exrs2)?2'b01:
	2'b00;

endmodule
