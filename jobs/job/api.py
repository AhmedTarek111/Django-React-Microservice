from .serializers import JobSerializer,JobApplySerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Job,JobApply

class JobListCreateApi(ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

class JobRetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()