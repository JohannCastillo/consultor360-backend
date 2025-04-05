from django.db.models import Q
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer
# Documentation
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


@extend_schema(tags=["cursos"])
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='estado',
                description='Filtra los cursos por estado activo.',
                required=False,
                enum=["activo", "inactivo", "activo,inactivo"],
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name='nombre',
                description='Filtra los cursos por nombre.',
                required=False,
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name='descripcion',
                description='Filtra los cursos por descripción.',
                required=False,
                type=OpenApiTypes.STR,
            ),
        ],
        description="Obtiene una lista de cursos. Puedes filtrar por el parámetro 'activo'."
    )
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
