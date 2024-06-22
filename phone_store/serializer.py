from rest_framework import serializers
from .models import Marca, Celular, Especificaciones
from django.conf import settings

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CelularSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    
    class Meta:
        model = Celular
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        celular = super().create(validated_data)
        if image:
            celular.image_url = self.save_image(celular, image)
            celular.save()
        return celular

    def save_image(self, celular, image):
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('images', str(celular.id) + '_' + image.name), ContentFile(image.read()))
        return settings.MEDIA_URL + path

class EspecificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especificaciones
        fields = '__all__'



