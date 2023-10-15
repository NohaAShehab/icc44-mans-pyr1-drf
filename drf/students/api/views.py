############### Django rest framework ?
## you need response , --> this is a api ?

from rest_framework.response import Response
from rest_framework.decorators import api_view

from students.models import Student


# you need to tell the view that is a drf view

@api_view(['GET'])
def hello(request):
    return Response({"data": "Hello World!"})


@api_view(['POST', 'GET'])
def acceptData(request):
    if request.method == 'POST':
        # get request content from request.data ---> serialization request body parameter  and put it
        # in request.data
        return Response({"data": request.data, 'message': "data received"}, status=200)
    return Response({"data": 'GET request received'})



### generate api to display all students


@api_view(['GET'])
def index(request):
    students= Student.get_all_students()  # query set of model objects
    serlized_students=  []
    for std in students:
        serlized_students.append({"name":std.name, "id":std.id, 'image':std.image.url})  # serialization model object
    return Response({"message": "students data receieved", 'students':serlized_students})


# create serializer for model objects  






