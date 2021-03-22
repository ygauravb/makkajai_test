from math import ceil

TAX_BASIC = 10  # Basic tax on all goods except some 'specials'
TAX_IMPORT = 5

def tax_round(tax):
    rnd = 20
    return ceil(round(tax, 2) * rnd) / rnd

def calc_tax(item):
    tax = 0
    if item[-1] == -1:
        tax += TAX_BASIC
    if item[1] == 'true':
        tax += TAX_IMPORT
    percent_tax = tax / 100
    total_tax = item[3] * percent_tax
    result_tax = tax_round(total_tax)
    return result_tax

def print_receipt(cart):
    print("Output:")
    entities = []
    total_tax = 0
    cart_total = 0
    for item in cart:
        tax = calc_tax(item)
        total = round((item[3] + tax), 2)
        entities.append("{} {}: {:.2f}".format(item[0], item[2], total))
        total_tax+=tax_round(tax*item[0])
        cart_total+=item[3]*item[0]
    print("\n".join(entities))
    print("Sales Taxes: {0:.2f}".format(total_tax))
    print("Total: {0:.2f}".format(cart_total+total_tax))