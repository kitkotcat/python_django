from django.shortcuts import render
from datetime import datetime

def index(request):
    products = [
        {'name': 'Laptop', 'price': 999.99, 'created_at': datetime.now()},
        {'name': 'Smartphone', 'price': 499.99, 'created_at': datetime.now()},
        {'name': 'Headphones', 'price': 89.99, 'created_at': datetime.now()},
    ]
    context = {
        'products': products,
    }
    return render(request, 'shopapp/index.html', context)
