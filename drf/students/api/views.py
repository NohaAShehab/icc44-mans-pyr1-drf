############### Django rest framework ?
## you need response , --> this is a api ?

from rest_framework.response import Response
from rest_framework.decorators import api_view

from students.models import Student
from students.api.serializers import StudentSerializer


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


# @api_view(['GET'])
# def index(request):
#     students= Student.get_all_students()  # query set of model objects
#     serlized_students=  []
#     for std in students:
#         serlized_students.append({"name":std.name, "id":std.id, 'image':std.image.url})  # serialization model object
#     return Response({"message": "students data receieved", 'students':serlized_students})


# create serializer for model objects
# use serilizer with the model object

# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         # {
#         #     "name": "ssss",
#         #     "email": "mmm@ggg.comss",
#         #     "grade": 10,
#         # }
#         request_data = request.data
#         name = request_data['name']
#         email = request_data['email']
#         grade = request_data['grade']
#         student = Student(name=name, email=email, grade=grade)
#         student.save()
#         return Response({"messsage": 'object add received', 'id':{student.id}}, status=201)
#
#     students = Student.get_all_students()  # query set of model objects
#     serlized_students = []
#     for std in students:
#         serialized_student = StudentSerializer(std).data
#         print(serialized_student)
#         serlized_students.append(serialized_student)
#
#     return Response({"message": "students data receieved", 'students': serlized_students})


# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         request_data = request.data
#         # name = request_data['name']
#         # email = request_data['email']
#         # grade = request_data['grade']
#         # student = Student.objects.create(name=name, email=email, grade=grade)
#         print(request_data) # dict
#         student = Student.objects.create(**request_data)
#         return Response({"messsage": 'object add received', 'id':{student.id}}, status=201)
#
#     students = Student.get_all_students()  # query set of model objects
#     serlized_students = []
#     for std in students:
#         serialized_student = StudentSerializer(std).data
#         print(serialized_student)
#         serlized_students.append(serialized_student)
#
#     return Response({"message": "students data receieved", 'students': serlized_students})


# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         request_data = request.data
#         print(request_data) # dict
#         student = Student.objects.create(**request_data)
#         serlized_student = StudentSerializer(student).data
#         return Response({"messsage": 'object add received', 'student':serlized_student}, status=201)
#
#     elif request.method=='GET':
#         students = Student.get_all_students()  # query set of model objects
#         serlized_students = []
#         for std in students:
#             serialized_student = StudentSerializer(std).data
#             print(serialized_student)
#             serlized_students.append(serialized_student)
#
#     return Response({"message": "students data receieved", 'students': serlized_students})





@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response({"messsage": 'object add received', "student":student.data}, status=201)
        return Response(student.errors, status=400)

    elif request.method=='GET':
        students = Student.get_all_students()  # query set of model objects
        serlized_students = StudentSerializer(students, many=True)
        return Response({"message": "students data receieved", 'students': serlized_students.data})




### operations on specific object

@api_view(['GET', 'DELETE', 'PUT'])
def student_resource(request, id):
    student = Student.objects.filter(id=id).first()
    if request.method=='GET':
        student = Student.objects.filter(id=id).first()
        serlized_student = StudentSerializer(student)
        return Response({'data':serlized_student.data}, status=200)

    elif request.method=='DELETE':
        student.delete()
        return Response({"message":"object deleted"}, status= 204)

    elif request.method=="PUT":
        serlized_student = StudentSerializer(instance=student,data=request.data)
        if serlized_student.is_valid():
            serlized_student.save()
            return Response({"messsage": 'object add received', "student": serlized_student.data}, status=201)
        return Response(serlized_student.errors, status=400)
