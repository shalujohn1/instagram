from users.models import Profile
from instaprojects.models import Post
from django.db.models import Q

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    post = Post.objects.distinct().filter(
        Q(description__icontains=search_query)
    )

    profile = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
    )
    print(search_query)
    print(profile)
    return profile, post, search_query