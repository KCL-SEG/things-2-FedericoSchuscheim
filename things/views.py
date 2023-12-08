from django.urls import reverse
from things.forms import ThingForm
from django.views.generic import FormView

class HomeView(FormView):
    form_class = ThingForm
    template_name = 'home.html'
    
    def form_valid(self, form: ThingForm):
        """Handle valid form by saving the new thing."""
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Return redirect URL after successful team creation."""
        return reverse('home')
