#import urlparse

def application(env, start_response):
  url=env['QUERY_STRING']
#  print('uRL ',url)
  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [url.replace('&','\n')]

