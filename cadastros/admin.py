from django.contrib import admin
from .models import Cliente, Sistema, Contrato

admin.site.register(Cliente)



@admin.register(Contrato)
class SiteContrato(admin.ModelAdmin):
    list_display = ["cliente", "sistema", "valor", "inicio", "termino"]


@admin.register(Sistema)
class SiteSistema(admin.ModelAdmin):
    list_display = ["nome"]

# Register your models here.
