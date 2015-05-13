# -*- coding: utf-8 -*-
from diretoria import *
from servico_postagem import *


class CartaoPostagem(object):
    def __init__(self, status, codigo_admin, numero):
        self.status = status
        self.numero = numero
        self.codigo_admin = codigo_admin

        # chave:codigo do servico
        self.servicos_postagem = {}

    def add_servico_postagem(self, codigo, nome, servico_id):
        self.servicos_postagem[codigo] = ServicoPostagem(int(codigo),
                                                         nome,
                                                         servico_id)


class Contrato(object):
    def __init__(self, codigo_diretoria, id_contrato):
        self.id_contrato = id_contrato
        self.diretoria = Diretoria(int(codigo_diretoria))

        # chave:numero do cartao de postagem
        self.cartoes_postagem = {}


class Cliente(object):
    
    def __init__(self, nome, cnpj, descricao_status_cliente):
        self.nome = nome
        self.cnpj = cnpj
        self.status = descricao_status_cliente

        # chave:id do contrato
        self.contratos = {}

    def get_contrato(self, id_contrato):
        return self.contratos[id_contrato]

    def get_cartao_postagem(self, id_contrato, numero_cartao):
        return self.contratos[id_contrato].cartoes_postagem[numero_cartao]

    def get_servico_postagem(self, id_contrato, numero_cartao,
                             codigo_servico):
        return self.contratos[id_contrato].cartoes_postagem[
            numero_cartao].servicos_postagem[codigo_servico]

    def get_lista_cartao_postagem(self, id_contrato):
        return self.contratos[id_contrato].cartoes_postagem

    def get_lista_servico_postagem(self, id_contrato, numero_cartao):
        return self.contratos[id_contrato].cartoes_postagem[
            numero_cartao].servicos_postagem



