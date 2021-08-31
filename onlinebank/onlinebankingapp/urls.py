from django.urls import path
from onlinebankingapp import views

urlpatterns=[
	path('login/',views.login_view),
	path('registration/',views.registration_view),
	path('change/',views.change_view),
	path('forget/',views.forget_view),
	path('deposit/',views.deposit_view),
	path('withdraw/',views.withdraw_view),
	path('balance/',views.balance_view),
	path('',views.home_view),
	path('display/',views.display_view),
	path('dummy1/',views.dummy1_view),
	path('bind/',views.bind_firstname),
	path('getidfirstname/',views.getid_firstname)
	
]