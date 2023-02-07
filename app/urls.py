from django.urls import path
from app import views
urlpatterns = [
    path('',views.Studentlist.as_view()),
    path('add',views.create_student.as_view()),
    path('re/<int:pk>/',views.retive_student.as_view()),
    path('up/<int:pk>/',views.update_student.as_view()),
    path('del/<int:pk>/',views.destroy_student.as_view()),
    path('lc',views.student_listcreate.as_view()),
    path('rd/<int:pk>/',views.student_rede.as_view()),
    path('ru/<int:pk>/',views.student_reup.as_view()),
    path('rud/<int:pk>/',views.student_reupde.as_view())
]