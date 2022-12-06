from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientView.as_view(), name='client_view'),
    path('<int:pk>/detail/', views.ClientDetailView.as_view(), name='detail_view'),
]