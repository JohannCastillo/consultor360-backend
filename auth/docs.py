from drf_spectacular.utils import extend_schema
from .serializers import UserSerializer, LoginSerializer

login_schema = extend_schema(
    description="Autentica al usuario y devuelve sus datos junto con el token de acceso.",
    summary="Login",
    request=LoginSerializer,
    responses=UserSerializer
)

register_schema = extend_schema(
    description="Registra un nuevo usuario y devuelve sus datos junto con el token de acceso.",
    summary="Register",
    methods=["POST"],
    request=UserSerializer,
    responses=UserSerializer,
)
