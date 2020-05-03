from itertools import permutations
import intcode

def thrust_calc(verbose=False):
    with open('input.txt') as my_file:
        input_list = list(map(lambda x: int(x), my_file.readline().split(',')))

    phase_orders = list(permutations(range(0,5)))

    max_thruster = 0

    for phase_order in phase_orders:
        outputs = []
        for x in phase_order:
            inst = intcode.IntCode(input_list)
            loop = 0
            first_input = True
            
            while inst.current_list[inst.current_op] != 99:
                if inst.current_list[inst.current_op] == 3:
                    if first_input:
                        inst.input = x
                        first_input = False
                    else:
                        try:
                            inst.input = outputs[-1]
                        except IndexError:
                            inst.input = 0
                
                if verbose:
                    print('step {}'.format(loop))
                    print('Starting list is \n{} \nwith operation index {}'.format(inst.current_list, inst.current_op))
                
                inst.one_step()
                
                if verbose:
                    print('Ending list is \n{} \nwith operation index {}'.format(inst.current_list, inst.current_op))
                    print('\n\n')
                loop += 1
            outputs.append(inst.output)
        max_thruster = max(max_thruster, outputs[-1])
    return max_thruster

if __name__ == '__main__':
    max_thrust = thrust_calc(verbose=False)
    print(max_thrust)