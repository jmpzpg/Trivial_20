from django.urls import path

from Apps.juego.views import comenzar_partida, inicio, preguntas, respuestas_para_pregunta, responder_pregunta, seleccionar_respuesta, home, CursoListView, registrar_curso, eliminar_curso, edicion_curso, editar_curso, contacto
#from Apps.juego.views import 

urlpatterns = [
    #path('', inicio),
    path('', comenzar_partida),
    path('preguntas/', preguntas),
    path('pruebaform/', respuestas_para_pregunta),
    path('responder_pregunta/<int:id>', responder_pregunta),
    path('seleccionar_respuesta/<int:id_p>/<int:id_r>', seleccionar_respuesta),
    #path('', home),
    #path('', CursoListView.as_view(), name='gestion_cursos'),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('editarCurso/', editar_curso),
    path('contacto/', contacto),
]