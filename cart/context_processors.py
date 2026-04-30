from .cart import Cart


def cart(request):
    """Inject the cart instance into every template context."""
    return {'cart': Cart(request)}