

class CartSession:
    def __init__(self,session):
        self.session = session
        self._cart = self.session.setdefault('cart', 
        {
            "items":[],
            "total_price":0,
            "total_item":0
        })

    
    def add_product(self, product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] += 1
                break
        else:
            new_item = {"product_id": product_id, "quantity": 1}
            self._cart["items"].append(new_item)
        
        # Update total item count
        self._cart["total_item"] = self.get_total_quantity()
        
        self.save()

            
    
    def clear(self):
        self.cart = self.session['cart']= {
            "items":[],
            "total_price":0,
            "total_item":0
        }
        self.save()
        
    def get_cart_dict(self):
        return self._cart

    def get_total_quantity(self):
        total_quantity = 0
        for item in self._cart['items']:
            total_quantity += item['quantity']
        return total_quantity
        
    def save(self):
        self.session.modified = True