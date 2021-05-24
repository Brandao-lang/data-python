

open_file = open('CupcakeInvoices.csv')


# for line in open_file:
#     print(line)

# for type in open_file:
#     type = type.split(',')
#     print(type[2])

invoices = []

for line in open_file:
    line = line.split(',')
    quantity = int(line[3])
    price = float(line[4])
    total = quantity * price
    invoices.append(total)
    print(f'${total}')

print(f'total price of all cupcakes: ${sum(invoices)}')
