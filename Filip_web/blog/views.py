from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Filip',
		'title' : 'můj nadpis',
		'content' : 'můj obsah',
		'post_date' : '7.9.2019'
	},
	{
		'author': 'Nela',
		'title' : 'Nela nadpis',
		'content' : 'Nelin obsah',
		'post_date' : '18.6.2017'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context) 

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})