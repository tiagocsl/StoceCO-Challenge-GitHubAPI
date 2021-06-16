#`Desafio StoneCo`

#`Desafio para vaga de desenvolvedor júnior`
------------------------------

##### `Objetivo`
Desenvolver uma API de integração com o GitHub utilizando Python ou Go.

##### `USO`
A Aplicação utiliza docker para facilitar a compilação do ambiente de desenvolvimento em qualquer máquina. Para rodar o projeto basta buildar a imagem e rodar o container dentro do diretório.

```docker
docker build -f .\Dockerfile -t python/integration .
docker run -itd --name python_api_integration -p 5000:5000 python/integration
`````

O serviço rodará em:
````
http://localhost:5000/
````

Para consumir o serviço, pode ser usado o programa Postman ou Insomnia (foi utilizado insomnia). Estes permitem alterar os verbos do protocolo HTTP e mandar uma requisição complexa com muita simplicidade.
(Há dois arquivos na pasta raiz, onde se pode importar a pasta com os requests que utilizei durante o desenvolvimento)

##### ```ENDPOINTS```
A API conta com os seguintes endpoints:
<img src="https://i.imgur.com/ct2yr4F.png">

Para realizar um pedido bastar alterar <user> e <repo> por um úsuario e um repositório que deseja:
```
GET /api/repos/tiagocsl/popular-repository
ou 
GET /api/repos/tiagocsl/StoceCO-Challenge-GitHubAPI/popular-issues 
ou 
GET /api/repos/tiagocsl/StoceCO-Challenge-GitHubAPI/uninteracted-pull
```
O USER e REPO devem ser válidos ou existentes, caso contrário, será retornado um erro "An error ocurred in your request!"

##### ```Tests```
Para rodar os tests, basta acessar a pasta raiz com seu CLI de preferência e rodar
```
py -m unittest
`````

##### ``A Aplicação``
Para criar a aplicação me baseei em projetos que já fiz em outras linguagens e ambientes, organizar o projeto com um controller, uma classe de serviço e um Util, me ajudou a deixar o código mais organizado e legível.

O Dockerfile roda uma imagem pronta do Python com a distribuição Alpine do Linux presente no DockerHub, algumas dependências extras foram adicionadas pois o pacote mysqlclient do Python não está funcionando caso seja instalado da web, se faz necessário utilizar os pacotes descritos abaixo, ou baixar manualmente o client e instalar via pip.


<small>Estrutura de pastas:</small>
````````
/
|   .gitignore
|   .dockerignore
|   main.py
|   test.py
|   Dockerfile
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
Apesar do meu prazo escolhido, tive problemas pessoais e de saúde durante a semana, fiz essa aplicação no pouco tempo que me sobrou em 4 dias. Apesar de já ter feito scripts entre outras coisas em python, foi muito diferente aprender implementar o Mock em python, de fato um desafio e foi o que me tomou mais tempo, pois levantar o server e fazer os serviços foi fácil, problema foi entender como usar o patch no Mock, já que cada tutorial ou Doc que eu estudava fazia algo diferente. 
Como dito antes, não tive muito tempo, por isso não conseguir cumprir meu desejo de implementar o Jenkins a tempo, por mais que tenha começado, não iria conseguir terminar a tempo, o mesmo digo do Redis para a camada de cache.
Outro ponto importante, meu computador não suporta Docker, pois é Win10Home, meu Ubuntu deu problema e ainda não tive tempo pra resolver. Então, tive que ficar testando o Docker enviando o app para um amigo.


Alguns pontos que pretendo melhorar no futuro: 
Criar um docker compose;
Implementar o Redis e a biblioteca PyGitHub para auxiliar na montagem do projeto;
Implementar o Fabric para automatizações de deploys e o Jenkins para CI e CD;
Adicionar camadas de autenticação; 



