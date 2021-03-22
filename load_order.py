import sys


Order_format = '''
Order File format example:
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85
'''

def orderfile_error(msg, line, content):
    """ Returns error details if order is wrong """
    print(msg)
    print("Wrong line: {}, Content: '{}'".format(line, content.strip('\n')))
    print(Order_format)
    sys.exit(1)

def contains_item_from_array(line,TAX_EXEMPT):    
    for x in TAX_EXEMPT:
        if x in line:
            return 1
    return -1        

def load_order(order_file):
    orderlist = []
    with open(order_file, 'r') as order:
        data = order.readlines()
    for item in data:
        line = data.index(item) + 1
        try:
            input_list = item.strip('\n').split(' ')
        except ValueError:
            orderfile_error("ERROR: Order file format is broken.", line, item)
        quantity = int(input_list[0])
        if quantity < 1:
            orderfile_error("ERROR: Quantity cannot be less than 1.", line, item)
        if 'imported' in input_list:
            imported = 'true'
        else:
            imported = 'false' 
        TAX_EXEMPT = ['book', 'chocolate', 'pills'] 
        exempted_item_true = contains_item_from_array(input_list,TAX_EXEMPT) 
        price = float(input_list[-1])
        name = " ".join(input_list[1:-2])
        entity = (quantity,imported,name,price,exempted_item_true)
        orderlist.append(entity)
    return orderlist