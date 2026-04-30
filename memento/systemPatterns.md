# System Patterns

## Architecture
Django MVT (Model-View-Template):
- **Models** → DB schema in each app's `models.py`
- **Views** → Business logic, returns rendered templates or redirects
- **Templates** → Jinja2-like Django templates with Bootstrap 5

## App Structure
```
amazon_project/   ← Django project settings module
accounts/         ← User auth + profile
products/         ← Product catalog & categories
cart/             ← Session-based cart logic
orders/           ← Checkout + order history
templates/        ← All HTML templates (global)
static/           ← CSS, JS, images
```

## Key Design Patterns

### Session-Based Cart
- Cart stored in `request.session` as a dict: `{product_id: {qty, price}}`
- `cart/cart.py` → `Cart` class encapsulates all cart operations
- `cart/context_processors.py` → injects cart into every template context

### User Profile Extension
- Django's built-in `User` model extended via `accounts.UserProfile` (OneToOne)
- Signal `post_save` on User auto-creates/updates UserProfile

### Slug-Based URLs
- Products and categories use slugs for SEO-friendly URLs
- `SlugField` with `unique=True` and `prepopulated_fields` in admin

### Admin Customization
- Each app registers models with custom `ModelAdmin` for list display, filters, search

## URL Routing
```
/                       → home (products:product_list)
/accounts/register/     → accounts:register
/accounts/login/        → accounts:login
/accounts/logout/       → accounts:logout
/accounts/profile/      → accounts:profile
/products/              → products:product_list
/products/<slug>/       → products:product_detail
/category/<slug>/       → products:category_detail
/cart/                  → cart:cart_detail
/cart/add/<id>/         → cart:cart_add
/cart/remove/<id>/      → cart:cart_remove
/orders/checkout/       → orders:checkout
/orders/history/        → orders:order_history
/orders/<id>/           → orders:order_detail