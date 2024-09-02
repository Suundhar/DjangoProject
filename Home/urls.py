from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="home"),
    path("about.html", views.about, name="about"),
    path("404.html", views.error, name="404_html"),
    path("feature.html", views.feature, name="feature_html"),
    path("service.html", views.service, name="service_html"),
    path("team.html", views.team, name="team_html"),
    path("contact.html", views.contact, name="contact_html"),
    path("testimonial.html", views.testimonial, name="testimonial_html"),
    path("appointment.html", views.appointment, name="appointment_html"),
    path("appointment_user",views.appointment_user,name="appointment_user"),
    path("updateuser",views.updateuser,name="updateuser"),
    path("loginuser",views.loginuser,name="loginuser"),
]