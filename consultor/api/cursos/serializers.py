from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

    def validate(self, data : dict):
        #Validate start date is before than end date
        start_date = data.get('fecha_inicio')
        end_date = data.get('fecha_fin')
   
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError({
                'fecha_inicio': 'La fecha de inicio debe ser anterior a la fecha de fin.',
                'fecha_fin': 'La fecha de fin debe ser posterior a la fecha de inicio.'
            })
        
        return data