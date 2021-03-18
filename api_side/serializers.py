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
class RestroomsSerializer(serializers.ModelSerializer):
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
    address_image = AddressImageSerializer(many=True, required=False)
    class Meta:
        model = Entity
        fields = ('address', 'region', 'longitude', 'latitude','address_image')
    
    def create(self, validated_data):
        request = self.context.get('request')
        toilet_ad = Entity.objects.create(username=request.user, **validated_data)
        for image_data in request.data.pop('address_image'):
            created = AddressImage.objects.create(address_image=image_data, toilet=toilet_ad)
            toilet_ad.toilet.add(created)
        return toilet_ad

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = AddressImageSerializer(instance.toilet.all(), many=True).data
        return representation   


class ToiletsPointDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity

class ToiletsPointUpdateSerializer(serializers.ModelSerializer):
    address_image = AddressImageSerializer(many=True, required=False)
    class Meta: 
        model = Entity
        fields = ('address', 'region', 'longitude', 'latitude', 'address_image')


    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.address = validated_data.get('address', instance.address)
        instance.region = validated_data.get('region', instance.region)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        try:
            images_data = request.data.pop('address_image')
        except:
            images_data = None

        if images_data is not None:
            for image_data in images_data:
                image_created = AddressImage.objects.create(address_image=image_data, toilet=instance)
                instance.toilet.add(image_created)

        instance.save()
        return instance
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
