import urllib.request,json
from .models import Source
from .models import Article

# Getting api key
apiKey = None
# Getting the Category url
sources_url = None
#Getting the Article url
everything_url = None
#Search url
search_url = None



def configure_request(app):
    global apiKey,everything_url,search_url,sources_url
    apiKey = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    everything_url=app.config['EVERYTHING_BASE_URL']
    search_url=app.config["SEARCH_API_BASE_URL"]

# def get_newsource(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_newsource_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=21b011f88eac4c0a8afec44dda193304'.format(category)

#     with urllib.request.urlopen(get_newsource_url) as url:
#         get_newsource_data = url.read()
#         get_newsource_response = json.loads(get_newsource_data)


#         newsource_results = None

#         if get_newsource_response['sources']:
#             newsource_results_list = get_newsource_response['sources']
#             newsource_results = process_results(newsource_results_list)

#     return newsource_results
