#import classes 
import CustomerClass as cc
import CarClass as c 
import ServiceQuoteClass as sqc


#get info from customer 
name = input(f'Customer Name: ').title()
address = input(f'Customer Address: ').title()
phone = input(f'Customer Phone Number: ')

make = input(f'Car Make: ').title()
model = input(f'Car Model: ').title()
year = input(f'Car Year: ')
 

pcharge = int(input(f'Parts Charges: $'))
lcharge = int(input(f'Labor Chargers: $'))


#create objects 
customer = cc.Customer(name,address,phone) 
car = c.Car(make,model,year) 
costs = sqc.ServiceQuote(pcharge,lcharge)


#call the calculation set methods
costs.set_sales_tax(pcharge,lcharge)
costs.set_total_charges(pcharge,lcharge)


#output 
print(f'-------------------------------------------')
print(f'              SERVICE QUOTE                ')
print(f'-------------------------------------------\n')
print(f'CUSTOMER INFORMATION')
print(f'Customer: {customer.get_name()}')
print(f'Address: {customer.get_address()}')
print(f'Phone Number: {customer.get_phone()}\n')
print(f'CUSTOMER CAR')
print(f'Make: {car.get_make()}')
print(f'Model: {car.get_model()}')
print(f'Year: {car.get_year()}\n')
print(f'ESTIMATED COSTS')
print(f'Estimated Parts Charge: ${costs.get_parts_charges()}')
print(f'Estimated Labor Charge: ${costs.get_parts_charges()}')
print(f'Sales Tax: ${costs.get_sales_tax():,.2f}')
print(f'Estimated Total: ${costs.get_total_charges():,.2f}\n')




