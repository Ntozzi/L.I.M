from django.views import generic
from .models import Project

class ProjectList(generic.ListView):
    template_name = 'portfolio/home.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(selfself):
        return Project.objects.all()