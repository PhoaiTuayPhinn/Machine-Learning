class Product:
    def __init__(self,id=None,name=None,quantity=None,price=None):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price

    def __str__(self):
        infor="{}\t{}\t{}\t{}".format(self.id,self.name,self.quantity,self.price)
        return infor

class ListProduct(Product):
    def __init__(self, id=None, name=None, quantity=None, price=None):
        super().__init__(id, name, quantity, price)
        self.list=[]
    def add_product(self,product):
        self.list.append(product)
    def print_products(self):
        for p in self.list:
            print(p)
    def sort_desc_price(self):
        for i in range(0,len(self.list)):
            for j in range(i+1,len(self.list)):
                pi=self.list[i].price
                pj=self.list[j].price
                if pi<pj:
                    self.list[i],self.list[j]=self.list[j],self.list[i]
        

