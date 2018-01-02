from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)  # Valid email is mandatory

    class Meta:  # Description of the form
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):  # Saves the data to the data base
        user = super(RegistrationForm, self ).save(commit=False)
        user.email = self.cleaned_data['email']  # Checks for code that can harm the site in the input box

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:  # Description of the form
        model = User
        fields = (
            'username',
            'email',
        )


class CourseForm1(forms.ModelForm):
    answer_1_1 = forms.CharField()
    answer_1_2 = forms.IntegerField()
    answer_1_3 = forms.CharField()
    answer_1_4 = forms.IntegerField()

    class Meta:
        model = UserProfile
        fields = ('answer_1_1','answer_1_2', 'answer_1_3', 'answer_1_4', )


class CourseForm2(forms.ModelForm):
    answer_2_1 = forms.CharField()
    answer_2_2 = forms.CharField()
    answer_2_3 = forms.IntegerField()
    answer_2_4 = forms.CharField()
    answer_2_5 = forms.CharField()


    class Meta:
        model = UserProfile
        fields = ('answer_2_1','answer_2_2', 'answer_2_3', 'answer_2_4', 'answer_2_5', )


class CourseForm3(forms.ModelForm):
    answer_3_1 = forms.CharField()
    answer_3_2 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('answer_3_1','answer_3_2', )


class CourseForm4(forms.ModelForm):
    answer_4_1 = forms.IntegerField()
    answer_4_2 = forms.CharField()
    answer_4_3 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('answer_4_1', 'answer_4_2', 'answer_4_3', )


class CourseForm5(forms.ModelForm):
    answer_5_1 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('answer_5_1', )


class CourseForm6(forms.ModelForm):
    answer_6_1 = forms.CharField()
    answer_6_2 = forms.CharField()
    answer_6_3 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ('answer_6_1','answer_6_2','answer_6_3',  )


class CourseForm7(forms.ModelForm):
    answer_7_1 = forms.CharField()
    answer_7_2 = forms.IntegerField()

    class Meta:
        model = UserProfile
        fields = ('answer_7_1','answer_7_2',)


