"""
Downloads product-relevant images using LoremFlickr (keyword-based real photos)
and assigns them to Product and Category records in the database.

Usage: python download_images.py
"""
import os
import django
import urllib.request
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon_project.settings')
django.setup()

from products.models import Category, Product

BASE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = BASE_DIR / 'media'
PRODUCTS_DIR = MEDIA_DIR / 'products'
CATEGORIES_DIR = MEDIA_DIR / 'categories'

PRODUCTS_DIR.mkdir(parents=True, exist_ok=True)
CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)


def download(url, dest_path, force=True):
    """Download a file from url to dest_path."""
    if dest_path.exists() and not force:
        print(f"  [skip] {dest_path.name} already exists")
        return True
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as response:
            data = response.read()
        if len(data) < 1000:
            print(f"  [warn] {dest_path.name} response too small ({len(data)} bytes), skipping")
            return False
        with open(dest_path, 'wb') as f:
            f.write(data)
        print(f"  [ok]   Downloaded {dest_path.name} ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"  [err]  Failed {dest_path.name}: {e}")
        return False


# loremflickr.com provides real, keyword-relevant photos
# Format: https://loremflickr.com/{width}/{height}/{keyword1,keyword2}

# ---- Category images (keyword-specific) ----
category_images = {
    'electronics':      'https://loremflickr.com/600/400/electronics,gadget',
    'books':            'https://loremflickr.com/600/400/books,library',
    'fashion':          'https://loremflickr.com/600/400/fashion,clothing',
    'home-kitchen':     'https://loremflickr.com/600/400/kitchen,cooking',
    'sports-fitness':   'https://loremflickr.com/600/400/sports,fitness',
    'toys-games':       'https://loremflickr.com/600/400/toys,games',
}

# ---- Product images (product-specific keywords) ----
product_image_map = {
    # Electronics
    'samsung-galaxy-s24':           'https://loremflickr.com/400/400/samsung,smartphone',
    'apple-iphone-15':              'https://loremflickr.com/400/400/iphone,apple,smartphone',
    'sony-wh-1000xm5-headphones':   'https://loremflickr.com/400/400/headphones,sony',
    'dell-inspiron-15-laptop':      'https://loremflickr.com/400/400/laptop,computer',
    'boat-airdopes-141':            'https://loremflickr.com/400/400/earbuds,wireless',
    'realme-narzo-n55':             'https://loremflickr.com/400/400/smartphone,mobile',
    # Books
    'atomic-habits-by-james-clear': 'https://loremflickr.com/400/400/book,reading,habit',
    'the-alchemist-by-paulo-coelho':'https://loremflickr.com/400/400/book,novel',
    'rich-dad-poor-dad':            'https://loremflickr.com/400/400/book,finance,money',
    'python-crash-course':          'https://loremflickr.com/400/400/programming,python,coding',
    # Fashion
    'levis-511-slim-jeans':         'https://loremflickr.com/400/400/jeans,denim',
    'nike-air-max-270':             'https://loremflickr.com/400/400/sneakers,shoes,nike',
    'fastrack-analog-watch':        'https://loremflickr.com/400/400/watch,wristwatch',
    # Home & Kitchen
    'instant-pot-duo-7-in-1':       'https://loremflickr.com/400/400/cooking,kitchen,pot',
    'philips-air-fryer-hd9252':     'https://loremflickr.com/400/400/airfryer,kitchen,appliance',
    'milton-thermosteel-flask-1l':  'https://loremflickr.com/400/400/flask,bottle,thermos',
    # Sports & Fitness
    'boldfit-yoga-mat':             'https://loremflickr.com/400/400/yoga,mat,fitness',
    'cosco-dribble-basketball':     'https://loremflickr.com/400/400/basketball,sports',
    # Toys & Games
    'lego-classic-bricks-box':      'https://loremflickr.com/400/400/lego,toy,bricks',
    'funskool-monopoly':            'https://loremflickr.com/400/400/boardgame,monopoly',
}

print("=" * 60)
print("Downloading category images...")
print("=" * 60)
for cat in Category.objects.all():
    key = cat.slug
    url = category_images.get(key, f'https://loremflickr.com/600/400/{cat.slug}')
    fname = f'{cat.slug}.jpg'
    dest = CATEGORIES_DIR / fname
    if download(url, dest):
        cat.image = f'categories/{fname}'
        cat.save()

print()
print("=" * 60)
print("Downloading product images...")
print("=" * 60)
for product in Product.objects.all():
    url = product_image_map.get(
        product.slug,
        f'https://loremflickr.com/400/400/{product.name.split()[0].lower()}'
    )
    fname = f'{product.slug}.jpg'
    dest = PRODUCTS_DIR / fname
    if download(url, dest):
        product.image = f'products/{fname}'
        product.save()

print()
print("=" * 60)
print("✅ Image download complete!")
print(f"   Categories with images: {Category.objects.exclude(image='').count()}")
print(f"   Products with images:   {Product.objects.exclude(image='').count()}")
print("=" * 60)