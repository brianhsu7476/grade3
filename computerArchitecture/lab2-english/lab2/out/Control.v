module Control(inst, noop, ctrl, Branch_o);
input[6:0] inst;
input noop;
output[6:0] ctrl;
output Branch_o;

wire[7:0] out;

// aluop, alusrc, branch, memread, memwrite, regwrite, memtoreg
assign out=
	(inst==7'b0000000||noop)?8'b00000000:
	(inst==7'b0110011)?8'b10000010: // add
	(inst==7'b0010011)?8'b11100010: // addi
	(inst==7'b0000011)?8'b00101011: // lw
	(inst==7'b0100011)?8'b00100100: // sw
	8'b01010000; // beq
assign ctrl[5:4]=out[7:6];
assign ctrl[6]=out[5];
assign Branch_o=out[4];
assign ctrl[2]=out[3];
assign ctrl[3]=out[2];
assign ctrl[0]=out[1];
assign ctrl[1]=out[0];
endmodule
