# from distutils.command.clean import clean
from django import forms
from .models import Mango
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try :
                mango = Mango.objects.get(username=username)
            except Mango.DoesNotExist:
                self.add_error('username', '아이디가 없습니다....ㅠ')
                return

            if not check_password(password, mango.password):
                self.add_error('password', '비밀번호가 틀렸습니다....ㅠ')

            else:
                self.user_id = mango.id