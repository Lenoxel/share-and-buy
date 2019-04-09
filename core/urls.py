from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('planos/', views.planos, name='planos'),
    path('suporte/', views.suporte, name='suporte'),
    path('afiliado/', views.afiliado, name='afiliado'),
    path('produtor/', views.produtor, name='produtor'),
    path('loginAfiliado/', views.loginAfiliado, name='loginAfiliado'),
    path('loginProdutor/', views.loginProdutor, name='loginProdutor'),
]
