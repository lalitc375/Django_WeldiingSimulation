from django.conf.urls import include, url
from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^signup',views.signup,name='signup'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^basicInputData',views.basicInputData.as_view(),name='basicInputData'),
    url(r'^advanceInputData',views.advanceInputData.as_view(),name='advanceInputData'),
    url(r'^advanceinput',views.advanceinput,name='advanceinput'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^basicinput',views.basicinput,name='basicinput'),
    url(r'^signUpData',views.signUpData.as_view(),name='signUpData'),
    url(r'^forgotPassword',views.forgotPassword,name='forgotPassword'),
    url(r'^requestPassword',views.requestPassword.as_view(),name='requestPassword'),
    url(r'^updateprofile',views.updateProfile,name='updateProfile'),
    url(r'^updateProfileData',views.updateProfileData.as_view(),name='updateProfileData'),










    ]
