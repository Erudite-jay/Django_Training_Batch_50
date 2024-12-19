
from django.urls import path
from . import views

urlpatterns = [
path("hello/",views.print_hello_world),
path("template/",views.print_hello_from_template),

path("all-data/",views.all_data),
path("sud/<int:pk>/",views.single_user_data)
]
