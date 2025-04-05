from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes
from .serializers import CursoSerializer

AUTH_HEADER_SCHEMA = OpenApiParameter(
    name="Authorization",
    description="Token para autenticación. Ejemplo: Token [token]",
    required=False,
    type=OpenApiTypes.STR,
    location=OpenApiParameter.HEADER,
)

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

curso_create_schema = extend_schema(
    description="Crea un nuevo curso. Requiere autenticación con un token de acceso.",
    summary="Crear curso",
    request=CursoSerializer,
    responses={201: CursoSerializer},
    parameters=[
        AUTH_HEADER_SCHEMA
    ],
)

curso_update_schema = extend_schema(
    description="Actualiza un curso. Requiere autenticación con un token de acceso.",
    summary="Actualizar curso",
    request=CursoSerializer,
    responses={200: CursoSerializer},
    parameters=[
        AUTH_HEADER_SCHEMA
    ],
)

curso_destroy_schema = extend_schema(
    description="Elimina un curso. Requiere autenticación con un token de acceso.",
    summary="Eliminar curso",
    responses={204: None},
    parameters=[
        AUTH_HEADER_SCHEMA
    ],
)
