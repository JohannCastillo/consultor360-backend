# implementar un viewset para cursos
from rest_framework import viewsets
from rest_framework.response import Response

class CursoViewSet(viewsets.GenericViewSet):
    def list(self, _):
        return Response({"message": "Hello, World!"})