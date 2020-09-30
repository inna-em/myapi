from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from django.http import Http404
from PIL import Image, UnidentifiedImageError
from scipy.spatial import distance

from .models import Person
from .serializers import IdSerializer, PersonSerializer, VectorSerializer

class PersonsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        persons = Person.objects.all()
        serializer = IdSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'surname': request.data.get('surname')
        }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            person_saved = serializer.save()
            return Response(person_saved.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetails(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except ValidationError or ValueError:
            raise Http404
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def delete(self, request, id):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            img = Image.open(request.data.get('image'))
        except UnidentifiedImageError:
            return Response(data='Please, upload an image file!', status=status.HTTP_400_BAD_REQUEST)
        img_resized = (300, 300)
        new_img = img.resize(img_resized)
        bytes = new_img.tobytes()
        bytes_array = list(bytes)
        float_array = ["{:.3f}".format(x/255) for x in bytes_array]
        vector = ",".join(map(str, float_array))
        person = self.get_object(id)
        data = {}
        data['vector'] = vector
        serializer = VectorSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data='Upload successful', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Compare(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except ValidationError or ValueError:
            raise Http404
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id1, id2):
        person1 = self.get_object(id1)
        person2 = self.get_object(id2)
        if person1.vector and person2.vector:
            vector1 = []
            for x in person1.vector.split(","):
                vector1.append(float(x))
            vector2 = []
            for y in person2.vector.split(","):
                vector2.append(float(y))
            return Response(data=distance.euclidean(vector1,vector2), status=status.HTTP_200_OK)
        return Response(data='Please, provide two users with vector', status=status.HTTP_400_BAD_REQUEST)