from django.apps import AppConfig
from keras.models import load_model


class ApiConfig(AppConfig):
    name = 'api'
    model = load_model('./api/saved_model/phone_price_classifier_model.h5')

