from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Function to check if the user is an Admin
def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

# Admin view restricted to Admin role
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin view! Only Admin users can access this.")
