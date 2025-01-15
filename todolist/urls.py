from django.urls import path

# import my_view from todo Application
# from .views import my_view

# urlpatterns = [
#     path('', my_view, name='my_view')
# ]

# import View dari todo Application
from .views import index_view, detail_view, create_view, update_view, delete_view
from django.contrib.auth import views as auth_views

app_name = 'todolist'
urlpatterns = [
    # route untuk halaman daftar task
    path('', index_view, name='index'),
    # route untuk halaman detail task
    path('<int:task_id>', detail_view, name='detail'),
    # url untuk halaman tambah task
    path('create', create_view, name='create'),
    # url untuk halaman ubah task
    path('update/<int:task_id>', update_view, name='update'),
    # url untuk menghapus task
    path('delete/<int:task_id>', delete_view, name='delete'),
    # route untuk login
    path('login/', auth_views.LoginView.as_view(template_name='todolist/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]