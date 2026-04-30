from .models import Category


def categories(request):
    """Inject all categories into every template context."""
    return {'all_categories': Category.objects.all()}