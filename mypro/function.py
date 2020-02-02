from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    usr_text = request.GET['text']
    total_count = len(usr_text)

    word_dict = {}  ##字频统计
    for word in usr_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_list=\
    sorted(word_dict.items(), key=lambda w:w[1], reverse=True)

    return render(request, 'count.html', {'count': total_count, 'text': usr_text,
                                          'wordict':word_dict, 'sorted': sorted_list})
