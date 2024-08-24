
from django.http import HttpResponse, JsonResponse
from django.template.defaultfilters import title

from .models import Project, Task
from django.shortcuts import get_object_or_404,render, redirect

# Create your views here lo que vera el user final.

def hello(request,username):
    return

def index(request):
    title = 'Welcome to DjangoProyect'
    return render(request,'index.html',{'title':title})

def projectHtml(request):
    projects = Project.objects.all()
    return render(request,'project.html',{'projects':projects})

def taskHtml(request):
    tasks = Task.objects.all()
    return render(request,'task.html',{'tasks':tasks})

def createTASK(request):
    projects = Project.objects.all()
    return render(request,'createTask.html',{'projects':projects})

def createProject(request):
    return render(request,'createProject.html')

def processForm(request):
    if request.method == 'POST':
        title = request.POST['i1']
        description = request.POST['txt1']
        pr= request.POST['projects']
        project = Project.objects.get(id=1)
        print(pr)
        task =Task(title=title, description=description,project=project)
        task.save()
        return redirect('/tasks/')  # 'success_page' es el nombre de la vista a la que quieres redirigir.
    else:
        return HttpResponse("Método no permitido", status=405)

def processFormProject(request):
    if request.method == 'POST':
        name = request.POST['i1']
        project = Project(name=name)
        project.save()
        return redirect('/project/')
    else:
        return HttpResponse("Método no permitido", status=405)

def projects(request):
    p = list(Project.objects.values())
    return JsonResponse(p, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id) #por si  no encuentra el recurso devolvemos 4004
    return HttpResponse("<h1>Tareas: %s </h1>"%task.title)

