from review.product import Product
from review.product import ListProduct

lp=ListProduct()
lp.add_product(Product("p1","coca","20","79"))
lp.add_product(Product("p2","pepsi","20","65"))
lp.add_product(Product("p3","sting","10","70"))
lp.add_product(Product("p4","redbull","25","75"))

lp.sort_desc_price()
print("--List Products - Sort Desc Price:-------")
lp.print_products()


