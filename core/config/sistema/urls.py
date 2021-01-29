from django.urls import path
from .views.category.views import *
from .views.product.views import *
from .views.dashboard.views import *
from .views.client.views import *
from .views.sale.views import *

app_name = 'sistema'

urlpatterns = [
    #Category
    path('category/list', CategoryListView.as_view(), name='list'),
    path('category/add/', CategoryCreateView.as_view(), name='add'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
    #Product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # client
    path('cliente/', ClientView.as_view(), name='cliente'),
    #Sale
    path('sale/add', SaleCreateView.as_view(), name='sale_create'),
    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
