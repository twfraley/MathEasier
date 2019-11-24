from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#@csrf_exempt
#def get_data(request):
#    data = EXAMPLEMODEL.objects.all()
#    if request.method == 'GET':
#        serializer = EXAMPLESERIALIZER(data, many=True)
#        return JsonResponse(serializer.data, safe=False)