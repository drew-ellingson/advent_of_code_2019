class IntCode():
    def __init__(self, input_list):
        self.input_list = input_list
        self.current_list = input_list
        self.current_op = 0
        self.output = 0
        self.input = 0

    '''return the immediate or position value depending on mode in [0,1]'''
    def im_pos(self, il, pos, mode):
        return il[il[pos]] if mode == 0 else il[pos]

    '''transform the instruction to remove the immedate/position mode logic'''
    def make_instruction(self, il, op):
        input_string = '{0:05d}'.format(il[op])
        op_code = int(input_string[-2:])

        # last param will always be position mode
        if op_code in [1, 2, 7, 8]:
            new_params = [self.im_pos(il, op+1, int(input_string[2])),
                        self.im_pos(il, op+2, int(input_string[1])),
                        il[op+3]]
        # write-to param always in position mode
        elif op_code == 3:
            new_params = [il[op+1]]
        elif op_code == 4:
            new_params = [self.im_pos(il, op+1, int(input_string[2]))]
        elif op_code in [5, 6]:
            new_params = [self.im_pos(il, op+1, int(input_string[2])),
                        self.im_pos(il, op+2, int(input_string[1]))]
        return op_code, new_params

    '''perform one operation'''
    def one_step(self):
        il = self.current_list 
        op = self.current_op 

        op_code, params = self.make_instruction(il, op)
        if op_code == 1:
            il[params[2]] = params[0] + params[1]
            op += 4
        elif op_code == 2:
            il[params[2]] = params[0] * params[1]
            op += 4
        elif op_code == 3:
            inst_input = self.input
            il[params[0]] = inst_input
            op += 2
        elif op_code == 4:
            self.output = params[0]
            op += 2
        elif op_code == 5:
            op = params[1] if params[0] != 0 else op + 3
        elif op_code == 6:
            op = params[1] if params[0] == 0 else op + 3
        elif op_code == 7:
            il[params[2]] = 1 if params[0] < params[1] else 0
            op += 4
        elif op_code == 8:
            il[params[2]] = 1 if params[0] == params[1] else 0
            op += 4
        self.current_list = il 
        self.current_op = op

        return il, op
