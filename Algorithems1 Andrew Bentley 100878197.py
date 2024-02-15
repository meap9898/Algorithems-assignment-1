class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Category: {self.category}"


class ProductManager:
    def __init__(self):
        self.products = []

    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = Product(int(data[0]), data[1], float(data[2]), data[3])
                self.products.append(product)

    def store_data(self, file_path):
        with open(file_path, 'w') as file:
            for product in self.products:
                file.write(f"{product.product_id},{product.name},{product.price},{product.category}\n")

    def insert_product(self, product):
        self.products.append(product)
        Inputfile = open("product_data.txt", "a")
        Inputfile.write(f"{product.product_id},{product.name},{product.price},{product.category}\n")
        Inputfile.close()

    def update_product(self, product_id, new_price):
        for product in self.products:
            if product.product_id == product_id:
                product.price = new_price

    def delete_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]
        with open("product_data.txt", "r") as f:
            lines = f.readlines()
        with open("product_data.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != productid:
                    f.write(line)

    def search_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def search_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def bubble_sort_by_price(self):
        n = len(self.products)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.products[j].price > self.products[j + 1].price:
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]
                    print(f"Swapping {self.products[j].price} and {self.products[j + 1].price}")


    def print_products(self):
        for product in self.products:
            print(product)


# Test the implementation
if __name__ == "__main__":
    while(True):
        scanner = input("Read R, Write W, Delete D, Update U, Sort SO, Search SE, Exit to exit the program")
        manager = ProductManager()
        manager.load_data("product_data.txt")

        if(scanner == "R"):
            print("Original Products:")
            manager.print_products()
        elif(scanner == "SO"):
            print("\nSorting Products by Price (Bubble Sort):")
            manager.bubble_sort_by_price()
            manager.print_products()
        elif(scanner == "SE"):
            print("\nSearching for a Product by ID:")
            productid = int(input("enter product id"))
            found_product = manager.search_product_by_id(productid)
            if found_product:
                print("Found Product:", found_product)
            else:
                print("Product not found.")
        elif(scanner == "W"):
            print("\nInserting a New Product:")
            productid = int(input("enter product id"))
            product = input("Enter the name if the product")
            price = float(input("enter the name of the price"))
            category = input("enter the category")
            new_product = Product(productid, product, price, category)
            manager.insert_product(new_product)
            manager.print_products()
        elif(scanner == "U"):
            print("\nUpdating Product Price:")
            productid = int(input("enter product id"))
            price = float(input("enter the new price"))
            manager.update_product(productid, price)
            manager.print_products()
        elif(scanner == "D"):
            print("\nDeleting a Product:")
            productid = int(input("enter product id"))
            manager.delete_product(productid)
            manager.print_products()
        elif(scanner == "Exit"):
            break
        else:
            print("invalid")

        manager.store_data("product_data.txt")
