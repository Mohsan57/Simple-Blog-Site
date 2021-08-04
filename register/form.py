from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django import forms
from register.models import Register, User_Image, Articles
from ckeditor.widgets import CKEditorWidget


class DateInput(forms.DateInput):
    input_type = "date"


class user_image(forms.ModelForm):
    class Meta:
        model = User_Image
        fields = ["photo"]


class Article(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Articles
        fields = ['title', 'cover_photo', 'content','tag']


class Registration_form(forms.Form):
    user_name = forms.CharField(
        max_length=100)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    date_of_birth = forms.DateField(widget=DateInput)
    email = forms.EmailField()
    password = forms.CharField(
        max_length=200,  widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=200, widget=forms.PasswordInput)


'''
    def user_name_test(self):
        user = self.cleaned_data.get('user_name')
        ex = Register.objects.filter(user_name_iexact=user)
        if(ex.exists()):
            raise forms.ValidationError("This User Name already exist")
        return user
'''


class login_form(forms.Form):
    user_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
