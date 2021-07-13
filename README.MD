#`Desafio StoneCo`

#`Desafio para vaga de desenvolvedor júnior`
------------------------------

##### `Objetivo`
Desenvolver uma API de integração com o GitHub utilizando Python ou Go.

##### `USO`
A Aplicação utiliza docker para facilitar a compilação do ambiente de desenvolvimento em qualquer máquina. Para rodar o projeto basta buildar a imagem e rodar o container dentro do diretório.

```docker
docker-compose up
`````

O serviço rodará em:
````
http://localhost:5000/
````
Para começar, acesse http://localhost:5000/api/authenticate para permitir acesso á rotas especiais.
Feito isso, para consumir o serviço, pode ser usado o programa Postman ou Insomnia (foi utilizado insomnia). Estes permitem alterar os verbos do protocolo HTTP e mandar uma requisição complexa com muita simplicidade.
(Há dois arquivos na pasta raiz, onde se pode importar a pasta com os requests que utilizei durante o desenvolvimento)

##### ```ENDPOINTS```

```
A documentação pode ser encontrada em http://localhost:5000/api/docs
```

Para realizar um pedido bastar alterar <user> e <repo> por um úsuario e um repositório que deseja:
O USER e REPO devem ser válidos ou existentes, caso contrário, será retornado um erro "An error ocurred in your request!"

##### ```Tests```
Para rodar os tests, basta acessar a pasta raiz com seu CLI de preferência e rodar
```
python -m unittest
`````

##### ``A Aplicação``
Para criar a aplicação me baseei em projetos que já fiz em outras linguagens e ambientes, organizar o projeto com um controller, uma classe de serviço e um Util, me ajudou a deixar o código mais organizado e legível.

O Docker-compose cria uma imagem pronta do Python com a distribuição Alpine do Linux presente no DockerHub, e uma imagem do Redis.


<small>Estrutura de pastas:</small>
````````
/
|   .gitignore
|   .dockerignore
|   main.py
|   test.py
|   Dockerfile
|   docker-compose
|   requirements.txt
|   README.MD
|   GitHub Integration.insomnia_collection
|   GitHub Integration.postman_collection
|   
\---src
    |   
    |   
    +---resources
    |   |---controllers.py
    |   |---services.py
    |   |---utils.py
    |            
    |           
    +---server
    |   |---instance.py
    |             
      

````````            
##### ``Considerações``
Bom, da ultima versão pra cá, a unica coisa que faltou implementar, foi o Jenkins. Eu realmente queria ter implementado ele,
mas preferi focar nas outras coisas.
Sobre a documentação, eu já tinha configurado o endpoint para acessar o swagger, porém esqueci de falar sobre aqui no README.


Alguns pontos que pretendo melhorar no futuro: 
Implementar o Fabric para automatizações de deploys e o Jenkins para CI e CD;



