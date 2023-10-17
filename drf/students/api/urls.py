

from django.urls import path, include
from students.api.views import  hello, acceptData, index, student_resource,StudentModelViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'stds',StudentModelViewSet, basename='stds')
urlpatterns = [
    path('hello',hello, name='hello' ),
    # path('h', hello_api),
    path('accept', acceptData),
    path('', index, name='api.index'),
    path('<int:id>',student_resource, name='api.student_resource'),
    # path('gen', StudentModelViewSet.as_view({"get":'list', 'post':'create', 'put':'update'}))
    path('gen/', include(router.urls))
]