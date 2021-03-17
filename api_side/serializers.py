from rest_framework import serializers, fields
from .models import Entity, AddressImage, Comment
from django.core.files.storage import FileSystemStorage



# Image
# -------------------------------------------------------------------------------------------------
class AddressImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = AddressImage
            fields = ('id','toilet', 'address_image')

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['toilet'] = instance.toilet.address
            representation['region'] = instance.toilet.region
            return representation


class AddressImageCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = AddressImage
            fields = ('toilet', 'address_image')

        def create(self, validated_data):
            request = self.context.get('request')
            toilet_id = validated_data.pop('toilet')
            print(request.data)
            rest = AddressImage.objects.create(toilet=toilet_id, address_image=request.data['address_images'])
            return rest

class AddressImageCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressImage
        fields = ('toilet', 'address_image')
        

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.toilet = validated_data.get('toilet', instance.toilet)
        instance.address_image = request.data['address_images']
        instance.save()
        return instance
        
# -------------------------------------------------------------------------------------------------

# Restroom points
# -------------------------------------------------------------------------------------------------
class ToiletsPointListSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id', 'username', 'region', 'address', 'longitude', 'latitude')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.username.username
        representation['region'] = instance.region
        representation['images'] =  instance.toilet.count()
        representation['comments'] = instance.restroom.count()
        return representation

class ToiletsPointsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id','username', 'region', 'address', 'longitude', 'latitude')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = AddressImageSerializer(instance.toilet.all(), many=True).data
        representation['region'] = instance.region
        representation['username'] = instance.username.username
        representation['comments'] = ComentSerializer(instance.restroom.all(), many=True).data
        return representation   


class ToiletsPointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('address', 'region', 'longitude', 'latitude')
    
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
        fields = ('address', 'region', 'longitude', 'latitude')
# -------------------------------------------------------------------------------------------------


# Comments 
# -------------------------------------------------------------------------------------------------
class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = instance.owner.username
        representation['region'] = instance.restroom.region
        representation['restroom'] = instance.restroom.address
        return representation

class ComentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('message', 'restroom')

    def create(self, validated_data):
        request = self.context.get('request')
        comment = Comment.objects.create(owner=request.user, **validated_data)
        return comment

class ComentCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')
# -------------------------------------------------------------------------------------------------
