from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')

    # Pre-fill form from user profile
    user = request.user
    profile = getattr(user, 'profile', None)
    initial_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': profile.phone if profile else '',
        'address': profile.address if profile else '',
        'city': profile.city if profile else '',
        'state': profile.state if profile else '',
        'pincode': profile.pincode if profile else '',
    }

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order.save()

            # Create order items from cart
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    product_name=item['product'].name,
                    price=item['price'],
                    quantity=item['quantity'],
                )

            # Clear the cart
            cart.clear()
            messages.success(
                request,
                f'Order #{order.id} placed successfully! Thank you for shopping with us.'
            )
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = CheckoutForm(initial=initial_data)

    context = {
        'cart': cart,
        'form': form,
        'title': 'Checkout',
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    context = {
        'orders': orders,
        'title': 'My Orders',
    }
    return render(request, 'orders/order_history.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
        'title': f'Order #{order.id}',
    }
    return render(request, 'orders/order_detail.html', context)