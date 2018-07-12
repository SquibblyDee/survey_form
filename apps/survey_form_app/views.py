from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    return render(request,'survey_form_app/index.html')

def result(request):
    return render(request,'survey_form_app/result.html')

def process(request, methods=['POST']):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['count']+=1
    print("NAME= ", request.session['name'])
    return redirect('/result')
