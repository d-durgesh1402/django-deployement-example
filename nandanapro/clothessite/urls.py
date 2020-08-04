from django.contrib import admin
from django.conf.urls import url,include
from clothessite import views
app_name='clothessite'
urlpatterns=[
url(r'^westerndress/$',views.westerndress,name='westerndress'),
url(r'^indowesterndress/$',views.indowesterndress,name='indowesterndress'),
url(r'^sareedress/$',views.sareedress,name='sareedress'),
url(r'^indiandress/$',views.indiandress,name='indiandress'),
url(r'^startuppage/$',views.startuppage,name='startuppage'),
url(r'user_login/$',views.user_login,name='user_login'),
url(r'^registration/$',views.registration,name='registration'),
url(r'^contactus/$',views.contactus,name='contactus'),
url(r'^location/$',views.location,name='location'),
url(r'^shipping/$',views.shipping,name='shipping'),
url(r'^privacy/$',views.privacy,name="privacy"),
url(r'^returnrule/$',views.returnrule,name="returnrule"),
]
