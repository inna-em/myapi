from rest_framework import serializers
from persons.models import Person

class IdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id',)


class PersonSerializer(serializers.ModelSerializer):
    has_vector = serializers.SerializerMethodField('check_vector')

    def check_vector(self, obj):
        return True if obj.vector else False

    class Meta:
        model = Person
        fields = ('name',
                  'surname',
                  'has_vector')

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

class VectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('vector', )

    def update(self, instance, validated_data):
        instance.vector = validated_data.get('vector', instance.vector)
        instance.save()
        return instance