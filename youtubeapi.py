## This code is modified from https://developers.google.com/youtube/v3/docs/search/list. 

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def videos_list_by_id(video_id, youtube):
  
  # youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  video_response = youtube.videos().list(
        id=video_id,
        part='snippet, contentDetails, statistics'
  ).execute()
  return video_response['items'][0]



def youtube_search(options):

	matching = 0
	# open file
	f = open(options.q+'_id.txt', 'w')

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
	developerKey=DEVELOPER_KEY)

	# Call the search.list method to retrieve results matching the specified
	# query term.
	search_response = youtube.search().list(
		q=options.q,
		part="id,snippet",
		maxResults=options.max_results
	).execute()
	proj=options.projection

	# Write each valid result to id file
	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
		  	if proj == "360":
				video_res = videos_list_by_id(search_result["id"]["videoId"], youtube)
				
				if video_res["contentDetails"]["projection"] == "360":	
					f.write(search_result["id"]["videoId"] + '\n')
					matching += 1
			else:
				f.write(search_result["id"]["videoId"] + '\n')
				matching += 1

	return matching
	  

if __name__ == "__main__":
	argparser.add_argument("--q", help="Search term", default="baseball")
	argparser.add_argument("--max-results", help="Max results", default=50)
	argparser.add_argument("--projection", help = "Search 360 video or rectangular", default="360")

	args = argparser.parse_args()
	
	try:
		matching = youtube_search(args)
		print "find %d matching result, try another keyword if you want more results" % (matching)
	except HttpError, e:
		print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

	
