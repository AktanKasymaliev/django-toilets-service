from rest_framework import serializers, fields
from .models import Entity, AddressImage
from django.core.files.storage import FileSystemStorage




class ToiletAddressImageSerializer(serializers.ModelSerializer):
    address_image = serializers.ImageField(use_url=True)
    class Meta:
        model = AddressImage
        fields = ('toilet','address_image',)

    # def get_photo_url(self, queryset):
    #     request = self.context.get('request')
    #     photo_url = queryset.address_image.url
    #     return request.build_absolute_uri(photo_url)

    def create(self, validated_data):
        toilet_name = validated_data.pop('toilet')
        toilet_ad = AddressImage.objects.create(toilet=toilet_name, **validated_data)
        return toilet_ad


class ToiletsPointListSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id', 'username', 'address', 'longitude', 'latitude')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] =  instance.toilet.count() #ToiletAddressImageSerializer(instance.toilet.all(), many=True).data
        return representation                               # Сериализация фоток


class ToiletsPointsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id','username', 'address', 'longitude', 'latitude')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ToiletAddressImageSerializer(instance.toilet.all(), many=True).data
        return representation   


class ToiletsPointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('address', 'longitude', 'latitude')
    
    def create(self, validated_data):
        request = self.context.get('request')
        toilet_ad = Entity.objects.create(username=request.user, **validated_data)
        return toilet_ad



class ToiletsPointDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity

class ToiletsPointUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('address', 'longitude', 'latitude')
