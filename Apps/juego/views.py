from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Pregunta, Respuesta, Curso, Docente

# Create your views here.

def inicio(request):
    listado_preguntas = Pregunta.objects.all()

    datos = {
        'titulo': 'Listado de Preguntas',
        'preguntas': listado_preguntas
    }
    return render(request, 'base.html', datos)

def comenzar_partida(request):
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
    list_texto_id_preguntas = Pregunta.objects.values_list('id', 'texto')
    
    for tupla in list_texto_id_preguntas:
        id = tupla[0]
        texto = tupla[1]
        list_texto_respuestas = Respuesta.objects.filter(pregunta=id).values_list('texto')
        dic_preg_resp[texto] = list_texto_respuestas
    return dic_preg_resp

def respuestas_para_cada_pregunta():
    dic_idPreg_lista_tuplas_idyTextResp = {}
    list_texto_id_preguntas = Pregunta.objects.values_list('id', 'texto')
    for tupla in list_texto_id_preguntas:
        dic_int = {}
        id = tupla[0]
        texto = tupla[1]
        lista_tuplas_texto_e_id_respuestas = Respuesta.objects.filter(pregunta=id).values_list('id', 'texto')
        dic_int[texto] = lista_tuplas_texto_e_id_respuestas
        dic_idPreg_lista_tuplas_idyTextResp[id] = dic_int
    return dic_idPreg_lista_tuplas_idyTextResp

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

def responder_pregunta(request, id):
    pass


def seleccionar_respuesta(request, id_p, id_r):
    pass


# ===============================================================

def home(request):
    cursos_listados = Curso.objects.all()
    # cursos_listados = Curso.objects.all()[:5]
    # cursos_listados = Curso.objects.all()[4:9]
    # cursos_listados = Curso.objects.all().order_by('nombre')
    # cursos_listados = Curso.objects.all().order_by('-nombre')
    # cursos_listados = Curso.objects.all().order_by('nombre', 'creditos')
    # cursos_listados = Curso.objects.filter(nombre='Historia', creditos=5)
    # cursos_listados = Curso.objects.filter(creditos__lte=4)
    # cursos_listados = Curso.objects.filter(nombre__startswith='Q')
    # cursos_listados = Curso.objects.filter(nombre__contains='g')

    # return HttpResponse("<h1>Hola Mundo!</h1>")
    data = {
        'titulo': 'HOME - Gestión de Cursos',
        'cursos': cursos_listados
    }
    # return render(request, "gestionCursos.html", {"cursos": cursos_listados})
    return render(request, "gestionCursos.html", data)


class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
        return Curso.objects.all().order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'LV - Gestión de Cursos'
        # print(context)
        return context


def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')


def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': 'Edición de Curso',
        'curso': curso
    }

    return render(request, "edicionCurso.html", data)


def editar_curso(request):
    id = int(request.POST['id'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')


def contacto(request):
    return render(request, "contacto.html")
