from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_note, name='list_note'),
    path('add', views.add_note, name='add_note'),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name='delete_note'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='update_note'),
]
