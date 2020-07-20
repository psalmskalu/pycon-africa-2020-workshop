
from sklearn.preprocessing import StandardScaler
#from keras.models import load_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
from .apps import ApiConfig

# Create your views here.

@api_view(["POST"])
def predict(request):
    try:
        battery_power = request.data.get('battery_power',None)
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
        bluetooth = request.data.get('bluetooth',0)
        dual_sim = request.data.get('dual_sim',0)
        four_g = request.data.get('four_g',0)
        three_g = request.data.get('three_g',0)
        touch_screen = request.data.get('touch_screen',0)
        wifi = request.data.get('wifi',0)
        
        features = [battery_power, clock_speed,front_camera, internal_memory, mobile_depth, 
                    weight, n_cores, primary_camera, pixel_height, pixel_width, ram_size,
                    screen_height, screen_width, talk_time, bluetooth, dual_sim, four_g,
                    three_g, touch_screen, wifi,
            ]
        
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
            bluetooth = int(bool(bluetooth))
            dual_sim = int(bool(dual_sim))
            four_g = int(bool(four_g))
            three_g = int(bool(three_g))
            touch_screen = int(bool(touch_screen))
            wifi = int(bool(wifi))

            cleaned_features = [battery_power, clock_speed,front_camera, internal_memory, mobile_depth, 
                    weight, n_cores, primary_camera, pixel_height, pixel_width, ram_size,
                    screen_height, screen_width, talk_time, bluetooth, dual_sim, four_g,
                    three_g, touch_screen, wifi,
            ]

            print(cleaned_features)

            #perform standard scaling of feature to get
            scaler = StandardScaler()
            X = scaler.fit_transform([cleaned_features])

        
            #bring in pre-loaded model                                   
            model = ApiConfig.model


            #Passing data to model & loading the model from disks
            prediction = model.predict([X])[0]

            #Convert prediction back to label
            prediction = np.argmax(prediction)                  
            
            
            predictions = {
                'status' : '0',
                'message' : 'Successful',
                'prediction' : prediction,                
            }

        else:
            predictions = {
                'status' : '1',
                'message': 'Invalid Parameters'                
            }

    except Exception as exception:
        predictions = {
            'status' : '2',
            "message": str(exception)
        }
    
    return Response(predictions)