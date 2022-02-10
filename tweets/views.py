from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.response import Response
from rest_framework.decorators import api_view

from tweets.serializers import TweetSerializer

from .forms import TweetForm
from .models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
	# print(args, kwargs)
	return render(request, "pages/home.html", context={}, status=200)


@api_view(['POST']) # http method the cloent === POST
def tweet_create_view(request, *args, **kwargs):
	serializer = TweetSerializer(data=request.POST)
	if serializer.is_valid(raise_exception=True): #send back what error is happen
		serializer.save(user=request.user)
		return Response(serializer.data, status=201) #.data contains dict representation of obj (Tweet)
	return Response({}, status=400)



@api_view(['GET']) # http method the cloent === GET
def tweet_list_view(request, *args, **kwargs):
	qs = Tweet.objects.all()
	serializer = TweetSerializer(qs, many=True)
	return Response(serializer.data)


def tweet_create_view_pure_django(request, *args, **kwargs):
	user = request.user
	if not request.user.is_authenticated:
		user = None
		if request.is_ajax():
			return JsonResponse({}, status=401) #Unauthorized
		return redirect(settings.LOGIN_URL)
	form = TweetForm(request.POST or None)
	next_url = request.POST.get("next") or None
	if form.is_valid():
		obj = form.save(commit=False)#it is a tweet object
		obj.user = user
		obj.save()
		if request.is_ajax():
			return JsonResponse(obj.serialize(), status=201) #we dont need redirect anymore, js reload page by himself
		if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
			return redirect(next_url)
		form = TweetForm()
	if form.errors:
		if request.is_ajax():
			return JsonResponse(form.errors, status=400) #response with error generated in TweetForm class
	return render(request, 'components/forms.html', context={"form": form})


def tweet_list_view_pure_django(request, *args, **kwargs):
	"""
	REST API VIEW
	Consume by JS and more
	return json data
	"""
	qs = Tweet.objects.all()
	tweets_list = [x.serialize() for x in qs]
	data = {
		"isUser": False,
		"response": tweets_list,
	}
	return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
	"""
	REST API VIEW
	Consume by JS and more
	return json data
	"""
	data = {
		"id":tweet_id,
		# "image_path": obj.image.url
	}
	status = 200
	try:
		obj = Tweet.objects.get(id=tweet_id)
		data["content"] = obj.content
	except:
		data['message'] = "Not found"
		status = 404
	return JsonResponse(data, status=status)


# Create your views here.
