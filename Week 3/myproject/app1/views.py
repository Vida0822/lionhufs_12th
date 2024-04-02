from django.shortcuts import render #render 모듈을 사용

# Create your views here.
def index(request):
    # 단순 렌더링(페이지만 띄운다) # 
    return render(request, "index.html")  # index.html 렌더링

def about(request):
    return render(request, "about.html") 

def count(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1 
        else:
            word_dictionary[word] = 1 

    return render(request, 'count.html',{'alltext': entered_text, 'total': len(word_list),'dictionary': word_dictionary.items()})
