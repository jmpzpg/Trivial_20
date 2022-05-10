from django.urls import path

from Apps.juego.views import comenzar_partida, inicio, preguntas, respuestas_para_pregunta, responder_pregunta, validar_respuesta
#from Apps.juego.views import 

urlpatterns = [
    #path('', inicio),
    path('', comenzar_partida),
    path('preguntas/', preguntas),
    path('pruebaform/', respuestas_para_pregunta),
    path('responder_pregunta/<int:id>', responder_pregunta),
    path('validar_respuesta/<int:id_p>/<int:id_r>', validar_respuesta)
]