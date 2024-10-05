from django.contrib import admin
from django.urls import path, re_path  # Import re_path for regex support
from StudentApp import views

urlpatterns = [
    re_path(r'^student$', views.studentApi, name='student_api'),  # Use re_path for regex URLs
    re_path(r'^student/([0-9]+)$', views.studentApi, name='student_api_with_id'),  # Use re_path for regex URLs
    path('admin/', admin.site.urls),
]
