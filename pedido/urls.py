from django.urls import path
from . import views


app_name = "pedido"


urlpatterns = [
    path('pagar/', views.Pagar.as_view(), name="pagar"),
    path('fecharpedido/', views.FecharPedido.as_view(), name="fecharpedido"),
    path('detalhepedido/', views.DetalhePedido.as_view(), name="detalhepedido"),

]