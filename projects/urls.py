from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.projects, name="list"),
    path("<slug>",views.project_detail,name="detail"),
]
