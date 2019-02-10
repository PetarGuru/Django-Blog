from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def email_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Subject - blog'
            message = 'The Mail is from {}... The Message is {} .. Email is {}'.format(cd['name'], cd['message'],
                                                                                       cd['email'])
            email = '{}'.format(cd['email'])
            try:
                send_mail(subject, message, email, ['petarmulaj@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact/email.html", {'form': form})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')