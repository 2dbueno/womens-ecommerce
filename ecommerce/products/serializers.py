from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        if not (1 <= len(images_data) <= 4):
            raise serializers.ValidationError("É necessário enviar de 1 a 4 imagens.")
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data is not None:
            # Exemplo simples: remove imagens antigas e adiciona as novas
            instance.images.all().delete()
            if not (1 <= len(images_data) <= 4):
                raise serializers.ValidationError("É necessário enviar de 1 a 4 imagens.")
            for image_data in images_data:
                ProductImage.objects.create(product=instance, **image_data)
        return instance
