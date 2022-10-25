from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)

@login_required
def show_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        "project_object": project,
    }
    return render(request, "projects/detail.html", context)
