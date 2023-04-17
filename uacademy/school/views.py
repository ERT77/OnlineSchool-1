from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView


#def show_grades(request):
 #   grades = Grade.objects.all
  #  return render(request, 'school/grades.html', {'grades': grades})


class GradesActiveView(ListView):
    model = Grade
    template_name = 'school/grades.html'
    context_object_name = 'grades'

    def get_queryset(self):
        return Grade.objects.filter(is_active=True)


class SubjectsAllView(ListView):
    model = Subject
    template_name = 'school/subjects_all.html'
    context_object_name = 'subjects'

'''
class CoursesView(DetailView):
    model = Subject
    template_name = 'school/grade_subjects.html'
    context_object_name = 'grade_subjects'

    def get_queryset(self):
           return Subject.objects.filter(is_active=True)
      #  return Subject.objects.filter(subject__slug=self.kwargs['grade_subject_slug'], is_active=True)
'''

class CoursesView(ListView):
    model = GradeSubject
    template_name = 'school/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return GradeSubject.objects.filter(is_active=True, grade_id=1) #заглушка


def show_topics(request):
    return render(request, 'school/topics.html')


#def subjects(request, gradeid):
#    return HttpResponse(f"<h1>Оберіть предмет {gradeid} класу</h1>")
