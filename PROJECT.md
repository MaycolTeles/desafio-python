# Functionamento do Script
Para executar o script, basta seguir os seguintes passos:

## Clonar o repositório
- Certifique-se de que o arquivo "csv_reader.py" está na sua pasta "src/"

## Executar o script
 - Para executar o script, basta abrir o terminal na pasta onde está seu arquivo "csv_reader.py" e e executar o seguinte comando:
 ```$ python csv_reader.py ```
 ou 
 ```$ python3 csv_reader.py ```, dependendo do seu ambiente.

 - Após isso, será solicitado que você entre com a cidade que deseja enviar a encomenda e qual o peso dela. Caso você digite uma cidade que não se encontra nas cidades cadastradas através do arquivo "transportadoras.csv" disponibilizado, o programa continuará solicitando pela entrada de uma cidade até que o nome da mesma seja válido.

## Considerações do Código
Para esse código, foi aplicado uma metodologia de programação orientado a objetos, por se tratar de um paradigma de programação mais profissional e robusto. Além disso, algumas conversões tiverem de ser feitas nos valores lidos pelo arquivo csv, que continham símbolos ("R$ ") e isso dificulta um pouco as operações de fluidez do código. Para solucionar esse problema, optou-se por remover esses caracteres das strings com o método "built-in" ".replace()"
