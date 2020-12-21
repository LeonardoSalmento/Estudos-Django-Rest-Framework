from django.http import HttpResponse, JsonResponse
from school.grades.models import Student
from school.grades.serializers import StudentSerializer
from rest_framework import viewsets

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



def grades(request):
    if request.method == 'GET':
        student = Student.objects.first()
        serializer = StudentSerializer(student)
        
        return JsonResponse(serializer.data)
