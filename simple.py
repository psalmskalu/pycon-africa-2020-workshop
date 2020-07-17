from sklearn.preprocessing import StandardScaler
from keras.models import load_model



class Predict:
    def __init__(self):
        self.list = None

    def receive_input(self, mylist):
        self.list = mylist

    def preprocess_input(self):
        scaler = StandardScaler()
        mylist = scaler.fit_transform(self.list)
        return mylist

    def make_prediction(self, mylist):
        model = load_model('./saved_model/phone_price_classifier_model.h5')
        result = model.predict(mylist)
        return result



    