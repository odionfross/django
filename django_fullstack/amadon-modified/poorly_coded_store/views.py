from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    context = {
        # Note we can accomplish without using session
        # Order.objects.last().total_price
        "total_current_amount": request.session['total_charge'],
        "total_combined_quantity": Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum'],
        "total_combined_amount": Order.objects.all().aggregate(Sum('total_price'))['total_price__sum']
    }
    return render(request, "store/checkout.html", context)

def process_order(request):
    print("Entering process_order GET")
    if request.method == 'POST':
        print("Entering process_order POST")
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = int(Product.objects.get(id=request.POST['id']).price)
        request.session['total_charge'] = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=request.session['total_charge'])
        # Note we can accomplish without using session
        # total_charge = quantity_from_form * price_from_form
        # print("Charging credit card...")
        # Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect('/checkout')
    return redirect('/')