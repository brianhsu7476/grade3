module Predictor(rst, clk, idbranch, exbranch, alu, pred, fail, flush);
input rst, clk, idbranch, exbranch, alu;
output pred, fail, flush;

wire predict_o;
wire[1:0] statei;
reg[1:0] state;

assign statei=exbranch?alu?
	(state==2'b11)?state:state+1:
	(state==2'b00)?state:state-1:
	state;
assign predict_o=state[1];
assign fail=exbranch&&alu!=predict_o;
assign pred=idbranch?fail?alu:predict_o:0;
assign flush=fail||pred;

always@(posedge clk or negedge rst)begin
	if(~rst)begin
		state<=2'b11;
	end
	else if(exbranch)begin
		state<=statei;
	end
end
endmodule
