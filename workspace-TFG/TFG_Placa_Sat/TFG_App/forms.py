from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# -*- coding: utf-8 -*-


class TCnew(forms.Form):
    type =  (('Change Sampling Period','Change Sampling Period'),
             ('Change Baud Rate','Change Baud Rate'),
             )
    tc_type     = forms.ChoiceField(choices=type, label="Tipo de telecomando")
    
    
#TCChangeMode es el formulario con los parametros propios del telecomando ChangeMode  
class TCChangeBaudRate(forms.Form):
    radio = (('14400', '14400'),
           ('19200', '19200'),
           ('38400', '38400'),
           ('57600', '57600'),
           ('115200', '115200'),
           ('230400', '230400'),)
    new_baudrate = forms.ChoiceField(choices=radio, label="Baud Rate")
    
#TCChangeSamplingPeriod es el formulario con los parametros propios del telecomando ChangeSamplingPeriod
class TCChangeSamplingPeriod(forms.Form):
    #signals_to_change_period
    signals =  (('TEMPERATURE','TEMPERATURE'),
             ('OTHER','OTHER'),)
    signals_to_change_period = forms.ChoiceField(choices=signals, label="Signal")
    new_period = forms.IntegerField(label='Period (s)', initial='10', min_value=10)


    