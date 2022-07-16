from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blogpost', views.blog_post, name="blog-post"),
    path('login', views.u_login, name="ulogin"),
    path('register', views.register, name="uregister"),
    path('logout', views.u_logout, name="ulogout"),
    path('blog_detail/<int:id>', views.blog_detail, name='blogdetail'),
    path('edit/<int:id>', views.edit, name='uedit'),
    path('delete/<int:id>', views.delete, name='udelete'),
]
