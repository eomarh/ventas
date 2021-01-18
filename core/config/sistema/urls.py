from django.urls import path
from .views.category.views import *

app_name = 'sistema'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='list'),
    path('category/add', CategoryCreateView.as_view(), name='add'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete')
]
