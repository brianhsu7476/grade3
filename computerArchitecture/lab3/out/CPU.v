module CPU(clk_i, rst_i);
input clk_i, rst_i;

wire[31:0] pc0, pc1, pc2, pc3, pc4;
wire[31:0] inst0, inst1, inst2;
wire[31:0] imm0, imm1;
wire[6:0] ctrl0, ctrl1;
wire idbranch, exbranch, alu, pred, fail;
wire[3:0] ctrl2;
wire[1:0] ctrl3;
wire[4:0] memrd, wbrd;
wire pcwrite, stall, noop, flush;
wire[1:0] fa, fb;
wire[31:0] r10, r11, r12, r20, r21, r22, r23, r24;
wire[31:0] alu0, alu1, alu2, alu3, alu4;
wire[31:0] wbwd;
wire[2:0] aluop3;
wire[31:0] pc5, pc6, pc7;

MUX2 MUX0(pc1, pc3, pred, pc4);
PC PC(rst_i, clk_i, pcwrite, pc7, pc0);
Instruction_Memory Instruction_Memory(pc0, inst0);
Add Add0(pc0, 32'd4, pc1);
MUX2 MUX5(pc3, pc0, pred, pc5);
MUX2 MUX6(pc4, pc6, fail, pc7);

IFID IF_ID(rst_i, clk_i, pc0, inst0, flush, stall, pc2, inst1);

ImmGen ImmGen(inst1, imm0);
Add Add1(imm0, pc2, pc3);
HazardDetectionUnit Hazard_Detection(inst1[19:15], inst1[24:20], inst2[11:7], ctrl1[2], pcwrite, stall, noop);
Registers Registers(rst_i, clk_i, inst1[19:15], inst1[24:20], wbrd, wbwd, ctrl3[0], r10, r20);
Control Control(inst1[6:0], noop, ctrl0, idbranch);
//assign flush=r10==r20&&idbranch;
Predictor branch_predictor(rst_i, clk_i, idbranch, exbranch, alu, pred, fail, flush);

IDEX ID_EX(rst_i, clk_i, ctrl0, r10, r20, imm0, inst1, ctrl1, r11, r21, imm1, inst2, fail, idbranch, exbranch, pc5, pc6);

ForwardingUnit FU(inst2[19:15], inst2[24:20], wbrd, ctrl3[0], memrd, ctrl2[0], fa, fb);
MUX4 MUX1(r11, wbwd, alu1, fa, r12);
MUX4 MUX2(r21, wbwd, alu1, fb, r22);
MUX2 MUX3(r22, imm1, ctrl1[6], r23);
ALUControl ALUControl({inst2[31:25], inst2[14:12]}, ctrl1[5:4], aluop3);
ALU ALU(r12, r23, aluop3, alu0);
assign alu=alu0==32'b0;

EXMEM EXMEM(rst_i, clk_i, ctrl1[3:0], alu0, r22, inst2[11:7], ctrl2, alu1, r24, memrd);

Data_Memory Data_Memory(clk_i, alu1, ctrl2[2], ctrl2[3], r24, alu2);

MEMWB MEMWB(rst_i, clk_i, ctrl2[1:0], alu1, alu2, memrd, ctrl3, alu4, alu3, wbrd);

MUX2 MUX4(alu4, alu3, ctrl3[1], wbwd);

endmodule
