from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm
from .models import Project


def projects(request):
    projects_list = Project.objects.all()
    context = {'projects': projects_list}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)

    return render(request, 'projects/single-project.html', {'project': project_obj})


@login_required(login_url='login')
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project-form.html", context)


@login_required(login_url='login')
def update_project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_obj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_obj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project-form.html", context)


@login_required(login_url='login')
def delete_project(reqeust, pk):
    project_obj = Project.objects.get(id=pk)

    if reqeust.method == 'POST':
        project_obj.delete()
        return redirect('projects')

    context = {'object': project_obj}
    return render(reqeust, 'projects/delete-template.html', context)
