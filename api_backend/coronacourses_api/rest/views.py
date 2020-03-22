from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Course
from .serialze import CourseSerializer, UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "course_id"

    def list(self, request):
        queryset = Course.objects.none()
        user = request.user
        if user:
            queryset = Course.objects.filter(admins=user)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "username"

    def create(self, request):
        raise 

    def update(self, request, pk=None):
        raise

    def partial_update(self, request, pk=None):
        raise

    def destroy(self, request, pk=None):
        raise
