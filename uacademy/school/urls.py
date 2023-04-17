from django.urls import path
from . import views


urlpatterns = [
    path('', views.GradesActiveView.as_view(), name='grades'),
    path('subjects_all', views.SubjectsAllView.as_view(), name='subjects_all'),
   # path('courses/<slug:grade_id>/', views.CoursesView.as_view(), name='courses'),
    path('courses/<slug:slug>/', views.CoursesView.as_view(), name='courses'),
    path('topics/', views.show_topics, name='topics'),
#   path('subjects_all', views.show_subjects_all, name='subjects_all'),
#   path('<int:gradeid>/', subjects)
#   path('<int:id>', views.SubjectsView.as_view(), name='subjects'),
]
