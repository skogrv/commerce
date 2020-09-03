from django import forms
from .models import Auction


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('image', 'price', 'name', 'description',)

        widgets = {
            'image': forms.FileInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
