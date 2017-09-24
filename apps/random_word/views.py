from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
	# if not 'rand_word' in session:
	print request.session['rand_word']
	return render(request, "random_word/index.html")

def generate(request):
	if request.method == "POST": 
		request.session['rand_word'] = get_random_string(length=14)
		return redirect('/')
	else:
		return redirect('/')