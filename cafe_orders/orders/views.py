from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Order
from .forms import OrderForm

def index(request):
    orders = Order.objects.all()
    return render(request, 'orders/index.html', {'orders': orders})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.calculate_total()
            return redirect('orders-index')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            order.calculate_total()
            return redirect('orders-index')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/edit_order.html', {'form': form, 'order': order})

def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('orders-index')

def change_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.status == 'pending':
        order.status = 'ready'
    elif order.status == 'ready':
        order.status = 'paid'
    order.save()
    return redirect('orders-index')
