from django.urls import include, path
from . import views

urlpatterns = [
  path('getencuesta', views.get_encuesta),
  path('addencuesta', views.add_encuesta),
  path('updateencuesta/<int:encuesta_id>', views.update_encuesta),
  path('deleteencuesta/<int:encuesta_id>', views.delete_encuesta)
]
