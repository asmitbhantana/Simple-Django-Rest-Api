from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from clubs.models import *
from clubs.serializers import *
# Create your views here.
@csrf_exempt
def club_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def notices_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        clubNotics = Club.objects.all()
        serializer = ClubSerializerForNotice(clubNotics, many=True)
        return JsonResponse(serializer.data, safe=False)
