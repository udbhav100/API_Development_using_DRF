
from rest_apis.api.serializers import  Registeruser

from django.contrib.auth.models import User
from rest_framework import status,permissions
from rest_framework.response import Response

from rest_apis.api.serializers import CertificationSerializer
from rest_apis.models import certification
from rest_framework.views import APIView
class Certification(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serial = CertificationSerializer(data=request.data)
        if serial.is_valid():
            serial.create(request.user)
            return Response([{"success":"Certification added"}],status=status.HTTP_200_OK)
        else:
            return Response([serial.errors],status=status.HTTP_400_BAD_REQUEST)
         
    def get(self,request):
        try:
            certificates = certification.objects.filter(user=request.user)
            data_list = CertificationSerializer(certificates,many=True)
            return Response(data_list.data,status=status.HTTP_200_OK)
        except:
            return Response([{"failure":"No certifications found"}],status=status.HTTP_404_NOT_FOUND)




