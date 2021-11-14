from django.shortcuts import render
from .drugner import druglist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DrugListSerializer
from .models import DrugList

# This view is used to get medicine from text
class Medicine(APIView):
    def post(self, request, *args, **kwargs): 

        # Taking text input from user  
        text = request.POST.get('text')

        # Example text
        dtext = "X-rays were negative and physical assessment determined soft tissue damage to the lateral aspect of her ankle. She was initially treated with ice, an ace wrap, crutches and mild pain medications (Albendazole with)"

        # Getting all salt name from text
        dlist = druglist(text)

        # Getting all medicine name and showing only 2 for first salt 
        medications = DrugList.objects.filter(salt_name=dlist[0])[:2]

        data = DrugListSerializer(medications, many=True) # serialization of data
        return Response({'status': 'SUCCESS', 'data': data.data},status=status.HTTP_200_OK)
