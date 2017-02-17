from django import forms


class NewLectureForm(forms.Form):
    lecture_name = forms.CharField(max_length=80)
    week = forms.CharField(widget=forms.NumberInput)
    course_name = forms.CharField()
    lecture_url = forms.URLField(label='Enter link for details:')
