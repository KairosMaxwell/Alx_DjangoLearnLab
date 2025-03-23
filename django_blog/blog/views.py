from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy


# Create your views here.


class SignUpView(CreateView):

    def register(request):
        pass
    #     if request.method == 'POST':
    #         form = UserCreationForm(request.POST)
    #         if form.is_valid():
    #             user = form.save()
    #             login(request, user)
    #             return redirect('profile')
    #     else:
    #         form = UserCreationForm()
    #     return render(request, 'registration/register.html', {'form': form})
    #
    # @login_required
    # def profile(request):
    #     return render(request, 'registration/profile.html')

form_class = UserCreationForm
success_url = reverse_lazy('login')
template_name = ""

