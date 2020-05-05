# RPG Character

## PyCharm
* Importar a apliação
    * File -> Open
* Adicionar o interpretador
    * File -> Settings ->  Python Interpreter -> Clique na engrenagem em Add -> New Environment
* Importar libs do python
    * ```pip install -r requirements.txt``` 

## Executar a aplicação 

* No terminal execute o comando abaixo  
    * ```hupper -m waitress --port=8000 main.main:application```
 * Sua aplicação web será executada no endereço
    * ```http://localhost:8000``` 

# A Aplicação

A aplicação deve criar um personagem de escolha do player(cadastrado pela aplicação rpg_player). 

* Deve possuir um endpoint para salvar as informações desse charcater. Esse endpoint deve ser um POST
    * Endpoint: ```/character```
* Deve receber um playload parecido com o abaixo e salvar em um banco dados(no momento pode ser um banco de dados fake)

    ```json
    {
        "player_id": "ID que foi cadastrado na aplicação rpg_player",
        "name": "Nome do Personagem",
        "race": "Ra;ca do personagem",
        "life": 100,        
        "strength": 100,
        "dexterity": 100,
        "intelligence": 100,
        "charisma": 100,
        "wisdom": 100,
        "constitution": 100
    }
    ``` 
* O payload foi uma inspiração tirada do seguinte site
    * https://drive.google.com/file/d/1v_LjX-UU7bIANntPS__H28M7TFB5Ymux/view
    * https://smolderingwizard.files.wordpress.com/2013/11/dd_char_sheet_thumb.png
* Vocês podem alterar e/ou adicionar as informações, copiar do livro dos monstros que qualquer estilo de RPG
* Usem a criatividade.
  