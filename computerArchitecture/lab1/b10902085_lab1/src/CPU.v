module CPU
(
    clk_i, 
    rst_i,
);

// Ports
input               clk_i;
input               rst_i;

wire [31:0]pc_i, pc_o, inst, ALUres, rs1, rs2, ext, rs3;
wire ALUSrc, RegWrite, Zero;
wire [1:0]ALUOp;
wire [2:0]ALUOp3;
wire [9:0]ALUinst;

assign ALUinst[9:3]=inst[31:25];
assign ALUinst[2:0]=inst[14:12];

Control Control(inst[6:0], ALUOp, ALUSrc, RegWrite);

Adder Add_PC(pc_o, 32'd4, pc_i);

PC PC(clk_i, rst_i, pc_i, pc_o);

Instruction_Memory Instruction_Memory(pc_o, inst);

Registers Registers(rst_i, clk_i, inst[19:15], inst[24:20], inst[11:7], ALUres, RegWrite, rs1, rs2);

MUX32 MUX_ALUSrc(rs2, ext, ALUSrc, rs3);

Sign_Extend Sign_Extend(inst[31:20], ext);
  
ALU ALU(rs1, rs3, ALUOp3, ALUres, Zero);

ALU_Control ALU_Control(ALUinst, ALUOp, ALUOp3);

endmodule

