from django.contrib import admin
from django.urls import path
from webapp.views import index_view, task_add_view, delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('tasks/add/', task_add_view),
    path('delete/<int:id>/', delete),
]
