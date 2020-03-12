from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	#path('quotes/', views.QuoteListView.as_view(), name='quotes'),
    #path('quote/<int:pk>', views.QuoteDetailView.as_view(), name='quote-detail'),

]