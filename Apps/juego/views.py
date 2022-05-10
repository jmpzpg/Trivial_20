from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Pregunta, Respuesta 

import random
import pdb




# Create your views here.

def inicio(request):
    listado_preguntas = Pregunta.objects.all()

    datos = {
        'titulo': 'Listado de Preguntas',
        'preguntas': listado_preguntas
    }
    return render(request, 'base.html', datos)

def comenzar_partida(request):
    
    #dic_respuestas_para_pregunta = respuestas_para_cada_pregunta()
    #dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp = respuestas_para_cada_pregunta()
    dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp_selecc_aleatoria = respuestas_para_cada_pregunta()
    listado_preguntas = Pregunta.objects.all()
    listado_respuestas = Respuesta.objects.all()
    list_id_texto_preguntas = Pregunta.objects.values_list('id', 'texto')
    list_id_preguntas = Pregunta.objects.values_list('id', flat=True)
    
    datos = {
        'titulo': 'Listado de respuestas',
        'preguntas': listado_preguntas,
        'preguntas_texto_e_id': list_id_texto_preguntas,
        'preguntas_selecc_aleat_con_sus_respuestas':dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp_selecc_aleatoria,
        'respuestas_a_pregunta': partida_pregunta(request, 2),
        'id_preguntas': list_id_preguntas,
        'dic_p_r': preguntas_respuestas()

    }
    return render(request, 'partida20.html', datos)

def comenzar_partida_2(request):
    dic_respuestas_para_pregunta = respuestas_para_cada_pregunta()
    listado_preguntas = Pregunta.objects.all()
    listado_respuestas = Respuesta.objects.all()
    list_id_texto_preguntas = Pregunta.objects.values_list('id', 'texto')
    list_id_preguntas = Pregunta.objects.values_list('id', flat=True)
    datos = {
        'titulo': 'Listado de respuestas',
        'preguntas': listado_preguntas,
        'preguntas_texto_e_id': list_id_texto_preguntas,
        'respuestas_para_pregunta':dic_respuestas_para_pregunta,
        'respuestas_a_pregunta': partida_pregunta(request, 2),
        'id_preguntas': list_id_preguntas,
        'dic_p_r': preguntas_respuestas()
        
    }
    return render(request, 'partida10.html', datos)

def partida_pregunta(request, id_pregunta):
    listado_respuestas = Respuesta.objects.filter(pregunta=id_pregunta)
    #listado_respuestas = {'uno':'el uno', 'Dos':'el dos', 'Tres':'el tres', 'Cuatro':'el cuarto'}
    return listado_respuestas
    #return render(request, 'partida_respuestas.html', {'respuestas_a_pregunta':listado_respuestas})

def preguntas_respuestas():
    dic_preg_resp = {}
    list_tuplas_id_texto_de_preguntas = Pregunta.objects.values_list('id', 'texto')
    
    for tupla in list_tuplas_id_texto_de_preguntas:
        id = tupla[0]
        texto = tupla[1]
        list_texto_respuestas = Respuesta.objects.filter(pregunta=id).values_list('texto')
        dic_preg_resp[texto] = list_texto_respuestas
    return dic_preg_resp

def respuestas_para_cada_pregunta():
    dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp = {}
    dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp_selecc_aleatoria ={}
    #list_tuplas_id_texto_de_preguntas = Pregunta.objects.values_list('id', 'texto')
    list_tuplas_id_texto_de_preguntas = tomar_preguntas_aleatorias()
    list_tuplas_IdyTexto_de_preguntas_selecc_aleatoria = tomar_preguntas_aleatorias()
    for tupla in list_tuplas_IdyTexto_de_preguntas_selecc_aleatoria:
        dic_int = {}
        id = tupla[0]
        texto = tupla[1]
        list_tuplas_id_texto_de_respuestas = Respuesta.objects.filter(pregunta=id).values_list('id', 'texto')
        dic_int[texto] = list_tuplas_id_texto_de_respuestas
        dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp_selecc_aleatoria[id] = dic_int
    return dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp_selecc_aleatoria

def respuestas_para_cada_pregunta_2():
    dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp = {}

    

    list_tuplas_id_texto_de_preguntas = Pregunta.objects.values_list('id', 'texto')
    for tupla in list_tuplas_id_texto_de_preguntas:
        dic_int = {}
        id = tupla[0]
        texto = tupla[1]
        list_tuplas_id_texto_de_respuestas = Respuesta.objects.filter(pregunta=id).values_list('id', 'texto')
        dic_int[texto] = list_tuplas_id_texto_de_respuestas
        dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp[id] = dic_int
    return dic_idPreg_y_dic_TxtPreg_y_lista_tuplas_idyTextResp

def preguntas(request):
    listado_preguntas = Pregunta.objects.all()

    datos = {
        'titulo': 'Listado de Preguntas',
        'preguntas': listado_preguntas
    }

    return render(request, 'preguntas.html', datos)

def respuestas_para_pregunta(request):
    #nombre_respuesta = Respuesta.objects.all().select_related('self.respuesta')
    listado_preguntas = Pregunta.objects.all()
    listado_respuestas = Respuesta.objects.all()
    datos = {
        'titulo': 'Listado de respuestas',
        'preguntas': listado_preguntas,
        'respuestas_para_pregunta': listado_respuestas
    }
    return render(request, 'pruebaform.html', datos)

def mostrar_pregunta(request):
    #nombre_respuesta = Respuesta.objects.all().select_related('self.respuesta')
    listado_preguntas = Pregunta.objects.all()
    listado_respuestas = Respuesta.objects.all()
    datos = {
        'titulo': 'Listado de respuestas',
        'preguntas': listado_preguntas,
        'respuestas_para_pregunta': listado_respuestas
    }
    return render(request, 'partida_pregunta.html', datos)


def sacar_lista_preg_aleatorias_de_tablaPreguntas():
    lista_tuplas_preguntas =Pregunta.objects.all().values_list('id')
    #lista_tuplas_preg_barajadas = random.sample(lista_tuplas_preguntas, k=4)
    listado_todas_las_preg = []
    for tupla in lista_tuplas_preguntas:
        listado_todas_las_preg.append(tupla[0])
    
    listado_todas_las_preg_barajadas = random.sample(listado_todas_las_preg, k=4)


    
    #preguntas_ids = Pregunta.objects.all().values('id')
    #random_id = random.choices(preguntas_ids, k=2)
    #preg_aleatorias = Pregunta.objects.filter(id in listado_todas_las_preg)
    return listado_todas_las_preg_barajadas

def tomar_preguntas_aleatorias():
    #pdb.set_trace()
    # primero tomamos una lista de dicc con todos los ID de la tabla Preguntas
    l_dic_preguntas_ids = Pregunta.objects.all().values('id') #es una lista de dicc id:valor
    # segundo creamos variable para guardar la lista de  esos ID
    lista_id_preg = []
    for dic in l_dic_preguntas_ids:
        lista_id_preg.append(dic['id'])
    a = list(lista_id_preg)
    # Ya tenemos la lista de ID de Preguntas. Ahora la barajamos y seleccionamos numero
    b = random.sample(lista_id_preg, 10)
    # Ya tenemos la misma lista con las preguntas seleccionadas y barajadas.
    # Ahora hay que reconstruir el dicc para tener los ID y sus textos
    list_tuplas_IdyTexto_de_preguntas_selecc_aleatoria = Pregunta.objects.filter(id__in = b).values_list('id', 'texto')

    return list_tuplas_IdyTexto_de_preguntas_selecc_aleatoria
    #resp_de_preg_aleat = Respuesta.objects.filter(pregunta=id in random_id).values_list('id', 'texto')
               


def responder_pregunta(request, id):
    pass


def validar_respuesta(request, id_p, id_r):
    num_resp_acertadas = request.session.get('num_resp_acertadas' , 0)
    
    a = Respuesta.objects.get(pregunta=id_p , correcta=1)
    b = Respuesta.objects.filter(pregunta=id_p , correcta=1).values('id')

    id_resp_correcta = b[0]['id']
    if id_r == id_resp_correcta:
        

        request.session['num_resp_acertadas'] = num_resp_acertadas + 1

    context = {
        'num_resp_acertadas': num_resp_acertadas,
    }
    return render(request, 'ver_respuesta.html', context=context)
    #dic_salida = { 'nra': contador}
    #return render(request, 'partida20.html', dic_salida)



# ===============================================================




# ≠≠≠≠≠≠≠  ≠≠≠≠≠≠≠≠≠≠≠≠  ≠≠≠≠≠≠≠≠≠≠≠≠  ≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠

