
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact')
]