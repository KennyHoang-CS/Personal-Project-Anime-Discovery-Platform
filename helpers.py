import requests
BASE_PATH = "https://kitsu.io/api/edge"

def processResponse(response, flag):
    """ sadsa """
    
    myList = []

    if flag == 'trending': 
        for i in range(0, 16):
            myList.append((
            response['data'][i]['id'],
            response['data'][i]['attributes']['canonicalTitle'],
            response['data'][i]['attributes']['synopsis'],
            response['data'][i]['attributes']['coverImage']['original'],
            response['data'][i]['attributes']['averageRating'],
            response['data'][i]['attributes']['ageRatingGuide']
            ))
    else: 
        for i in range(0, len(response)):
            myList.append((
            response['data'][i]['id'],
            response['data'][i]['attributes']['canonicalTitle'],
            response['data'][i]['attributes']['synopsis'],
            response['data'][i]['attributes']['coverImage']['original'],
            response['data'][i]['attributes']['averageRating'],
            response['data'][i]['attributes']['ageRatingGuide']
            ))

    return myList
        
    

def handleResponse2(user_list):
    """ Get the anime data for user's list from external API. """
    user_list = list(user_list)
    myList = []
    for i in range(0, len(user_list)):
        response = requests.get(f'{BASE_PATH}/anime/{user_list[i].anime_id}')
        response = response.json()
        myList.append((
            response['data']['id'],
            response['data']['attributes']['canonicalTitle'],
            response['data']['attributes']['synopsis'],
            response['data']['attributes']['coverImage']['original'],
            response['data']['attributes']['averageRating'],
            response['data']['attributes']['ageRatingGuide']
            ))
    return myList