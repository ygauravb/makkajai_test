import sys

from load_order import load_order
from PrintReceipt import print_receipt

# input instructions
input_format = '''
Input format:
    python3 sales_taxes.py [test_case_file]\n
Example:
    python3 sales_taxes.py test_case1.txt
'''
Order_format = '''
Order File format example:
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85
'''

def main():
    order = []
    if len(sys.argv) > 1:
        order = load_order(sys.argv[1])
    else:
        print("\nSales Taxes Problem.\n")
        print(input_format)
        sys.exit(0)
    if len(order) < 1:
        print("ERROR: Order is empty")
        print(Order_format)
        sys.exit(1)
    print_receipt(order)
  
if __name__ == "__main__":
    main()
