from django.shortcuts import render

from django.shortcuts import render

def base_view(request):
    return render(request, 'base.html')  # Ensure you have a `base.html` template.


def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')  # Login page

def signup_view(request):
    return render(request, 'signup.html')  # Signup page; create this template if needed

def contactus_view(request):
    return render(request, 'contactus.html')  # Contact us page

def getstarted_view(request):
    return render(request, 'getstarted.html')  # Getting started page

def german_view(request):
    return render(request, 'german.html')  # German language page

def french_view(request):
    return render(request, 'french.html')  # French language page

def english_view(request):
    return render(request, 'english.html')  # English language page

def spanish_view(request):
    return render(request, 'spanish.html')  # Spanish language page

def italian_view(request):
    return render(request, 'italian.html')  # Italian language page

def working_view(request):
    return render(request, 'working.html')  # Working page

def chatbot_view(request):
    return render(request, 'chatbot.html')  # Chatbot page

def ga_quiz(request):
    return render(request, 'gaquiz.html')  # A1: Beginner Quiz page

def gb_quiz(request):
    return render(request, 'gbquiz.html')  # A2: Beginner Quiz page

def gc(request):
    return render(request, 'gc.html')  # A1: Intermediate Quiz page

def gd(request):
    return render(request, 'gd.html')  # A2: Intermediate Quiz page

def fa(request):
    return render(request, 'fa.html')  # French A1 Quiz page

def fb(request):
    return render(request, 'fb.html')  # French A2 Quiz page
def fc(request):
    return render(request, 'fc.html')
def fd(request):
    return render(request, 'fd.html')
def sa(request):
    return render(request, 'sa.html')

def sb(request):
    return render(request, 'sb.html')
def sc(request):
    return render(request, 'sc.html')
def sd(request):
    return render(request, 'sd.html')
def ia(request):
    return render(request, 'ia.html')

def ib(request):
    return render(request, 'ib.html')
def ic(request):
    return render(request, 'ic.html')
def id(request):
    return render(request, 'id.html')
def ea(request):
    return render(request, 'ea.html')

def eb(request):
    return render(request, 'eb.html')
def ec(request):
    return render(request, 'ec.html')
def ed(request):
    return render(request, 'ed.html')
