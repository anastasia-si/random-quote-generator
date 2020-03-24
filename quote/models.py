from django.db import models
from django.urls import reverse 


class QuoteType(models.Model):

	"""
	Model to represent a quote type (funny, inspirational, etc.)
	"""

	QUOTE_TYPES = [
		('ins', 'Inspiring'),
		('fun', 'Funny'),
		('mot', 'Motivational'),
		('dem', 'Demotivational'),
		('tru', 'Truthful')
	]

	name = models.CharField(max_length=3, choices=QUOTE_TYPES, help_text='Quote category')

	def __str__(self):        
		return dict(self.QUOTE_TYPES)[self.name]


class Author(models.Model):

	"""
	Model to represent an author of a quote
	"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	class Meta:
		ordering = ['last_name', 'first_name']

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Quote(models.Model):
	"""
	Model to represent a quote:
		text - quote text
		author - quote author
		user - user who posted a quote
		quotetype - a quote type (funny, inspirational, etc.)

	"""
	text = models.TextField(max_length=500)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
	user = models.CharField(max_length=100, null=True)
	quotetype = models.ManyToManyField(QuoteType) #, help_text='Please select a quote type:'
	created_date = models.DateField(null=False, auto_now=True)

	def __str__(self):
		return f'\"{self.text}\" ({str(self.author)}). Posted by \'{self.user}\'' 

	class Meta:
		ordering = ['created_date']



      