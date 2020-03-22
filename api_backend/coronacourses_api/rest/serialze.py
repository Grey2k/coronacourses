from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = models.Course
        fields = ["id", "course_id", "name", "kind", "lecturer", "description", "admins"]
    course_id = serializers.CharField(read_only=True)
    admins = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = User
        fields = ["id"]
    id = serializers.IntegerField()
