from django.shortcuts import render, redirect, get_object_or_404
from .models import Module, Participant, Task
from .forms import ModuleForm, TaskForm, ParticipantForm


def home(request):
    return render(request, 'main/home.html')


def modules(request):
    all_modules = Module.objects.using('modules_db').all()
    return render(request, 'main/modules.html', {'modules': all_modules})


def module_details(request, pk):
    module = get_object_or_404(Module.objects.using('modules_db'), pk=pk)
    tasks = Task.objects.using('modules_db').filter(module=module)
    return render(request, 'main/module_details.html', {'module': module, 'tasks': tasks})


def participants(request):
    participants_list = Participant.objects.all()
    return render(request, 'main/participants.html', {'participants': participants_list})


def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/register.html',
                          {'form': None, 'success_message': "Вы успешно зарегистрировались!"})
    else:
        form = ParticipantForm()
    return render(request, 'main/register.html', {'form': form})


def manage_modules(request):
    modules = Module.objects.all()
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modules')
    else:
        form = ModuleForm()
    return render(request, 'main/manage_modules.html', {'modules': modules, 'form': form})


def edit_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('modules')
    else:
        form = ModuleForm(instance=module)
    return render(request, 'main/edit_module.html', {'form': form})


def delete_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.delete()
    return redirect('modules')


def manage_tasks(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modules')
    else:
        form = TaskForm()
    return render(request, 'main/manage_tasks.html', {'tasks': tasks, 'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('modules')
    else:
        form = TaskForm(instance=task)
    return render(request, 'main/edit_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('modules')

