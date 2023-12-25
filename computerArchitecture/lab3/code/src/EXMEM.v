module EXMEM(rst, clk, ctrli, alui, r2i, insti, ctrlo, aluo, r2o, insto);
input rst, clk;
input[3:0] ctrli;
input[31:0] alui, r2i;
input[4:0] insti;
output[3:0] ctrlo;
output[31:0] aluo, r2o;
output[4:0] insto;

reg[3:0] ctrl;
reg[31:0] alu, r2;
reg[4:0] inst;
assign ctrlo=ctrl;
assign aluo=alu;
assign r2o=r2;
assign insto=inst;

always@(posedge clk or negedge rst)begin
	if(~rst)begin
		ctrl<=4'b0;
		alu<=32'b0;
		r2<=32'b0;
		inst<=5'b0;
	end
	else begin
		ctrl<=ctrli;
		alu<=alui;
		r2<=r2i;
		inst<=insti;
	end
end


endmodule
