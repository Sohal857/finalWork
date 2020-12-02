from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView

from .models import Content
from .models import Product
from .models import Category

def index(request):
    content = Product.objects.filter(is_featured=True)
    template = loader.get_template('website/index.html')
    context = {
        'content': content
    }
    return HttpResponse(
        template.render(context, request)
    )



class ContentDetailView(View):
    def get(self, request, *args, **kwargs):
        content = get_object_or_404(Content, slug=kwargs['slug'])
        context = {'content': content}
        return render(request, 'website/content.html', context)

class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs['slug'])
        context = {'product': product}
        return render(request, 'website/product-detail.html', context)

class ProductListView(ListView):
    queryset = Product.objects.filter()
    template_name = 'website/product.html'
    context_object_name = 'products'

class CategoryDetailView(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['slug'])
        context = {'category': category}
        return render(request, 'website/category-detail.html', context)

class CategoryListView(ListView):
    queryset = Category.objects.filter()
    template_name = 'website/category.html'
    context_object_name = 'categories'
