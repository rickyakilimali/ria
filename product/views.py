from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MyProductView(TemplateView):
    template_name = 'product/my-product.html'

class EditProductView(TemplateView):
    template_name = 'product/edit-product.html'