from django.urls import path
from . import views


urlpatterns = [
    path('teacherlist/', views.TeacherRead.as_view(), name='teacherslist'),
    path('reports/', views.CreateTeacher.as_view(), name='createteachers'),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view(), name='teacher_detail'),   # detail
    path('teacher/update/<int:pk>/', views.TeacherUpdate.as_view(), name='updateteacher'),  # update
    path('teacher/delete/<int:pk>/', views.TeacherDelete.as_view(), name='deleteteacher'),  # delete
]
