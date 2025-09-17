from django.urls import path
from . import views

urlpatterns = [
    path('newaddmission/', views.newadmissions, name='newadmission'),
    path('reports/', views.reports, name='studentslist'),
    path('deletestudent/<int:id>/', views.deletestudent, name='deletestudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('studentdetail/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
]
