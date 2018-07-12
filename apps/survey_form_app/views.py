from django.shortcuts import render, redirect

# Index creates a session key for count if it doesn't already exist.
def index(request, methods=['POST']):
    if 'count' not in request.session:
        request.session['count']=0
    return render(request,'survey_form_app/index.html')

# Request only renders our result page and is called by the process function.
def result(request):
    return render(request,'survey_form_app/result.html')

# Assigns our post data to session keys and increments the count by 1 before redirecting to result.html
def process(request, methods=['POST']):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['count']+=1
    return redirect('/result')
