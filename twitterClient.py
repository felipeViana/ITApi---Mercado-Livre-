#Python 3.x, for Python 2.7 Twitter Client: http://pastebin.com/peP6nrhf
import urllib.request
import json

f = open("resultado.txt", "w")

class categoria:
  numero_vendas=0
  iden=0
  name=''
  subclasses=[]

  def printa():
    print(str(id) + ' ' + name)
    for i in self.subclasses:
      printa(i)
  
def busca_coisas(texto='python'):
  url = 'https://api.mercadolibre.com/sites/MLB/search/.json?q=' + texto
  resp = urllib.request.urlopen(url).read()
  data = json.loads(resp.decode('utf-8'))
  
  
 
def print_result(result):
  for t in result:
    f.write(str(t)+'\n')
 
resultados = busca_coisas()
print_result(resultados)

f.close()
