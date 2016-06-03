#!/usr/local/bin/python

def translate(text, src = '', to = 'en'):
  parameters = ({'langpair': '{0}|{1}'.format(src, to), 'v': '1.0' })
  translated = ''

  for text in (text[index:index + 4500] for index in range(0, len(text), 4500)):
    parameters['q'] = text
    response = json.loads(urllib.request.urlopen('http://ajax.googleapis.com/ajax/services/language/translate', data = urllib.parse.urlencode(parameters).encode('utf-8')).read().decode('utf-8'))

    try:
      translated += response['responseData']['translatedText']
    except:
      pass

  return translated
