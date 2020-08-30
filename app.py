from flask import Flask
from flask_restful import Resource, Api
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
api = Api(app)

URL_CHROME = 'https://chrome.google.com/webstore/detail/where-to/kdhcodpjaffhbbphkahnkbllddjihima'
URL_FIREFOX = 'https://addons.mozilla.org/en-US/firefox/addon/where-to/'

COLOR_OK = 'brightgreen'
COLOR_BAD = 'red'
COLOR_WARN = 'yellow'

def initResponse(label, message = 'available', color = COLOR_OK):
  response = {
    'schemaVersion': 1,
    'label': label,
    'message': message,
    'color': color
  }
  return response

class Chrome(Resource):
  def get(self):
    html = requests.get(URL_CHROME)
    if html.status_code != 200:
      res = initResponse('chrome', 'unavailable', COLOR_BAD)
      return res, 200
    soup = BeautifulSoup(html.text, 'html.parser')
    elements = soup.select('.C-b-p-D-J .C-b-p-D-Xe.h-C-b-p-D-md')
    if len(elements) != 1:
      res = initResponse('chrome', 'unknown ver', COLOR_WARN)
      return res, 200
    version = elements[0].decode_contents()
    res = initResponse('chrome', version)
    return res, 200

class Firefox(Resource):
  def get(self):
    html = requests.get(URL_FIREFOX)
    if html.status_code != 200:
      res = initResponse('firefox', 'unavailable', COLOR_BAD)
      return res, 200
    soup = BeautifulSoup(html.text, 'html.parser')
    elements = soup.select('.DefinitionList .Definition-dd.AddonMoreInfo-version')
    if len(elements) != 1:
      res = initResponse('firefox', 'unknown ver', COLOR_WARN)
      return res, 200
    version = elements[0].decode_contents()
    res = initResponse('firefox', version)
    return res, 200

class Safari(Resource):
  def get(self):
    res = initResponse('safari', 'unavailable', COLOR_BAD)
    return res, 200

class Edge(Resource):
  def get(self):
    res = initResponse('edge', 'unavailable', COLOR_BAD)
    return res, 200

class Ping(Resource):
  def get(self):
    return {'message': 'up'}, 200

class NotFound(Resource):
  def get(self, content):
    return {'message': 'The requested resource does not exist.'}, 404

api.add_resource(Chrome, '/chrome')
api.add_resource(Firefox, '/firefox')
api.add_resource(Safari, '/safari')
api.add_resource(Edge, '/edge')
api.add_resource(Ping, '/')
api.add_resource(NotFound, '/<path:content>')

if __name__ == '__main__':
  app.run(host='localhost', port=8080)
