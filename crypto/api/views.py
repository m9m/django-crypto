from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
  return JsonResponse({"version": "1.0.0"})