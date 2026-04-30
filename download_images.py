"""
Downloads sample product & category images from picsum.photos
and assigns them to Product and Category records.

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


def download(url, dest_path):
    """Download a file from url to dest_path if it doesn't already exist."""
    if dest_path.exists():
        print(f"  [skip] {dest_path.name} already exists")
        return True
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read()
        with open(dest_path, 'wb') as f:
            f.write(data)
        print(f"  [ok]   Downloaded {dest_path.name}")
        return True
    except Exception as e:
        print(f"  [err]  Failed {dest_path.name}: {e}")
        return False


# ---- Category images ----
# Using picsum.photos/seed/<word>/400/300
category_images = {
    'electronics':      'https://picsum.photos/seed/electronics/400/300',
    'books':            'https://picsum.photos/seed/books/400/300',
    'fashion':          'https://picsum.photos/seed/fashion/400/300',
    'home-kitchen':     'https://picsum.photos/seed/kitchen/400/300',
    'sports-fitness':   'https://picsum.photos/seed/sports/400/300',
    'toys-games':       'https://picsum.photos/seed/toys/400/300',
}

print("Downloading category images...")
for cat in Category.objects.all():
    key = cat.slug
    url = category_images.get(key)
    if not url:
        # fallback: use slug as seed
        url = f'https://picsum.photos/seed/{cat.slug}/400/300'
    fname = f'{cat.slug}.jpg'
    dest = CATEGORIES_DIR / fname
    if download(url, dest):
        cat.image = f'categories/{fname}'
        cat.save()

# ---- Product images ----
# Mapping product slug → picsum photo ID (hand-picked for relevance)
product_image_map = {
    # Electronics
    'samsung-galaxy-s24':           'https://picsum.photos/seed/samsung/400/400',
    'apple-iphone-15':              'https://picsum.photos/seed/iphone/400/400',
    'sony-wh-1000xm5-headphones':   'https://picsum.photos/seed/headphones/400/400',
    'dell-inspiron-15-laptop':      'https://picsum.photos/seed/laptop/400/400',
    'boat-airdopes-141':            'https://picsum.photos/seed/earbuds/400/400',
    'realme-narzo-n55':             'https://picsum.photos/seed/smartphone/400/400',
    # Books
    'atomic-habits-by-james-clear': 'https://picsum.photos/seed/atomichabits/400/400',
    'the-alchemist-by-paulo-coelho':'https://picsum.photos/seed/alchemist/400/400',
    'rich-dad-poor-dad':            'https://picsum.photos/seed/richdad/400/400',
    'python-crash-course':          'https://picsum.photos/seed/pythonbook/400/400',
    # Fashion
    'levis-511-slim-jeans':         'https://picsum.photos/seed/jeans/400/400',
    'nike-air-max-270':             'https://picsum.photos/seed/sneakers/400/400',
    'fastrack-analog-watch':        'https://picsum.photos/seed/watch/400/400',
    # Home & Kitchen
    'instant-pot-duo-7-in-1':       'https://picsum.photos/seed/instantpot/400/400',
    'philips-air-fryer-hd9252':     'https://picsum.photos/seed/airfryer/400/400',
    'milton-thermosteel-flask-1l':  'https://picsum.photos/seed/flask/400/400',
    # Sports
    'boldfit-yoga-mat':             'https://picsum.photos/seed/yogamat/400/400',
    'cosco-dribble-basketball':     'https://picsum.photos/seed/basketball/400/400',
    # Toys
    'lego-classic-bricks-box':      'https://picsum.photos/seed/lego/400/400',
    'funskool-monopoly':            'https://picsum.photos/seed/monopoly/400/400',
}

print("\nDownloading product images...")
for product in Product.objects.all():
    url = product_image_map.get(product.slug)
    if not url:
        url = f'https://picsum.photos/seed/{product.slug}/400/400'
    fname = f'{product.slug}.jpg'
    dest = PRODUCTS_DIR / fname
    if download(url, dest):
        product.image = f'products/{fname}'
        product.save()

print("\n✅ Image download complete!")
print(f"   Categories with images: {Category.objects.exclude(image='').count()}")
print(f"   Products with images:   {Product.objects.exclude(image='').count()}")