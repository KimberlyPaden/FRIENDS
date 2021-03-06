from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Department
from django.contrib import messages

def Home(request):
    
    if request.method == "POST":
        if Employee.objects.filter(Id_Number=request.POST["ID_Number"]).exists() and Employee.objects.filter(Password=request.POST["password"]).exists():
            return redirect("dashboard")
        
        else:
            return redirect("home")               
    else:
        return render(request,'login.html')



def Register(request):
    
    if request.method == "POST":
        if Employee.objects.filter(Id_Number=request.POST["ID"]).exists():
            messages.error(request, "ID Number has been taken by another account")
            return redirect("register")
        
        elif Employee.objects.filter(Email=request.POST["email"]).exists():
            messages.warning(request, "Email has been taken by another account")
            return redirect("register")
        
        elif Employee.objects.filter(Contact=request.POST["contact_number"]).exists():
            messages.error(request, "Contact Number has been taken by another account")
            return redirect("register")    
            
        else:
            signUpEmployee = Employee(Id_Number = request.POST["ID"], Full_Name = request.POST["full_name"],Email = request.POST["email"], Contact = request.POST["contact_number"], Password = request.POST["password"])
            signUpEmployee.save()
            id = Employee.objects.get(Id_Number = request.POST["ID"])
            signUpDepartment = Department(Id_Number=id, department=request.POST["Department"],Status_Dept=request.POST["Status"])    
            signUpDepartment.save()
            return redirect("home")
    
    else:
        return render(request,"Sign-Up.html")


    
def Dashboard(request):
    return render(request,"Dashboard.html")