module IFID(rst, clk, pci, insti, flush_i, stall, pco, insto);

input rst, clk, flush_i, stall;
input[31:0] pci, insti;
output[31:0] pco, insto;

reg[31:0] pc, inst;
assign insto=inst;
assign pco=pc;

always@(posedge clk or negedge rst)begin
	if(~rst)begin
		pc<=32'b0;
		inst<=32'b0;
	end
	else if(flush_i)begin
		inst<=32'b0;
	end
	else if(~stall)begin
		inst<=insti;
		pc<=pci;
	end
end
endmodule
