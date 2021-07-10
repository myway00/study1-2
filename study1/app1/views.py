from django.shortcuts import render
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def result(request):
    text=request.GET['fulltext'] #home에서 fulltext라는 name의 친구도 가져온다
    words=text.split() #위에서 받아온 fulltext(text)를 쪼개준다
    
    word_dic={} #이 친구를 추가 처음엔 빈 리스트
    for x in words:
        if x in word_dic :
            word_dic[x]+=1
        else :
            word_dic[x]=1
    
    return render(request, "result.html",{ "total" : text, 'dic':word_dic.items()})
        #키(result에 가져다 줄 최종 별명) : 값(위의 GET에서 받아온 별명)