from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('blogs',views.bloglist,name='blogs'),
    path('blog/<str:slug>',views.blogpage,name='blogpage'),
    path('createblog',views.createblog,name='createblog'),
    path('updateblog/<int:id>',views.updateblog,name='updateblog'),
    path('delete/<int:id>',views.deleteblog,name='deleteblog'),
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.logoutuser,name='logoutuser'),
    path('addtopic',views.addtopic,name='addtopic')
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
