from django.urls import path
from . import views

app_name='studapp'

urlpatterns = [
    path('',views.StudList.as_view(),name='studlist'),
    path('addstudent',views.AddStudent.as_view(),name='studadd'),
    path('studentdetail/<int:pk>',views.StudDetail.as_view(),name='studdetail'),
    path('updatestudent/<int:pk>',views.UpdateStudent.as_view(),name='updatestudent'),
    path('deletestudent/<int:pk>',views.DeleteStudent.as_view(),name='deletestudent')
]