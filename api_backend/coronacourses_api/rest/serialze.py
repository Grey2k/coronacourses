from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = models.Course
        fields = ["course_id", "name", "kind", "lecturer", "description"]
    course_id = serializers.CharField(read_only=True)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = ["id"]
    id = serializers.IntegerField()


class CourseMaintainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = models.CourseMaintainer
        fields = ["user", "course"]
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
