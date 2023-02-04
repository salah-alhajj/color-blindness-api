from django.core.files.storage import default_storage, FileSystemStorage
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Proccesser.proccesser import proccessImage


@api_view(['POST'])
def index(request):
    image = request.FILES['image']

    # path = default_storage.save('uploads/' + request.FILES['image'].name, request)
    fs = FileSystemStorage()
    filename = fs.save("uploads/"+image.name, image)
    type_convert = request.data['type']
    type_convert = type_convert.lower()
    print(type_convert)


    result = proccessImage(type_convert, filename)

    if result :
        return Response({'link': result}, status=200)
    else:
        return Response({'error': 'type not found'}, status=400)

