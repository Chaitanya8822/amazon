"""
Run this script to seed the database with sample categories and products.
Usage: python manage.py shell < seed_data.py
  OR:  python seed_data.py  (if DJANGO_SETTINGS_MODULE is set)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon_project.settings')
django.setup()

from products.models import Category, Product
from django.utils.text import slugify

print("Seeding categories...")

categories_data = [
    {'name': 'Electronics', 'description': 'Gadgets, phones, laptops and more'},
    {'name': 'Books', 'description': 'Fiction, non-fiction, textbooks and more'},
    {'name': 'Fashion', 'description': 'Clothing, shoes, and accessories'},
    {'name': 'Home & Kitchen', 'description': 'Appliances, cookware, and décor'},
    {'name': 'Sports & Fitness', 'description': 'Equipment, clothing, and accessories'},
    {'name': 'Toys & Games', 'description': 'Fun for all ages'},
]

categories = {}
for c in categories_data:
    obj, created = Category.objects.get_or_create(
        slug=slugify(c['name']),
        defaults={'name': c['name'], 'description': c['description']}
    )
    categories[c['name']] = obj
    print(f"  {'Created' if created else 'Exists'}: {obj.name}")

print("\nSeeding products...")

products_data = [
    # Electronics
    {'name': 'Samsung Galaxy S24', 'category': 'Electronics', 'price': 79999, 'discount_price': 69999, 'stock': 25, 'featured': True,
     'description': 'Samsung Galaxy S24 with 6.2" Dynamic AMOLED display, 50MP camera, and Snapdragon 8 Gen 3 processor. Experience next-level performance and stunning photography.'},
    {'name': 'Apple iPhone 15', 'category': 'Electronics', 'price': 89999, 'discount_price': 84999, 'stock': 15, 'featured': True,
     'description': 'iPhone 15 with A16 Bionic chip, 6.1" Super Retina XDR display, and 48MP main camera. USB-C connector for universal compatibility.'},
    {'name': 'Sony WH-1000XM5 Headphones', 'category': 'Electronics', 'price': 29990, 'discount_price': 24990, 'stock': 40, 'featured': True,
     'description': 'Industry-leading noise canceling headphones with 30-hour battery life, multipoint connection, and crystal-clear hands-free calling.'},
    {'name': 'Dell Inspiron 15 Laptop', 'category': 'Electronics', 'price': 55000, 'discount_price': 49999, 'stock': 10,
     'description': 'Dell Inspiron 15 with Intel Core i5, 8GB RAM, 512GB SSD, Windows 11. Perfect for work and entertainment.'},
    {'name': 'boAt Airdopes 141', 'category': 'Electronics', 'price': 1999, 'discount_price': 999, 'stock': 200, 'featured': True,
     'description': 'True wireless earbuds with 42H total playback, Beast Mode low latency, IPX4 water resistance, and ASAP Charge.'},
    {'name': 'Realme Narzo N55', 'category': 'Electronics', 'price': 11999, 'discount_price': 10499, 'stock': 50,
     'description': 'Realme Narzo N55 with 6.72" display, 64MP AI camera, 5000mAh battery, and 33W SUPERVOOC charging.'},

    # Books
    {'name': 'Atomic Habits by James Clear', 'category': 'Books', 'price': 499, 'discount_price': 299, 'stock': 100, 'featured': True,
     'description': 'An easy and proven way to build good habits and break bad ones. The #1 New York Times bestseller.'},
    {'name': 'The Alchemist by Paulo Coelho', 'category': 'Books', 'price': 350, 'discount_price': 199, 'stock': 150,
     'description': 'A magical story about following your dreams. One of the best-selling books in history.'},
    {'name': 'Rich Dad Poor Dad', 'category': 'Books', 'price': 399, 'discount_price': 249, 'stock': 80,
     'description': "Robert Kiyosaki's lesson about money, investing, and building wealth. A classic in personal finance."},
    {'name': 'Python Crash Course', 'category': 'Books', 'price': 699, 'discount_price': 549, 'stock': 60,
     'description': 'A hands-on, project-based introduction to programming with Python 3. Perfect for beginners.'},

    # Fashion
    {'name': 'Levi\'s 511 Slim Jeans', 'category': 'Fashion', 'price': 3999, 'discount_price': 2499, 'stock': 75, 'featured': True,
     'description': "Levi's 511 slim fit jeans with flex fabric for comfortable all-day wear. Classic 5-pocket styling."},
    {'name': 'Nike Air Max 270', 'category': 'Fashion', 'price': 12995, 'discount_price': 9999, 'stock': 30,
     'description': "Nike Air Max 270 running shoes with the largest Air unit in heel history for incredible cushioning and style."},
    {'name': 'Fastrack Analog Watch', 'category': 'Fashion', 'price': 2499, 'discount_price': 1799, 'stock': 45,
     'description': 'Fastrack casual analog watch with mineral glass, stainless steel case, and leather strap. Water resistant.'},

    # Home & Kitchen
    {'name': 'Instant Pot Duo 7-in-1', 'category': 'Home & Kitchen', 'price': 8999, 'discount_price': 6999, 'stock': 20, 'featured': True,
     'description': '7-in-1 multi-cooker: pressure cooker, slow cooker, rice cooker, steamer, sauté pan, yogurt maker, and warmer.'},
    {'name': 'Philips Air Fryer HD9252', 'category': 'Home & Kitchen', 'price': 9995, 'discount_price': 7499, 'stock': 25,
     'description': 'Philips Air Fryer with Rapid Air Technology. Cook crispy food with up to 90% less fat. 4.1L capacity.'},
    {'name': 'Milton Thermosteel Flask 1L', 'category': 'Home & Kitchen', 'price': 799, 'discount_price': 599, 'stock': 100,
     'description': 'Milton stainless steel insulated flask keeps beverages hot for 24 hours and cold for 12 hours.'},

    # Sports
    {'name': 'Boldfit Yoga Mat', 'category': 'Sports & Fitness', 'price': 999, 'discount_price': 699, 'stock': 80, 'featured': True,
     'description': '6mm thick anti-slip yoga mat with carrying strap. Made from eco-friendly NBR material. 183 x 61 cm.'},
    {'name': 'Cosco Dribble Basketball', 'category': 'Sports & Fitness', 'price': 1299, 'discount_price': 899, 'stock': 60,
     'description': 'Official size & weight basketball for indoor and outdoor play. Rubber construction for durability.'},

    # Toys
    {'name': 'LEGO Classic Bricks Box', 'category': 'Toys & Games', 'price': 3499, 'discount_price': 2799, 'stock': 35, 'featured': True,
     'description': 'LEGO Classic creative brick set with 790 pieces in 33 different colors. Build anything you imagine.'},
    {'name': 'Funskool Monopoly', 'category': 'Toys & Games', 'price': 999, 'discount_price': 749, 'stock': 55,
     'description': 'Classic Monopoly board game for 2-6 players. Buy, trade, and develop properties to become the wealthiest player.'},
]

for p in products_data:
    cat = categories.get(p['category'])
    if not cat:
        continue
    obj, created = Product.objects.get_or_create(
        slug=slugify(p['name']),
        defaults={
            'category': cat,
            'name': p['name'],
            'price': p['price'],
            'discount_price': p.get('discount_price'),
            'stock': p.get('stock', 10),
            'available': True,
            'featured': p.get('featured', False),
            'description': p['description'],
        }
    )
    print(f"  {'Created' if created else 'Exists'}: {obj.name}")

print("\n✅ Seed data complete!")
print(f"   Categories: {Category.objects.count()}")
print(f"   Products:   {Product.objects.count()}")