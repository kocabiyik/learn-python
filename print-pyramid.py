#  for n = 3, print:
#          +
#        + + +
#      + + + + +

def print_pyramid(n_lines: int = 15, symbol: str = '+'):
    """Prints a pyramid with the given symbol"""
    for line in range(0, n_lines * 2, 2):
        n_symbols = line + 1
        print((n_symbols * symbol).center(n_lines * 2))


print_pyramid(n_lines=10, symbol='x')
#          x
#         xxx
#        xxxxx
#       xxxxxxx
#      xxxxxxxxx
#     xxxxxxxxxxx
#    xxxxxxxxxxxxx
#   xxxxxxxxxxxxxxx
#  xxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxx