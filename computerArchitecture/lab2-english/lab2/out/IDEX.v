module IDEX(rst, clk, ctrli, r1i, r2i, immi, insti, ctrlo, r1o, r2o, immo, insto);
input rst, clk;
input[6:0] ctrli;
input[31:0] r1i, r2i, immi, insti;
output[6:0] ctrlo;
output[31:0] r1o, r2o, immo, insto;

reg[6:0] ctrl;
reg[31:0] r1, r2, imm, inst;
assign ctrlo=ctrl;
assign r1o=r1;
assign r2o=r2;
assign immo=imm;
assign insto=inst;

always@(posedge clk or negedge rst)begin
	if(~rst)begin
		ctrl<=6'b0;
		r1<=32'b0;
		r2<=32'b0;
		imm<=32'b0;
		inst<=32'b0;
	end
	else begin
		ctrl<=ctrli;
		r1<=r1i;
		r2<=r2i;
		imm<=immi;
		inst<=insti;
	end
end
endmodule
