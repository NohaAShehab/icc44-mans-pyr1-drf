from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse


### create api for my application
## return with data in JSON Format
def get_all_students(request):
    students = [
        {"id": 1, "name": 'Ahmed'},
        {'id': 2, 'name': 'Ali'}
    ]
    return JsonResponse({"students": students})


@csrf_exempt
def accept_student_data(request):
    if request.method == 'POST':
        print(request.POST)  # empty
        print(request.body)  # convert to dict --> then it can be represented in json response
        # serilization
        received_data = json.loads(request.body)
        print(received_data)
        return JsonResponse({"info": "post request received", 'data': received_data})

    return JsonResponse({"info": 'Request accepted'})
