from shop.models import ProductModel, ProductStatusType

class CartSession:
    def __init__(self, session):
        self.session = session
        self._cart = self.session.setdefault('cart', {
            "items": [],
            "total_price": 0,
            "total_item": 0
        })

    def update_product_quantity(self,product_id,quantity):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] = int(quantity)
                break
        else:
            return
        self.save()
        
    def remove_product(self, product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                self._cart['items'].remove(item)
                break
        else:
            return
        self.save()
    
    def add_product(self, product_id):
        item = next((item for item in self._cart["items"] if item["product_id"] == product_id), None)
        
        if item:
            item["quantity"] += 1
        else:
            self._cart["items"].append({"product_id": product_id, "quantity": 1})
        
        self._cart["total_item"] = self.get_total_quantity()
        self.save()
    
    def clear(self):
        self.session['cart'] = {"items": [], "total_price": 0, "total_item": 0}
        self.save()
    
    def get_cart_dict(self):
        return self._cart
    
    def get_cart_items(self):
        total_payment_price = 0
        
        for item in self._cart['items']:
            product_obj = self._get_product(item['product_id'])
            if product_obj:
                item['product_obj'] = product_obj
                item['total_price'] = item['quantity'] * product_obj.get_price()
                total_payment_price += item['total_price']
        
        return self._cart['items']
    
    def get_total_payment_price(self):
        return sum(
            item['quantity'] * self._get_product(item['product_id']).get_price()
            for item in self._cart['items']
            if self._get_product(item['product_id'])
        )

    def get_total_quantity(self):
        return sum(item['quantity'] for item in self._cart['items'])
    
    def save(self):
        self.session.modified = True
    
    def _get_product(self, product_id):
        """Helper method to fetch a product with published status."""
        return ProductModel.objects.filter(id=product_id, status=ProductStatusType.publish.value).first()
