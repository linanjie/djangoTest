from django import forms


# 使用django的表单forms
class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
