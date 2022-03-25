from django.urls import path
from .views import UsuarioCreate
from .import views
from .views import List
app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("registrar/", UsuarioCreate.as_view(), name="registrar" ),
    path("listar/", List.as_view(), name="listar" ),
]