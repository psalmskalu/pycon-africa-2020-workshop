from django import forms 


class PhoneForm(forms.Form):
    
    battery_power = forms.IntegerField(label="Battery Power: What is the battery power of your phone (in mAh)?")
    clock_speed = forms.FloatField(label="Clock Speed: What is the processor speed of your phone?")    
    front_camera = forms.IntegerField(label="Front Camera: What is the megapixel value of the front camera?")    
    internal_memory = forms.IntegerField(label="Internal Memory: What is the size of the internal memory (in GB)?")
    mobile_depth = forms.IntegerField(label="Mobile Depth: What is the mobile depth (in cm)")
    weight = forms.IntegerField(label="Weight: How much does your phone weigh?")
    n_cores = forms.IntegerField(label="Cores: How many cores has your phone?")
    primary_camera = forms.IntegerField(label="Back Camera: What is the megapixel value of the back camera?")
    pixel_height = forms.IntegerField(label="Pixel Height: What is the pixel resolution height?")
    pixel_width = forms.IntegerField(label="Pixel Width: What is the pixel resolution width?")
    ram_size = forms.IntegerField(label="RAM Size: What is the size of the RAM (in MB)")
    screen_height = forms.IntegerField(label="Screen Height: What is the screen height?")
    screen_width = forms.IntegerField(label="Screen Width: What is the screen width?")
    talk_time = forms.IntegerField(label="Talk Time: How long does your phone battery last after charge (in hours)")
    bluetooth = forms.BooleanField(label="Bluetooth: Does your phone have bluetooth?")
    dual_sim = forms.BooleanField(label="Dual SIM: Does your phone have dual SIM?")
    four_g = forms.BooleanField(label="4G: Does your phone have 4G?")
    three_g = forms.BooleanField(label="3G: Does your phone have 3G")
    touch_screen = forms.BooleanField(label="Touch Screen: Does your phone have touch screen?")
    wifi = forms.BooleanField(label="WIFI: Does your phone have WIFI?")

    

    
    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        self.fields['battery_power'].widget.attrs.update({'class' : 'form-control'})
        self.fields['bluetooth'].widget.attrs.update({'class' : 'form-control'})
        self.fields['clock_speed'].widget.attrs.update({'class' : 'form-control'})
        self.fields['dual_sim'].widget.attrs.update({'class' : 'form-control'})
        self.fields['front_camera'].widget.attrs.update({'class' : 'form-control'})
        self.fields['four_g'].widget.attrs.update({'class' : 'form-control'})
        self.fields['internal_memory'].widget.attrs.update({'class' : 'form-control'})
        self.fields['mobile_depth'].widget.attrs.update({'class' : 'form-control'})
        self.fields['weight'].widget.attrs.update({'class' : 'form-control'})
        self.fields['n_cores'].widget.attrs.update({'class' : 'form-control'})
        self.fields['primary_camera'].widget.attrs.update({'class' : 'form-control'})
        self.fields['pixel_height'].widget.attrs.update({'class' : 'form-control'})
        self.fields['pixel_width'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ram_size'].widget.attrs.update({'class' : 'form-control'})
        self.fields['screen_height'].widget.attrs.update({'class' : 'form-control'})
        self.fields['screen_width'].widget.attrs.update({'class' : 'form-control'})
        self.fields['talk_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['three_g'].widget.attrs.update({'class' : 'form-control'})
        self.fields['touch_screen'].widget.attrs.update({'class' : 'form-control'})
        self.fields['wifi'].widget.attrs.update({'class' : 'form-control'})
        



