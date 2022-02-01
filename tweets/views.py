from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Tweet


def home_view(request, *args, **kwargs):
	# print(args, kwargs)
	return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
	"""
	REST API VIEW
	Consume by JS and more
	return json data
	"""
	qs = Tweet.objects.all()
	tweets_list = [{"id": x.id, "content": x.content} for x in qs]
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
