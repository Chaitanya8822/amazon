from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'price', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'status', 'paid', 'created']
    list_filter = ['status', 'paid', 'created']
    list_editable = ['status', 'paid']
    search_fields = ['user__username', 'first_name', 'last_name', 'email']
    date_hierarchy = 'created'
    ordering = ['-created']
    inlines = [OrderItemInline]
    readonly_fields = ['created', 'updated']