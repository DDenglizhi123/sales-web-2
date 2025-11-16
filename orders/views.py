from django.shortcuts import render
from .models import Order, OrderItem
from django.db.models import Q

# Create your views here.
def order_list(request):
    # Searching function
    query = request.GET.get('search', '').strip()
    if query:
        orders = Order.objects.filter(
            Q(customer__name__icontains=query)
            | Q(order_number__icontains=query)
            | Q(ordered__product__item_name__icontains=query)
        ).distinct()
    else:
        orders = Order.objects.all()

    return render(request, 'orders/order_list.html', {'orders': orders, 'query': query})

def order_details(request, pk):
    order_details = OrderItem.objects.filter(order=pk)
    order= Order.objects.get(id=pk)
    customer_name = order.customer.name
    order_number = order.order_number
    contexts = {
        'order_details': order_details,
        'customer_name': customer_name,
        'order_number': order_number,
        }
    return render(request, 'orders/order_details.html', contexts)