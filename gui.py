import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


class Product: 


    quantities = {}


    def __init__(self, name, price_sale, price_purchase, barcode, amount, type_price):
        self.name = name                        
        self.price_sale = price_sale
        self.price_purchase = price_purchase
        self.barcode = barcode 
        self.amount = amount 
        self.type_price = type_price 


    def product_amounts(self, id_):
        """The purpose of this method is to create an inventory
                with products referenced by an id. """
        product_amount = self.amount
        Product.quantities[id_] = product_amount


    def get_quantities(self):
        return self.quantities 

class Store(Product):


    sales = []
    purchases = [] 
    inventory = Product.quantities


    def __init__(self, employees, num_products, size):
        self.employees = employees
        self.num_products = num_products
        self.size = size 


    def sell(self, quantity, date, id_, sale_price_):
        new_sale = {}

        if quantity <= Store.inventory.get([id_]):
            new_sale['_id_'] = id_
            new_sale['sale_price'] = sale_price_
            new_sale['date_'] = date
            new_sale['quantity_'] = quantity

            Store.sales.append(new_sale) 

            Store.inventory[id_] -= quantity

        return 'Sorry, we ran out of this product' 


    def buy(self, quantity, date, id_, purchase_price_):
        new_purchase = {}
        
        new_purchase['_id_'] = id_ 
        new_purchase['purchase_price'] = purchase_price_ 
        new_purchase['date'] = date
        new_purchase['quantity'] = quantity 
        
        Store.purchases.append(new_purchase) 
        Store.inventory[id_] += quantity 


    def get_inventory(self):
        return self.inventory 

def least_sold(sales):
    
    freq = {} 

    for sale in sales: 
        id_ = sale['id_']
        freq[id_] = freq.get(id_, 0) + 1 

    min_ = float('inf') 
    min_id_ = " " 

    for prod_id_, count in freq.items():
        if count <= min_:
            min_ = count 
            min_id_ = prod_id_ 

    return min_id_ 
    

def most_sold(sales):
    
    freq = {} 

    for sale in sales: 
        id_ = sale['id_']
        freq[id_] = freq.get(id_, 0) + 1 

    max_ = 0 
    max_id_ = " " 

    for prod_id_, count in freq.items():
        if count >= max_:
            max_ = count 
            max_id_ = prod_id_ 

    return max_id_ 


def most_common_hour(sales):
    freq = {} 

    for sale in sales: 
        date = sale['date']
        hour = date.hour 
        freq[hour] = freq.get(hour, 0) + 1 

    max_ = 0 
    max_hour_ = " " 

    for hour, count in freq.items():
        if count >= max_:
            max_ = count 
            max_hour_ = hour 

    return max_hour_ 


def most_common_day(sales):
    freq = {} 

    for sale in sales: 
        date = sale['date']
        day = date.day 
        freq[day] = freq.get(day, 0) + 1 

    max_ = 0 
    max_day_ = " " 

    for day, count in freq.items():
        if count >= max_:
            max_ = count 
            max_day_ = day 

    return max_day_ 


def max_num_sales(sales):
    freq = {}
    
    for sale in sales:
        id_ = sale['id_'] 
        freq[id_] += freq.get(id_, 0) + sale['quantity'] 

    max_ = 0 
    max_id_ = ' '

    for prod_id_, count in freq.items():
        if count >= max_: 
            max_ = count 
            max_id_ = prod_id_ 

    return max_id_ + ':' + max_ 


def min_num_sales(sales):
    freq = {}
    
    for sale in sales:
        id_ = sale['id_'] 
        freq[id_] += freq.get(id_, 0) + sale['quantity'] 

    min_ = float('inf')
    min_id_ = ' '

    for prod_id_, count in freq.items():
        if count <= min_: 
            min_ = count 
            min_id_ = prod_id_ 

    return min_id_ + ':' + min_ 


def reorder(id_, reorder, inventory, product_reorder):

    product_reorder[id_] = reorder 
    
    if inventory.get(id_) <= product_reorder.get(id_): 
        print('You should order more items of this product, press 6 and follow instructions')
    
   
def total_spent(purchases):

    spent_product = {}

    for purchase in purchases: 
        price = purchase['price_purchase_'] 
        id_ = purchase['id_']
        spent_product[id_] = spent_product.get(id_, 0) + price 

    return spent_product 


def total_gained(sales):

    gained_product = {}

    for sale in sales: 
        price = sale['price_sale_'] 
        id_ = sale['id_']
        gained_product[id_] = gained_product.get(id_, 0) + price 

    return gained_product 

def total_profit(gained_product, spent_product):

    profit_product = {} 

    for id_ in gained_product:  
        profit_product[id_] = gained_product[id_] - spent_product.get(id_, 0) + 0 

    return profit_product
 
print('Hello, world')
window = tkinter.Tk()

window.title("ShopManager")

window.geometry('400x600')

label = tkinter.Label(window, text="ShopManager", fg="blue", font =('Arial Bold', 43))
label.grid(column=2, row=0)

def accion(): 
    current = combobox.get()

    if  current == 'Register product':
        label1.set('Name')
        label2.set('Price sale')
        label3.set('Price purchase')
        label4.set('Barcode')
        label5.set('Amount')
        label6.set('Type of price (weight, unit)')

        name = entry1.get()
        price_sale = entry2.get()
        price_purchase = entry3.get()
        barcode = entry4.get()
        amount = entry5.get()
        type_price = entry6.get()


        p1 = Product(name, price_sale, price_purchase, barcode, amount, type_price)


    elif current == 'Amount-Product':
        label1.set('Product ID')
        label2.set('No pongas nada')
        label3.set('No pongas nada')
        label4.set('No pongas nada')
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        id_ = entry1.get()

        p1.product_amounts(id_)


    elif current == 'Amount':
        label1.set('No pongas nada')
        label2.set('No pongas nada') 
        label3.set('No pongas nada')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        print(p1.quantities)

    elif current == 'Register store':
        label1.set('Num employees')
        label2.set('Num products') 
        label3.set('Size')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        employees = entry1.get()
        num_products = entry2.get()
        size = entry3.get()
        
        s1 = Store(employees, num_products, size)

    elif current == 'Sell': 
        label1.set('Amount')
        label2.set('Product ID') 
        label3.set('Price sale')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        quantity = entry1.get()
        date = datetime.now()
        id_ = entry2.get()
        sale_price_ = entry3.get()

        s1.sell(quantity, date, id_, sale_price_)

    elif current == 'Buy':
        label1.set('Amount')
        label2.set('Product ID') 
        label3.set('Price purchase')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        quantity = entry1.get()
        date = datetime.now()
        id_ = entry2.get()
        purchase_price_ = entry3.get() 

        s1.buy(quantity, date, id_, purchase_price_)


    elif current == 'Inventory':
        label1.set('No pongas nada')
        label2.set('No pongas nada') 
        label3.set('No pongas nada')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        print(s1.inventory)

    elif current == 'Least sales-product':
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        print(least_sold(sales)) 

    elif current == 'Most sales-product': 
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        print(most_sold(sales)) 


    elif current == 'Most common hour':
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        print(most_common_hour(sales)) 

    elif current == 'Most common day':
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        print(most_common_day(sales)) 

    elif current == 'Most products sold':
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        print(max_num_sales(sales)) 

    elif current == 'Least products sold':
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        print(min_num_sales(sales)) 

    elif current == 'Reorder':
        label1.set('Product ID')
        label2.set('Reorder') 
        label3.set('No pongas nada')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        id_ = entry1.get()
        reorder = entry2.get() 

        reorder(id_, reorder)

    elif current == 'Spent':
        label1.set('Product ID')
        label2.set('Price purchase') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_purchase_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        
        spent_product = total_spent(sales)
        print(spent_product) 

    elif current == 'Gained':
        label1.set('Product ID')
        label2.set('Price sale') 
        label3.set('Amount')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        sales = {}
        sales['id_'] = entry1.get()
        sales['price_sale_'] = entry2.get()
        sales['date'] = datetime.now() 
        sales['quantity'] = entry3.get()

        gained_product = total_gained(sales)
        print(gained_product)

    elif current == 'Profit': 

        label1.set('No pongas nada')
        label2.set('No pongas nada') 
        label3.set('No pongas nada')
        label4.set('No pongas nada') 
        label5.set('No pongas nada')
        label6.set('No pongas nada')

        print(total_profit(gained_product, spent_product))


combobox = ttk.Combobox(window)
combobox['values'] = ('Register product','Quantity-Product','Quantity','Register store','Sell','Buy','Inventory','Least sales-product','Most sales-product','Most common hour','Most common day','Most products sold','Least products sold','Reorder', 'Spent','Gained','Profit')
combobox.grid(column=2, row=2) 

entry1 = tkinter.StringVar() 
entry2 = tkinter.StringVar()
entry3 = tkinter.StringVar() 
entry4 = tkinter.StringVar()
entry5 = tkinter.StringVar()
entry6 = tkinter.StringVar()

label1 = tkinter.StringVar()
label2 = tkinter.StringVar()
label3 = tkinter.StringVar()
label4 = tkinter.StringVar()
label5 = tkinter.StringVar()
label6 = tkinter.StringVar()


tkinter.Entry(textvariable=entry1, width='50').grid(column=2, row=15)
tkinter.Entry(textvariable=entry2, width='50').grid(column=2, row=25) 
tkinter.Entry(textvariable=entry3, width='50').grid(column=2, row=35) 
tkinter.Entry(textvariable=entry4, width='50').grid(column=2, row=45) 
tkinter.Entry(textvariable=entry5, width='50').grid(column=2, row=55) 
tkinter.Entry(textvariable=entry6, width='50').grid(column=2, row=65) 

tkinter.Label(window, textvariable=label1).grid(column=2, row=10)
tkinter.Label(window, textvariable=label2).grid(column=2, row=20) 
tkinter.Label(window, textvariable=label3).grid(column=2, row=30) 
tkinter.Label(window, textvariable=label4).grid(column=2, row=40) 
tkinter.Label(window, textvariable=label5).grid(column=2, row=50) 
tkinter.Label(window, textvariable=label6).grid(column=2, row=60) 


btn = ttk.Button(window, text = 'Get value', command=accion) 
btn.grid(column=2, row=5)


window.mainloop()