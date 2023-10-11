from users.models import Profile
from django.db.models import Q

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
    )
    print(search_query)
    print(profiles)
    return profiles, search_query