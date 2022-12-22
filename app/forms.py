from django import forms
g=[('male','m'),('female','fm')]
c=[('PYTHON','python'),('DJANGO','django'),('SQL','sql')]
    
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)
    #course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    address=forms.CharField(widget=forms.TextInput)