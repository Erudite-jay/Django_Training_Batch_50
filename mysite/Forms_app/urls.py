from django.urls import path
from . import views
urlpatterns = [
   path("c/",views.contact_view)
]
