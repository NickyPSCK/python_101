import argparse

# https://docs.python.org/3/library/argparse.html
# --------------------------------------------------------------------------------------------------------
# INPUT ARGUMENTS
# --------------------------------------------------------------------------------------------------------
def input_argument():

    # Init ArgumentParser object
    parser = argparse.ArgumentParser(description='Example program to calculate the sum between two numbers')

    # Add arguments
    parser.add_argument('--num1', metavar='num1', action='store', type=int, default=1,
                            help='Input integer numbers e.g. 1 (Default: 1)')

    parser.add_argument('--num2', metavar='num2', action='store', type=int, default=2,
                            help='Input integer numbers e.g. 2 (Default: 2)')

    parser.add_argument('--sum', metavar='sum', type=bool, default=False,
                            help='''
                                    Calculate the sum between input numbers.          
                                    (Default: False)  ''') 


    args = parser.parse_args()
    args_dict = vars(args)

    return args_dict


# --------------------------------------------------------------------------------------------------------
# RUN
# --------------------------------------------------------------------------------------------------------
def run(args_dict:dict):

    if args_dict['sum']:
        total = args_dict['num1'] + args_dict['num2']
        print(f"The result is {total}")
    else:
        print(f"Your input is {args_dict['num1']}, {args_dict['num2']}")


if __name__ == '__main__':
    args_dict = input_argument()
    run(args_dict)