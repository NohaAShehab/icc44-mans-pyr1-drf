

from django.urls import path
from students.api.views import  hello, acceptData, index, student_resource

urlpatterns = [
    path('hello',hello, name='hello' ),
    # path('h', hello_api),
    path('accept', acceptData),
    path('', index, name='api.index'),
    path('<int:id>',student_resource, name='api.student_resource')
]