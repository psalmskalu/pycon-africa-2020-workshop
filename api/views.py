
from sklearn.preprocessing import StandardScaler
#from keras import load_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np

# Create your views here.
@api_view(['GET'])
def index(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict(request):
    try:
        battery_power = request.data.get('clock_speed',None)
        clock_speed = request.data.get('clock_speed',None)
        front_camera = request.data.get('front_camera',None)
        internal_memory = request.data.get('internal_memory',None)
        mobile_depth = request.data.get('mobile_depth',None)
        weight = request.data.get('weight',None)
        n_cores = request.data.get('n_cores',None)
        primary_camera = request.data.get('primary_camera',None)
        pixel_height = request.data.get('pixel_height',None)
        pixel_width = request.data.get('pixel_width',None)
        ram_size = request.data.get('ram_size',None)
        screen_height = request.data.get('screen_height',None)
        screen_width = request.data.get('screen_width',None)
        talk_time = request.data.get('talk_time',None)
        bluetooth = request.data.get('bluetooth',None)
        dual_sim = request.data.get('dual_sim',None)
        four_g = request.data.get('four_g',None)
        three_g = request.data.get('three_g',None)
        touch_screen = request.data.get('touch_screen',None)
        wifi = request.data.get('wifi',None)
        
        features = [battery_power, clock_speed,front_camera, internal_memory, mobile_depth, 
                    weight, n_cores, primary_camera, pixel_height, pixel_width, ram_size,
                    screen_height, screen_width, talk_time, bluetooth, dual_sim, four_g,
                    three_g, touch_screen, wifi,
            ]

        print("Features", features)
        print()

        if not None in features:

            #Datapreprocessing Convert the values to float
            battery_power = int(battery_power)
            clock_speed = float(clock_speed)
            front_camera = int(front_camera)
            internal_memory = int(internal_memory)
            mobile_depth = float(mobile_depth)
            weight = int(weight)
            n_cores = int(n_cores)
            primary_camera = int(primary_camera)
            pixel_height = int(pixel_height)
            pixel_width = int(pixel_width)
            ram_size = int(ram_size)
            screen_height = int(screen_height)
            screen_width = int(screen_width)
            talk_time = int(talk_time)
            bluetooth = bool(bluetooth)
            dual_sim = bool(dual_sim)
            four_g = bool(four_g)
            three_g = bool(three_g)
            touch_screen = bool(touch_screen)
            wifi = bool(wifi)

            cleaned_features = [battery_power, clock_speed,front_camera, internal_memory, mobile_depth, 
                    weight, n_cores, primary_camera, pixel_height, pixel_width, ram_size,
                    screen_height, screen_width, talk_time, bluetooth, dual_sim, four_g,
                    three_g, touch_screen, wifi,
            ]

            print("Cleaned Features", cleaned_features)

            #perform standard scaling of feature to get
            scaler = StandardScaler()
            X = scaler.fit_transform([cleaned_features])

            print(X)

            #Passing data to model & loading the model from disks
            
            '''
            model = load_model('saved_model/phone_price_classifier_model.h5')
            model = None

            prediction = model.predict([X])[0]

            #Convert prediction back to label
            prediction = np.argmax(prediction)

            '''

            conf_score =  np.max(0.333)*100
            
            
            predictions = {
                'error' : '0',
                'message' : 'Successful',
                'prediction' : 2,
                'confidence_score' : conf_score
            }

        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }

    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)