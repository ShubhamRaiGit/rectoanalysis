from django.shortcuts import render
from django.views import generic
from .models import TwitterData
from forms import TrackerForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .utils import twitter
from tweepy import Cursor
import json

from tweepy import OAuthHandler
from tweepy import API

ckey = '2lLcB1zHTBFIksGCYhiP1tPur'
csecret = 'h8DlwdLrepqATIqbq2V7oLRkWxEBVS4ad9RlhdrPHe2ofCG0GJ'
atoken = '3014982345-DtL7wx9trlC7A4B8VQGxSulry1greYDoxKammLd'
asecret = 'CChdoQS4G9E6iZ0NsehCW91SaHDmemmwrGdJORRtcWVJx'


def get_twitter_auth():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return auth


def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client



# Create your views here.
@login_required
def index(request):
    context = {
        'page_title': "Home",
    }
    return render(request, 'base.html', context)


@login_required
def facebook(request):
    context = {
        'page_title': "Facebook",
    }
    return render(request, 'facebook.html', context)


@login_required
def twitter(request):
    tracker_form = TrackerForm(request.POST or None)
    list_of_trackers = TwitterData.objects.all(request.user)
    count = list_of_trackers.count()
    error = False
    if tracker_form.is_valid():
        instance = tracker_form.save(commit=False)
        instance.tracker_user = request.user
        instance.timestamp = now()
        error = instance.save_clean(username=request.user)

    context = {
        'page_title': "Twitter",
        'tracker_form': tracker_form,
        'list_of_trackers': list_of_trackers,
        'count': count,
        'error': error,
    }
    return render(request, 'twitter.html', context)


def tracker_view(request, tracking_num):
    qs = TwitterData.objects.filter(tracking_number__iexact=tracking_num)
    if qs.exists() and qs.count() == 1:
        tracker_obj = qs.first()
        print_text = []
        """twitter_client = get_twitter_client()

        for status in Cursor(twitter_client.home_timeline).items(10):
            print_text.append(status.text)"""
        context = {
            'page_title': "Analytics",
            "tracker_obj": tracker_obj,
            'print_text' : print_text,
        }
    else:
        raise Http404


    return render(request, 'tracker_view.html', context)
