
#This is created by kamran:

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')




def analyze(request):
    djtext = request.POST.get('text','off')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    # print(djtext)

    if (removepunc == 'on'):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove punctuation','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if (fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremove == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char

        params = {'purpose': 'Remove Extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == 'on'):
        count = 0
        for char in djtext:
            count+=1

        params = {'purpose': 'Remove Extra space', 'analyzed_text': count}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse('Error')

    if (removepunc != 'on' and fullcaps != 'on' and newlineremove != 'on' and extraspaceremover != 'on'
    and charcount != 'on'):
        return HttpResponse('Please select any operation and try again')

    return render(request, 'analyze.html', params)




