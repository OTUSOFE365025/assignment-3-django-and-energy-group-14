import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Product

# Add products (reset each time)
Product.objects.all().delete()
Product.objects.create(upc="1001", name="Milk", price=2.99)
Product.objects.create(upc="1002", name="Mango", price=1.99)
Product.objects.create(upc="1003", name="Cookies", price=3.49)
Product.objects.create(upc="1004", name="Shampoo", price=4.99)
Product.objects.create(upc="1005", name="Carrot", price=1.49)

print("Available products:")
for p in Product.objects.all():
    print(p.upc, p.name, p.price)

while True:
    upc = input("Enter product UPC (or type 'done' to finish): ").strip()
    if upc.lower() == "done":
        print("Done.")
        break
    try:
        product = Product.objects.get(upc=upc)
        print("Product:", product.name)
        print("Price: $", product.price)
    except Product.DoesNotExist:
        print("Product not found, please try again.")
