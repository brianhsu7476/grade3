module MEMWB(rst, clk, ctrli, alu1i, alu2i, rdi, ctrlo, alu1o, alu2o, rdo);
input rst, clk;
input[1:0] ctrli;
input[31:0] alu1i, alu2i;
input[4:0] rdi;
output[1:0] ctrlo;
output[31:0] alu1o, alu2o;
output[4:0] rdo;

reg[1:0] ctrl;
reg[31:0] alu1, alu2, rd;

assign ctrlo=ctrl;
assign alu1o=alu1;
assign alu2o=alu2;
assign rdo=rd;

always@(posedge clk or negedge rst)begin
	if(~rst)begin
		ctrl<=2'b0;
		alu1<=32'b0;
		alu2<=32'b0;
		rd<=32'b0;
	end
	else begin
		ctrl[0]<=ctrli[0]&&rdi;
		ctrl[1]<=ctrli[1];
		alu1<=alu1i;
		alu2<=alu2i;
		rd<=rdi;
	end
end

endmodule
