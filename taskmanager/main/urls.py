from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='detail-task'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete-task')
]
