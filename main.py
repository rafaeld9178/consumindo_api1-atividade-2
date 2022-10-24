import requests, json

digite_cep = input("Digite o CEP: ")
request = requests.get("https://viacep.com.br/ws/{0}/json:", digite_cep)
data = json.loads(request.content)

endereco = data['logradouro']
bairro = data['bairro']
uf = data['uf']
cep = data['cep']

print(endereco, bairro, uf, cep)