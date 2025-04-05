from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes

curso_list_schema = extend_schema(
    description="Obtiene una lista de cursos.",
    summary="Listar cursos",
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
)
