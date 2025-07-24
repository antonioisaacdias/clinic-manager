from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from .models import Professional, Specialty
from django.shortcuts import get_object_or_404

from .serializers import ProfessionalSerializer, SpecialtySerializer

class ProfessionalViewSet(viewsets.ModelViewSet):

    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    lookup_field = 'uuid'

    @action(detail=True, methods=['get', 'post', 'delete'], url_path='specialties')
    def manage_specialties(self, request, uuid=None):
        professional = self.get_object()
        
        if request.method == 'GET':
            specialty_data = professional.list_specialties()
            return Response(specialty_data, status=status.HTTP_200_OK)
        
        elif request.method == 'POST':
            specialty_uuid = request.data.get('specialty_uuid')
            if not specialty_uuid:
                return Response({
                    'error': 'MISSING_SPECIALTY_UUID',
                    'message': 'O UUID da especialidade é obrigatório',
                    'field': 'specialty_uuid'
                }, status=status.HTTP_400_BAD_REQUEST)

            specialty = get_object_or_404(Specialty, uuid=specialty_uuid)
            
            if specialty in professional.specialties.all():
                return Response({
                    'error': 'SPECIALTY_ALREADY_EXISTS',
                    'message': 'Especialidade já associada a este profissional'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            professional.add_specialty(specialty)
            return Response(status=status.HTTP_200_OK)
        
        if request.method == 'DELETE':
            specialty_uuid = request.data.get('specialty_uuid')

            if not specialty_uuid:
                return Response({
                    'error': 'MISSING_SPECIALTY_UUID',
                    'message': 'O UUID da especialidade é obrigatório',
                    'field': 'specialty_uuid'
                }, status=status.HTTP_400_BAD_REQUEST)

            specialty = get_object_or_404(Specialty, uuid=specialty_uuid)

            if specialty not in professional.specialties.all():
                return Response({
                    'error': 'SPECIALTY_NOT_FOUND',
                    'message': 'Especialidade não encontrada para este profissional'
                }, status=status.HTTP_404_NOT_FOUND)

            professional.remove_specialty(specialty)
            return Response(status=status.HTTP_204_NO_CONTENT)

class SpecialtyViewSet(viewsets.ModelViewSet):

    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    lookup_field = 'uuid'

