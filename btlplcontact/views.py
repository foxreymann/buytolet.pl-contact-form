from django.shortcuts import render, redirect

from django.contrib import messages

from btlplcontact.forms import ContactDataForm

def index(request):
  if request.method == "POST":
    form = ContactDataForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'VALID');
      return redirect('/')
    else:
      messages.error(request, 'NOT VALID');
  else:
    form = ContactDataForm()
  template_vars = {
    "form": form
  }
  return render(request, "index.html", template_vars)
