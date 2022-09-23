from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from syuapp.forms import FeedbackForm
from syuapp.models import Portfolio

msgIndex = "Hey guys! Check me out!";
msgPortfolio = "My most recent project:";
msgContactUs = "Halo Halo!";

def index(request):
    context = {'title':'Syu App!','text':msgIndex}
    return render(request, "base_content.html", context);

def portfolio(request):
    # get all records from Portfolio model
    porfolioData = Portfolio.objects.all().order_by('-id') # descending order by id
    context = {'title':'Portfolio','text':msgPortfolio,'data':porfolioData} 
    return render(request, "base_content.html", context);

def contact(request):
    context = {'title':'Contact Me', 'text':msgContactUs} # establish basic context
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just triggers the validation
            feedback = form.cleaned_data['feedback']
            send_mail('Feedback Form',
            feedback,
            settings.EMAIL_HOST_USER,
            [settings.ADMIN_EMAIL],
            fail_silently = False)
            form.save()
            form = FeedbackForm()
            context.update({'form':form.as_table, 'created':True}) # update basic context
            return render(request, "base_content.html", context);
        else:
            context.update({'form':form.as_table, 'notcreated':True}) # update basic context
            return render(request, "base_content.html", context);
    else:
        form = FeedbackForm()
    context.update({'form':form.as_table}) # update basic context
    return render(request, "base_content.html", context);