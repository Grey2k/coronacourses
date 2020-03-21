from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Course, CourseMaintainer
from .serialze import CourseSerializer, CourseMaintainerSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Course.objects.none()
        user = request.user
        if user:
            queryset = Course.objects.filter(coursemaintainer__user=user)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


class CourseMaintainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CourseMaintainer.objects.all()
    serializer_class = CourseMaintainerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #def list(self, request):
    #    queryset = CourseMaintainer.objects.none()
    #    serializer = CourseMaintainerSerializer(queryset)
    #    return Response(serializer.data)
