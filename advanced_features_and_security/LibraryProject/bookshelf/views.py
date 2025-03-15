from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('app_name.can_view', raise_exception=True)
def view_instance(request, pk):
    # Logic for viewing an instance
    return render(request, 'view_instance.html')

@permission_required('app_name.can_edit', raise_exception=True)
def edit_instance(request, pk):
    # Logic for editing an instance
    return render(request, 'edit_instance.html')
