from django.shortcuts import render
from admissions.models import student
from admissions.forms import studentmodelforms
from django.views.generic import DeleteView
# from django.http import HttpResponse

# Create your views here.
# def homepage(request):
#     return render(request,'index.html')


# def newadmissions(request):
#     form=studentmodelforms
#     studentform={'form':form}

#     #saving data
#     if request.method=='POST':
#         form=studentmodelforms(request.POST)
#         if form.is_valid():
#             form.save()
#             print("data saved")

    

#     return render(request,'admissions/newadmission.html',studentform)
   

# def reports(request):
#     result=student.objects.all()
#     students={'allstudents':result}
#     return render(request,'admissions/report.html',students)

# def deletestudent(request,id):
#     s=student.objects.get(id=id)
#     s.delete()
#     result=student.objects.all()
#     students={'allstudents':result}
#     return render(request,'admissions/report.html',students)


# def updatestudent(request,id):
#     s=student.objects.get(id=id)
#     form=studentmodelforms(instance=s)
#     dict={'form':form}

#     if request.method=='POST':
#         form=studentmodelforms(request.POST,instance=s)
#         if form.is_valid():
#             form.save()
#         return reports(request)

    
#     return render(request,'admissions/update.html',dict)


# class StudentDetail(DeleteView):
#     model=student
#     template_name = "admissions/student_detail.html" 


from django.shortcuts import render, redirect, get_object_or_404
from admissions.models import student
from admissions.forms import studentmodelforms
from django.views.generic import DetailView

def homepage(request):
    return render(request, 'index.html')

def newadmissions(request):
    if request.method == 'POST':
        form = studentmodelforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentslist')  # ✅ redirect after save
    else:
        form = studentmodelforms()
    return render(request, 'admissions/newadmission.html', {'form': form})

def reports(request):
    result = student.objects.all()
    return render(request, 'admissions/report.html', {'allstudents': result})

def deletestudent(request, id):
    s = get_object_or_404(student, id=id)
    s.delete()
    return redirect('studentslist')  # ✅ redirect to list after delete

def updatestudent(request, id):
    s = get_object_or_404(student, id=id)
    if request.method == 'POST':
        form = studentmodelforms(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return redirect('studentslist')  # ✅ redirect after update
    else:
        form = studentmodelforms(instance=s)
    return render(request, 'admissions/update.html', {'form': form})

# ✅ Corrected: StudentDetail should be a DetailView, not DeleteView
class StudentDetail(DetailView):
    model = student
    template_name = "admissions/student_detail.html"
    context_object_name = "student"

    

