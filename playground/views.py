from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer, Collection
from django.db.models import Q, Value, F, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction, connection
# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(price__gt=30)

    return render(request, 'hello.html', {'name': 'Oleh', 'result': queryset})
