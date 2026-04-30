# Active Context

## Current Focus
Initial project scaffold — building the complete Amazon Clone from scratch.

## What's Being Built Now
- Django project skeleton (`amazon_project/`)
- Four Django apps: `accounts`, `products`, `cart`, `orders`
- All models, views, URLs, forms, admin registrations
- Full Bootstrap 5 template set
- Static CSS/JS
- requirements.txt, manage.py

## Recent Changes
- Created memento documentation (projectbrief, productContext, systemPatterns, techContext)

## Next Steps
1. Create `requirements.txt`
2. Create `manage.py`
3. Create `amazon_project/` settings module
4. Create all four Django apps with models, views, URLs
5. Create all templates
6. Create static files (CSS, JS)
7. Wire up admin

## Active Decisions
- Project settings module: `amazon_project` (not `amazon` to avoid dir collision)
- Cart is session-based (no DB table for cart items)
- UserProfile created via signal on User save
- Slugs used for all product/category URLs
- Bootstrap 5 CDN for rapid development
- `crispy_forms` with bootstrap5 pack for form rendering