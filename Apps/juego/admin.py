from django.contrib import admin
from .models import Tematica, Respuesta, Pregunta, Docente, Curso

# Register your models here.

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'tematica')

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pregunta', 'texto', 'correcta')

admin.site.register(Tematica)





# ===============================================

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos', 'docente')
    # ordering = ('creditos', 'nombre')
    # search_fields = ('nombre', 'creditos')
    # list_editable = ('nombre','creditos')
    # list_display_links = ('nombre',)
    # list_filter = ('creditos',)
    # list_per_page = 3 # Paginación
    # exclude = ('creditos',)

    """
    fieldsets = (
        (None, {
            'fields': ('nombre',)
        }),
        ('Advanced options', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',)
        })
    )
    """

    def datos(self, obj):
        return obj.nombre.upper()

    datos.short_description = "CURSO (MAYÚS)"
    datos.empty_value_display = "???"
    datos.admin_order_field = 'nombre'


# admin.site.register(Curso)
# admin.site.register(Curso, CursoAdmin)

admin.site.register(Docente)
