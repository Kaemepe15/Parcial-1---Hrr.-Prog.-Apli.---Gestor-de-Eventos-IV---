from django.urls import path
from .views import OrganizadorListView, OrganizadorCreativeView

urlpatterns= [
    path('organizadores/', OrganizadorListView.as_view(), name='organizador_list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador_create'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout')

]