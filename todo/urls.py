from django.urls import path
from . import views


urlpatterns = [
    path('addtask/', views.AddTask, name='addtask'),
    path('mark_as_done/<int:pk>/', views.MarkTask, name='mark_as_done'),
    path('delete_task/<int:pk>', views.DeleteTask, name='delete_task'),
    path('mark_as_undone/<int:pk>', views.MarkUndone, name='mark_as_undone'),
    path('edit_task/<int:pk>', views.EditTask, name='edit_task'),
]