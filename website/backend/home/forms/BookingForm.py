from django import forms

from ..models.booking_form import BookingForm


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = "__all__"
        # fields = ('title', 'text',)


class BookingFormForm(forms.Form):
    arrival_date = forms.DateField(label="Дата заезда")
    departure_date = forms.DateField(label="Дата выезда")
    adults = forms.IntegerField(label="Взрослые")
    children = forms.IntegerField(label="Дети")
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="комменте")
    email = forms.EmailField(label="Email")
