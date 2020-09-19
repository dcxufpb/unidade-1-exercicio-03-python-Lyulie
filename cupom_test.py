import cupom;
from cupom import imprime_dados_loja

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_loja_completa():
    assert imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
    global nome_loja
    cupom.nome_loja = ""
    assert imprime_dados_loja() == '''O campo nome da loja é obrigatório'''
    cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    global logradouro
    cupom.logradouro = ""
    assert imprime_dados_loja() == '''O campo logradouro do endereço é obrigatório'''
    cupom.logradouro = "Av. Projetada Leste"

def test_numero_zero():
    global numero
    cupom.numero = 0
    assert imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
    cupom.numero = 500

def test_municipio_vazio():
    global municipio
    cupom.municipio = ""
    assert cupom.imprime_dados_loja() == '''O campo município do endereço é obrigatório'''
    cupom.municipio = "Campinas"

def test_estado_vazio():
    global estado
    cupom.estado = ""
    assert cupom.imprime_dados_loja() == '''O campo estado do endereço é obrigatório'''
    cupom.estado = "SP"

def test_cnpj_vazio():
    global cnpj
    cupom.cnpj = ""
    assert cupom.imprime_dados_loja() == '''O campo CNPJ da loja é obrigatório'''
    cupom.cnpj = "42.591.651/0797-34"

def test_ie_vazio():
    global inscricao_estadual
    cupom.inscricao_estadual = ""
    assert cupom.imprime_dados_loja() == '''O campo inscrição estadual da loja é obrigatório'''
    cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Aguas indaia"
    cupom.logradouro = "Av Joana Silveira"
    cupom.numero = 727
    cupom.complemento = "portal"
    cupom.bairro = "Bela Vista"
    cupom.municipio = "Campina Grande"
    cupom.estado = "PB"
    cupom.cep = "58038-000"
    cupom.telefone = "(83) 8888-7777"
    cupom.observacao = "Fonte sul"
    cupom.cnpj = "11.111.222/3333-44"
    cupom.inscricao_estadual = "111.222.333.444"

    #E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == \
'''Aguas indaia
Av Joana Silveira, 727 portal
Bela Vista - Campina Grande - PB
CEP:58038-000 Tel (83) 8888-7777
Fonte sul
CNPJ: 11.111.222/3333-44
IE: 111.222.333.444
'''
