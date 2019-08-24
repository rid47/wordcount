from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,"home.html")


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    print(wordlist)

    worddict = {}
    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word] += 1
        else:
            #add to dict
            worddict[word] = 1
    print(worddict)
    print(worddict.items())
    sortedwords= sorted(worddict.items(),key = operator.itemgetter(1),reverse = True)
    print(sortedwords)

    # print(fulltext)
    return render(request,'count.html',{'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})


def about(request):
    # return HttpResponse("hello from about page")
    return render(request, "about.html")