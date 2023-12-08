"""Forms of the project."""

# Create your forms here.
from django.forms import ModelForm, Textarea
from .models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': Textarea()}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self):
        super().save(commit=False)
        thingObject = Thing.objects.create(
            name=self.cleaned_data.get('name'),
            description=self.cleaned_data.get('description'),
            quantity = self.cleaned_data.get('quantity'),
        )
        return thingObject
