"""
URL configuration for abc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from abc_project import view
from srvc import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.Home,name="home"),
    path('AboutUs/', view.AboutUs),
    path('Service/', view.Service),
    path('Price/', view.Price),
    path('Import/', view.Import),
    path('Hardware/', view.Hardware),
    path('Software/', view.Software),
    path('Crude/', view.Crude),
    path('Motor/', view.Motor),
    path('Mechanical/', view.Mechanical),
    path('Export/', view.Export),
    path('Register/', view.Register,name="regg"),
    path('Login/', view.Login,name="login"),
    path('Forget/', view.Forget),
    path('Learn/', view.Learn),
    path('track/', view.track,name="trackk"),
    # srvc views
    path('rgst/', view.rgst,name="rgst"),
    path('singin/', view.singin, name="singin"),
    path('impform/', view.impform,name="importform"),
    path('Exform/', view.Exform,name="exorder"),
    path('Contact/', view.Contact,name="cont"),
    path('Feedback/', view.Feedback,name="feed"),
    path('singout/', view.singout, name='singout'),
    path('app/', include('export_dyp.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)