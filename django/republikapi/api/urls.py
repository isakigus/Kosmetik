from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'producto', views.ProductoViewSet)
router.register(r'ingrediente', views.IngredienteViewSet)
router.register(r'imagen', views.ImagenViewSet)
router.register(r'ingrediente_receta', views.IngredienteRecetaViewSet)
router.register(r'receta', views.RecetaViewSet)
router.register(r'precio', views.PrecioViewSet)
router.register(r'atributo', views.AtributoCosmeticoViewSet)


urlpatterns = [
    url(r'search/', views.SearchList.as_view()),
    url(r'^', include(router.urls)),
]
