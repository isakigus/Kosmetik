from django.contrib import admin

from api.models import AtributoCosmetico
from api.models import Producto
from api.models import Ingrediente
from api.models import Imagen
from api.models import IngredienteReceta
from api.models import Receta
from api.models import Precio
from api.models import Tienda
from api.models import CategoriaIngrediente
from api.models import CategoriaCosmetica


class AtributoCosmeticoAdmin(admin.ModelAdmin):
    pass


class ProductoAdmin(admin.ModelAdmin):
    pass


class IngredienteAdmin(admin.ModelAdmin):
    pass


class ImagenAdmin(admin.ModelAdmin):
    pass


class IngredienteRecetaAdmin(admin.ModelAdmin):
    pass


class RecetaAdmin(admin.ModelAdmin):
    pass


class PrecioAdmin(admin.ModelAdmin):
    pass


class TiendaAdmin(admin.ModelAdmin):
    pass


class CategoriaIngredienteAdmin(admin.ModelAdmin):
    pass


class CategoriaCosmeticaAdmin(admin.ModelAdmin):
    pass


admin.site.register(AtributoCosmetico, AtributoCosmeticoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Receta, RecetaAdmin)
admin.site.register(IngredienteReceta, IngredienteRecetaAdmin)
admin.site.register(Precio, PrecioAdmin)
admin.site.register(Tienda, TiendaAdmin)
admin.site.register(CategoriaIngrediente, CategoriaIngredienteAdmin)
admin.site.register(CategoriaCosmetica, CategoriaCosmeticaAdmin)
