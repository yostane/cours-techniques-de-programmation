class CoffeeShop:
    def __init__(self):
        """__init__ est un constructeur"""
        self.name = ""
        self.stock_quantity = 0

    def open(self):
        pass

    def close(self):
        pass

    def renew_stock(self):
        """Ajotuer un café dans le stock"""
        self.stock_quantity += 1

    def serve(self):
        self.stock_quantity -= 1

    def __str__(self):
        """Représentation textuelle de chaque instance (str -> string)"""
        # f"{variable}" permet de mettre le contenu de la variable dans la chaine de caractères
        return f"name: {self.name} - stock: {self.stock_quantity}"


coffee_shop1 = CoffeeShop()
coffee_shop1.renew_stock()
coffee_shop1.name = "Café du coin"
print(coffee_shop1.stock_quantity, coffee_shop1.name)
print(coffee_shop1)

coffee_shop2 = CoffeeShop()
coffee_shop2.renew_stock()
coffee_shop2.name = "Café de la palce"
print(coffee_shop2.stock_quantity, coffee_shop2.name)
