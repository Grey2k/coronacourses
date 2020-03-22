from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Course
from .serialze import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
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