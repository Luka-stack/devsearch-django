from calendar import c
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from projects.utils import paginate_project, search_projects
from .forms import ProjectForm, ReviewForm
from .models import Project, Tag


def projects(request):
    project_list, query = search_projects(request)
    custom_range, project_list = paginate_project(request, project_list, 3)

    context = {'projects': project_list,
               'search_query': query, 'custom_range': custom_range}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project_obj
        review.owner = request.user.profile
        review.save()

        project_obj.get_vote_count

        messages.success(request, 'Your review was successfully submitted!')

        return redirect('project', pk=pk)

    context = {'project': project_obj, 'form': form}

    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newTags = request.POST.get('newTags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newTags:
                tag, created = Tag.objects.get_or_create()
                project.tags.add(tag)

            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project-form.html", context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project_obj = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project_obj)

    if request.method == 'POST':
        newTags = request.POST.get('newTags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project_obj)

        if form.is_valid():
            project = form.save()

            for tag in newTags:
                tag, created = Tag.objects.get_or_create()
                project.tags.add(tag)

            return redirect('projects')

    context = {'form': form, 'project': project_obj}
    return render(request, "projects/project-form.html", context)


@login_required(login_url='login')
def delete_project(reqeust, pk):
    profile = reqeust.user.profile
    project_obj = profile.project_set.get(id=pk)

    if reqeust.method == 'POST':
        project_obj.delete()
        return redirect('projects')

    context = {'object': project_obj}
    return render(reqeust, 'delete-template.html', context)
