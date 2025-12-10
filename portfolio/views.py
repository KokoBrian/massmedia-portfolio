from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, GalleryItem
from .forms import ContactForm
from bolt import run_flow

def index(request):
    return render(request, "portfolio/index.html", {
        "projects": Project.objects.all().order_by("-created_at")[:6]
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {"project": project})

def gallery(request):
    return render(request, "portfolio/gallery.html", {
        "items": GalleryItem.objects.all()
    })

def contact(request):
    form = ContactForm()
    return render(request, "portfolio/contact.html", {"form": form})

def generate_ai_description(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    ai = run_flow("auto_description", project.raw_description)
    project.description = ai
    project.save()
    return redirect("project_detail", pk=project_id)
