`Desafio StoneCo`

`Desafio para vaga de desenvolvedor júnior`
------------------------------

##### `Objetivo`
Desenvolver uma API de integração com o GitHub utilizando Python ou Go.

##### `USO`
A Aplicação utiliza docker para facilitar a compilação do ambiente de desenvolvimento em qualquer máquina. Para rodar o projeto basta buildar a imagem e rodar o container dentro do diretório.

```docker
docker-compose build
&
docker-compose up
`````

O serviço rodará em:
````
http://localhost:5000/api/v1/
````
Para começar, acesse http://localhost:5000/api/v1/authenticate para permitir acesso á rotas especiais.
Feito isso, para consumir o serviço, pode ser usado o programa Postman, Insomnia ou até mesmo o swagger na rota /docs .

##### ```ENDPOINTS```

```
A documentação pode ser encontrada em http://localhost:5000/docs
```


##### ```Tests```
Para rodar os tests, basta acessar a pasta raiz com seu CLI de preferência e rodar
```
python -m unittest
`````

##### ``A Aplicação``
Para criar a aplicação me baseei em projetos que já fiz em outras linguagens e ambientes, organizar o projeto com um controller, uma classe de serviço e um Util, me ajudou a deixar o código mais organizado e legível.

O Docker-compose cria uma imagem pronta do Python com a distribuição Alpine do Linux presente no DockerHub, e uma imagem do Redis.


<small>Estrutura de pastas v2.0:</small>
````````
/
|   .gitignore
|   .dockerignore
|   Dockerfile
|   docker-compose
|   requirements.txt
|   README.MD
|   
\---src
    |   
    \---app
        |
        |   app.py
        |   
        \---main        
        |   |   
        |   |
        |   \---controllers
        |   |   |---github_authentication.py
        |   |   |---github_integration.py
        |   |          
        |   \---services
        |   |   |---github_authentication_service.py
        |   |   |---github_integration_service.py
        |   |
        |   \---utils
        |   |   |---utilitaries.py  
        |   |
        |   |   api.py
        |   |   cache_instance.py
        |   |   config.py
        |   
        \---test       
            |   tests.py 
            | 
      

````````            
##### ``Considerações``
Percebi que a estrutura do projeto poderia melhorar, então visando a melhoria, estudei mais afundo e alterei toda a estruturação das pastas e dos arquivos hoje (19/07).
Sobre a documentação, tentei melhorar o swagger, visando melhorar o entendimento de como os endpoints se comportam.


Alguns pontos que estou melhorando: 
Eu tinha dito que iria implementar o Fabric e o Jenkins, mas achei uma solução talvez mais óbvia, que no caso é o Github Actions (no momento estou implementando o mesmo).




