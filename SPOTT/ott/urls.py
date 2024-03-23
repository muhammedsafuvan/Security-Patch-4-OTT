from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("home/", views.home, name="home"),
	path("play/", views.play, name="play"),
	path("face/", views.face, name="face"),
	path("blocked/", views.blocked, name="blocked"),
	path("device",views.device,name="dev"),
	path("audio",views.audio,name="aud"),
	path("start/",views.start, name ="start"),
	path("flagcall",views.flagcall,name="flagcall")

]
