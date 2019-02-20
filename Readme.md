[![Build Status](https://travis-ci.org/DyegoMaas/weather-forecast.svg?branch=master)](https://travis-ci.org/DyegoMaas/weather-forecast)

# Previsão do Tempo

A aplicação permite consultar a previsão de tempo em cidades brasileiras, utilizando o [Open Weather Map API](https://openweathermap.org/api).

## Instalação

A aplicação requer o *Python 3.7* instalado no PATH.

A instalação dos pacotes de dependências da aplicação é feita com a ferramenta `pipenv`, responsável por instalar os pacotes no escopo do projeto. Se você não tem o `pipenv` instalado, basta rodar o comando `pip install pipenv`.

Em seguida rode o comando `pipenv install`.

## Rodando a aplicação

### Backend - Flask

Para rodar a aplicação, navegue até a raiz no console e rode o comando `pipenv shell` para ativar o *virtual environment*. Em seguida rode o comando `python main.py`.

A aplicação vai subir um servidor web auto-hospedado, rodando na **porta 8003**. Caso for necessário trocar a porta, é possível fazê-lo na última linha do arquivo `main.py`.

### Frontend - SPA com Vue.js

Para rodar a aplicação de frontend será necessário ter instalado o NodeJS 8.0+. Navegue até a pasta `frontend` e rode os comandos `npm install` e `npm run start`.

A aplicação rodará em http://localhost:8080.

## Arquitetura

A aplicação utiliza uma arquitetura cliente servidor que se assemelha estruturalmente a uma aplicação empresarial simples, disponibilizando uma API REST para consumo pelo frontend.

O servidor web é feito com o microframework `Flask`, auto-hospedado, rodando na porta 8003, e que fornece tanto o conteúdo estático para a interface gráfica quanto os endpoints de consulta da API.

A injeção de dependência é feita com `inject` e `FlaskInject`.

Os testes unitários foram implementados utilizando a biblioteca `pytest`. Para a criação de mocks, foi utilizada a biblioteca `pymox`.

Como sugerido na especificação, foi implementado salvamento em arquivo. O formato escolhido foi o JSON Lines.

O frontend, por sua vez, é constituído por uma SPA (*Single Page Application*) implementada com VueJS.

### Integração Contínua

O pipeline de integração contínua está rodando no Travis CI, rodando os testes com a lib `pytest`.

## Descrição da API

A aplicação disponibiliza dois endpoints:

### GET http://localhost:8003/api/cities

Lista todas as cidades cadastradas e previamente consultadas. Retorna um array de strings.

### POST http://localhost:8003/api/forecast/{city_name}

Lista todas as cidades cadastradas e previamente consultadas.

Ao consultar a previsão do tempo para uma nova cidade, se a cidade existir no Open Weather API, a mesma ficará salva, e a previsão para os próximos 5 dias será retornada.

