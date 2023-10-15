
from  django.urls import path, include
from students.views import  get_all_students, accept_student_data

urlpatterns = [

    path('api/', include('students.api.urls')),
    path('', get_all_students),
    path('new', accept_student_data)

]