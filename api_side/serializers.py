from rest_framework import serializers


from .models import Entity, AddressImage


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
        user = self.context.get('request').user
        toilet = Entity.objects.create(username=user, **validated_data)
        return toilet



class ToiletsPointDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity













class ToiletAddressImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressImage
        fields = ('address_image',)