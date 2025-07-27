from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Professional, Specialty
from django.shortcuts import get_object_or_404
from .serializers import ProfessionalSerializer, SpecialtySerializer
from rest_framework.pagination import PageNumberPagination

class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    lookup_field = 'uuid'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Use o serializer para garantir o tratamento correto da foto
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        # Agora, customize para retornar apenas as informações desejadas
        data = []
        for item in serializer.data:
            data.append({
                'uuid': item['uuid'],
                'name': item['name'],
                'specialties': [s['name'] if isinstance(s, dict) else s for s in item.get('specialties', [])],
                'photo': item['photo'],
            })
        return Response(data)

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

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100  # limite máximo opcional

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    lookup_field = 'uuid'
    pagination_class = CustomPagination  # Adicione esta linha

    def get_queryset(self):
        queryset = Specialty.objects.all().order_by('-is_active', 'name')
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == "true")
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

