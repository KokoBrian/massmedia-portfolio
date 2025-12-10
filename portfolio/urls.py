from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("ai/generate/<int:project_id>/", views.generate_ai_description, name="generate_ai"),
]
