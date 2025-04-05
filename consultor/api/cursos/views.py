from django.db.models import Q
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# Documentation
from .docs import *


@extend_schema(tags=["cursos"])
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]  # Requiere autenticación para estas acciones
        return super().get_permissions()
    
    @curso_list_schema
    def list(self, request):
        return super().list(request)
    
    @curso_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @curso_update_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @curso_destroy_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        text_filters = ["nombre", "descripcion"]
        status = self.request.query_params.get("estado", None)

        query = Q()

        # Handle text filters
        for field in text_filters:
            value = self.request.query_params.get(field, None)
            if value:
                query &= Q(**{f"{field}__icontains": value})

        # Handle status filter
        if status is not None:
            status_map = {
                "activo": True,
                "inactivo": False,
            }
            if status in status_map:
                queryset = queryset.filter(activo=status_map[status])

        return queryset.filter(query)
