# I created this file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Deepanshu','place':'India'}
    return render(request, 'index.html', params)

def analyze(request):
    #Assign arguments
    txt=request.POST.get('text','default')
    rmpunc=request.POST.get('rmpunc','off')
    cap=request.POST.get('cap','off')
    nlrem=request.POST.get('nlrem','off')
    srem=request.POST.get('srem','off')
    ccount=request.POST.get('ccount','off')
    li=['','','','']

    if rmpunc=='on':
        final=rempunc(txt)
        txt=final
        li[0]='Remove Punctuations'

    if cap=='on':
        final = capfirst(txt)
        txt=final
        li[1]='Capitalize text'

    if nlrem=='on':
        final = newlineremove(txt)
        txt=final
        li[2]='New Line Remove'

    if srem=='on':
        final = spaceremove(txt)
        txt=final
        li[3]='Space Remover'

    if rmpunc=='on' or cap=='on' or nlrem=='on' or srem=='on':
        st=''
        for i in li:
            if i != '':
                st+=' '+i
        params = {'purpose': st, 'analyzed_txt': final}
        return render(request, 'analyze.html', params)
    elif ccount=='on':
        final = charcount(txt)
        params = {'purpose': 'Count Characters', 'analyzed_txt': final}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

def rempunc(txt):
    punc = '''~`!@#$%^&*()-_=+{[]};:'"\|,<.>/?'''
    final_txt = ''
    for char in txt:
        if char not in punc:
            final_txt += char
    return final_txt

def capfirst(txt):
    final_txt = txt.upper()
    return final_txt

def newlineremove(txt):
    final_txt = ''
    for char in txt:
        if char!='\n' and char!='\r':
            final_txt+=char
    return final_txt

def spaceremove(txt):
    final_txt = ''
    for index,char in enumerate(txt):
        if not(txt[index]==' ' and txt[index+1]==' '):
            final_txt+=char
    return final_txt

def charcount(txt):
    final_txt = 'The total count of the text: '+str(len(txt))
    return final_txt