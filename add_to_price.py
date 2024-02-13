import random

"""If one would want to change the initial condition of the transformation from produkter.txt to products.txt"""

PRICE_LOWER_LIMIT = 20
PRICE_UPPER_LIMIT = 2000
IN_STOCK_LOWER_LIMIT = 5000
IN_STOCK_UPPER_LIMIT = 40000
FILE_NAME = "produkter.txt"

dict_of_products= {}

num_of_prod = 0

with open(FILE_NAME, "r", encoding='utf-8') as f:
    for prod in f.readlines():
        num_of_prod +=1 
        p = prod.strip().strip("(").strip(")").strip("\n").replace(" ","")
        new_prod = tuple(
            p.split(",") + \
            [str(random.randint(PRICE_LOWER_LIMIT,PRICE_UPPER_LIMIT))] + \
            [str(random.randint(IN_STOCK_LOWER_LIMIT,IN_STOCK_UPPER_LIMIT))])
        dict_of_products[num_of_prod] = new_prod

with open("products.txt", "w", encoding="utf-8") as f:
    for key,value in dict_of_products.items():
        f.write(str(value)+ '\n')