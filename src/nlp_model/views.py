from django.shortcuts import render, HttpResponse, Http404
from joblib import load
from nlp_model.forms import Tweet

tfidf_vectorizer = load("C:/Users/lotar/Desktop/projets/00.django_projects/django_nlp/src/"
                        "saved_models/tfidf_vectorizer.joblib")
tfidf_svc = load("C:/Users/lotar/Desktop/projets/00.django_projects/django_nlp/src/saved_models/tfidf_svc.joblib")


def index(request):
    tweet = Tweet()
    if request.method == "POST":
        if tweet.is_valid():
            tweet.save()
    return render(request, "index.html", {"form": tweet})


def result(request):
    tweet = request.GET.get("tweet", "")
    tweet_vectorized = tfidf_vectorizer.transform([tweet])
    tweet_pred = tfidf_svc.predict(tweet_vectorized)
    if tweet_pred == ['Donald J. Trump']:
        tweet_pred = "L'auteur de ce tweet est Donald J. Trump."
    else:
        tweet_pred = "L'auteur de ce tweet est Justin Trudeau."

    return render(request, "result.html", {'tweet_analyzed': tweet_pred})
