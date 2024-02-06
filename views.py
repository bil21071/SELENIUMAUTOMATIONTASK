from django.shortcuts import render, redirect
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
    else:
        form = MyForm()

    return render(request, 'myapp/my_template.html', {'form': form})
# myapp/views.py
from django.shortcuts import render, redirect



def success_view(request):
    # Logic for rendering the success page
    return render(request, 'myapp/success_template.html')
