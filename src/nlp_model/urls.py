from django.urls import path
from .views import index, result


app_name = "nlp-model"

urlpatterns = [
    path('', index, name="index"),
    path('result', result, name="result")
 ]