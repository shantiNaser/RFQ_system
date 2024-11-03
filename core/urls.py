from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Client URLs
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.item_add, name='item_add'),
    path('rfq/create/', views.rfq_create, name='rfq_create'),
    path('rfq/<int:pk>/', views.rfq_detail, name='rfq_detail'),
    path('rfq/<int:pk>/approve/', views.rfq_approve, name='rfq_approve'),
    path('rfqs/client/', views.rfq_list_client, name='rfq_list_client'),
    # Vendor URLs
    path('rfqs/', views.rfq_list, name='rfq_list'),
    path('quotation/add/<int:rfq_id>/', views.quotation_add, name='quotation_add'),
    path('rfq/<int:pk>/load_quotations/', views.load_quotations, name='load_quotations'),
    path('rfqs/approved/', views.rfq_approved_list, name='rfq_approved_list'),
    # registration url
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
