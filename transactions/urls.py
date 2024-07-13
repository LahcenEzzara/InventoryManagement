from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers-list'),
    path('suppliers/new/', views.SupplierCreateView.as_view(), name='new-supplier'),
    path('suppliers/<int:pk>/edit/',
         views.SupplierUpdateView.as_view(), name='edit-supplier'),
    path('suppliers/<int:pk>/delete/',
         views.SupplierDeleteView.as_view(), name='delete-supplier'),
    path('suppliers/<str:name>/', views.SupplierView.as_view(), name='supplier'),

    path('purchases/', views.PurchaseView.as_view(), name='purchases-list'),
    path('purchases/new/', views.SelectSupplierView.as_view(),
         name='select-supplier'),
    path('purchases/new/<int:pk>/',
         views.PurchaseCreateView.as_view(), name='new-purchase'),
    path('purchases/<int:pk>/delete/',
         views.PurchaseDeleteView.as_view(), name='delete-purchase'),

    path('sales/', views.SaleView.as_view(), name='sales-list'),
    path('sales/new/', views.SaleCreateView.as_view(), name='new-sale'),
    path('sales/<int:pk>/delete/',
         views.SaleDeleteView.as_view(), name='delete-sale'),

    path('purchases/<str:billno>/',
         views.PurchaseBillView.as_view(), name='purchase-bill'),
    path('sales/<str:billno>/', views.SaleBillView.as_view(), name='sale-bill'),
]
