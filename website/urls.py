from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.ProductListView.as_view(), name='products'),
    path('product/category/', views.CategoryListView.as_view(), name='categories'),
    path('<str:slug>/', views.ContentDetailView.as_view(), name='content'),
    path('product/<str:slug>/', views.ProductDetailView.as_view(), name='product'),
    path('product/category/<str:slug>/', views.CategoryDetailView.as_view(), name='category'),
]
