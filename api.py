from piplapis.search import SearchAPIRequest
request = SearchAPIRequest(first_name=u'Yuki', last_name=u'Falcon')
response = request.send()
print response
