from django.urls import path


from analyse import views


urlpatterns=[
    path('',views.index,name="analyse_index")
]