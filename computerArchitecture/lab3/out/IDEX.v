module IDEX(rst, clk, ctrli, r1i, r2i, immi, insti, ctrlo, r1o, r2o, immo, insto, fail, branchi, Branch_o, pci, pco);
input rst, clk, fail, branchi;
input[6:0] ctrli;
input[31:0] r1i, r2i, immi, insti, pci;
output[6:0] ctrlo;
output[31:0] r1o, r2o, immo, insto, pco;
output Branch_o;

reg[6:0] ctrl;
reg[31:0] r1, r2, imm, inst, pc;
reg branch;
assign ctrlo=ctrl;
assign r1o=r1;
assign r2o=r2;
assign immo=imm;
assign insto=inst;
assign Branch_o=branch;
assign pco=pc;

always@(posedge clk or negedge rst)begin
	if(~rst||fail)begin
		ctrl<=6'b0;
		r1<=32'b0;
		r2<=32'b0;
		imm<=32'b0;
		inst<=32'b0;
		branch<=1'b0;
		pc<=32'b0;
	end
	else begin
		ctrl<=ctrli;
		r1<=r1i;
		r2<=r2i;
		imm<=immi;
		inst<=insti;
		branch<=branchi;
		pc<=pci;
	end
end
endmodule
