from django.db.models import Q
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer
# Documentation
from .docs import *


@extend_schema(tags=["cursos"])
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @curso_list_schema
    def list(self, request):
        return super().list(request)

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
