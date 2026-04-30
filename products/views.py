from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Product


def home(request):
    featured_products = Product.objects.filter(available=True, featured=True)[:8]
    latest_products = Product.objects.filter(available=True)[:12]
    categories = Category.objects.all()
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories,
        'title': 'Amazon Clone – Home',
    }
    return render(request, 'home.html', context)


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Search
    query = request.GET.get('q', '')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # Category filter via query param
    category_slug = request.GET.get('category', '')
    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    # Price sort
    sort = request.GET.get('sort', '')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created')

    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
        'query': query,
        'sort': sort,
        'title': 'All Products',
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category, available=True
    ).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'title': product.name,
    }
    return render(request, 'products/product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()

    sort = request.GET.get('sort', '')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created')

    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'sort': sort,
        'title': category.name,
    }
    return render(request, 'products/category_detail.html', context)