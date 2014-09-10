from django.shortcuts import render
import urllib
import json

# IP DO WEBSERVICE
HOST = 'http://fcamaramichel.no-ip.info/'

def function():
  #### TESTE HOST
  # clientes = urllib.request.urlopen(HOST+'/WS_FastLine/cliente_teste/listar_Todos')
  # clientes = json.loads(clientes.read().decode('utf-8'))
  # clientes = clientes["clientesTest"]

  ##### TESTE LOCAL
  clientes = json.loads('{"clientesTest":[{"id_cliente": "1","nm_cliente": "Lucas Castejon Alves","numero_cel": "993353325","email": "lucascastejon@gmail.com","cep": "14403180"},{"id_cliente": "2","nm_cliente": "Michel Ribeiro","numero_cel": "991293942","email": "michelribeiro@gmail.com","cep": "14403440"},{"id_cliente": "3","nm_cliente": "Leandro Borgesss","numero_cel": "999294123","email": "leandro@borges.br","cep": "14403180"}] }')
  clientes = clientes["clientesTest"]
  return clientes

def home(request):
  clientes = function()
  return render(request,'index.html', {'clientes':clientes})

def cep(request, cep, id_cliente):

  # RECUPERANDO ENDEREÇO COM TIPO TXT
  cep         = urllib.request.urlopen('http://viacep.com.br/ws/'+cep+'/json/')
  endereco    = json.loads(cep.read().decode('utf-8')) # TRANSFORMANDO TXT EM JSON

  clientes    = function()
  cliente     = clientes[int(id_cliente) - 1] # RETORNA CLIENTE REFERENTE AO ID PASSADO

  logradouro  = endereco['logradouro']
  bairro      = endereco['bairro']
  localidade  = endereco['localidade']
  uf          = endereco['uf']
  ibge        = endereco['ibge']
  cep         = endereco['cep']

  return render(request,'cep.html', {'cliente':cliente['nm_cliente'], 'logradouro':logradouro, 'bairro':bairro, 'localidade':localidade, 'uf':uf, 'ibge':ibge, 'cep':cep})

def formulario(request, id_cliente):
  clientes   = function()
  cliente    = clientes[int(id_cliente) - 1] # id_cliente É O ID DO CLIENTE ENVIADO NA URL
  return render(request,'form.html', {'cliente':cliente})

def salvar_enviar(request):
  clientes   = function()

  # RECUPERANDO DADOS GET
  id_cliente = request.GET['id_cliente']
  nm_cliente = request.GET['nm_cliente']
  numero_cel = request.GET['numero_cel']
  email      = request.GET['email']
  cep        = request.GET['cep']

  cliente = clientes[int(id_cliente) - 1]

  # CONCATENANDO PARÂMETROS A SER ENVIADO VIA URL
  dados = id_cliente+'/'+nm_cliente.replace(" ","%20")+'/'+numero_cel.replace(" ","%20")+'/'+email+'/'+cep

  # save = urllib.request.urlopen(HOST+'WS_FastLine/produto/listarTodos/'+dados)

  return render(request,'form.html', {'nm_cliente':nm_cliente,'cliente':cliente})