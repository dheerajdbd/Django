from django.http import HttpResponse
from django.shortcuts import render
import operator

hit={'hithere':'sdfa'}

def demo(request):
	return render(request,'home.html',hit)

def count(request):
	fulltext = request.GET['fulltext']
	mywords = fulltext.split()
	mydict={}
	for word in mywords:
		if word in mydict:
			mydict[word] +=1
		else:
			mydict[word] = 1
	print(fulltext)
	sortedWords = sorted(mydict.items(),key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'fulltext':fulltext,'count_length':len(mywords),'worddictionary':sortedWords})

def about(request):
	print('indie about')
	return render(request,'about.html')