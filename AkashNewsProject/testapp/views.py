from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movie_news_view(request):
        news1 = 'In Hindi EndGame is not good'
        news2 = 'Salman Updating Minimum 100 carors Gurantee for his movies'
        news3 = 'Sonali slowly getting Curing'
        news4 = 'Amintabh Bachchan next movie is Thugs of hindustan'
        news5 = 'Salman and Catreena going to marry soon.'
        my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
        return render(request,'testapp/mnews.html',my_dict)

def sports_news_view(request):
        news1 = 'In Hindi EndGame is not good'
        news2 = 'Salman Updating Minimum 100 carors Gurantee for his movies'
        news3 = 'Sonali slowly getting Curing'
        news4 = 'Amintabh Bachchan next movie is Thugs of hindustan'
        news5 = 'Salman and Catreena going to marry soon.'
        my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
        return render(request,'testapp/snews.html',my_dict)

def politics_news_view(request):
        news1 = 'In Hindi EndGame is not good'
        news2 = 'Salman Updating Minimum 100 carors Gurantee for his movies'
        news3 = 'Sonali slowly getting Curing'
        news4 = 'Amintabh Bachchan next movie is Thugs of hindustan'
        news5 = 'Salman and Catreena going to marry soon.'
        my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
        return render(request,'testapp/pnews.html',my_dict)

def spicy_news_view(request):
        news1 = 'In Hindi EndGame is not good'
        news2 = 'Salman Updating Minimum 100 carors Gurantee for his movies'
        news3 = 'Sonali slowly getting Curing'
        news4 = 'Amintabh Bachchan next movie is Thugs of hindustan'
        news5 = 'Salman and Catreena going to marry soon.'
        my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
        return render(request,'testapp/spnews.html',my_dict)
