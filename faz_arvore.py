#Python 3.x, for Python 2.7 Twitter Client: http://pastebin.com/peP6nrhf
import urllib.request
import json

f = open("resultado.txt", "w")

class categoria:
  def __init__(self):
    self.numero_vendas=0
    self.iden=0
    self.name=''
    
  def printa(self):
    f.write(str(self.iden) + ' ' + self.name + '\n')

lista=[]
c=categoria()
c.iden='MLB'
c.name='Brasil'
lista.append(c)

def bota(iden='MLB'):
  if iden=='MLB':
    url='https://api.mercadolibre.com/sites/MLB/.json'
  else:
    url='https://api.mercadolibre.com/categories/'+iden+'/.json'
  resp = urllib.request.urlopen(url).read()
  data = json.loads(resp.decode('utf-8'))

  if iden=='MLB':
    children='categories'
  else:
    children='children_categories'
  
  for i in range(len(data[children])):
    d=categoria()
    d.name=data[children][i]['name']
    d.iden=data[children][i]['id']
    lista.append(d)

def busca_coisas(texto='MLB'):
  bota(texto)

for i in lista:
  busca_coisas(i.iden)

for i in lista:
  i.printa()

f.close()
