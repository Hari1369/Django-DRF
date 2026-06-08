from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Employee
from .serializers import EmployeeSerializers

from django.shortcuts import render



@api_view(['GET','POST'])
def employee_list(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        if not employee.exists():
            return Response({"message": "No data found!"})
        serializer = EmployeeSerializers(employee, many=True)
        return response(serializer.data)
    
    elif request.method == "POST":
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'messsage':'data recieved'})
        
        return Response(serializer.errors)
