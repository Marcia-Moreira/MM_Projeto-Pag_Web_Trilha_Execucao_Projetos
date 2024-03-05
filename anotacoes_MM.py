# Minhas Anotações:

# | Marcia Moreira | Desenvolver a rota para listar as localizações|

# Clonei o repositório atualizado na minha máquina - Diretório: C:\CLONES-GitHub

'''
Referências utilizadas - VSCode / Windows 11 / Python / Flask / Pip / Terminal PowerShell:

01- Abrir um Terminal PowerShell no seu VSCode, estando dentro da pasta correta do repositório (cd + nome da pasta):

02- Entrando na pasta correta do repositório:
=> cd .\ExercicioAPIs_SquadAmeenahGuribFakim\ 

03- Para verificar as versões do Python e do Pip no Ambiente Virtual instalado
=> python --version  (No meu caso Python 3.12.1)
=> pip --version (No meu caso pip 23.2.1)

04- Para Instalar o Ambiente Virtual:
=> pip install virtualenv

05- Se precisar atualizar o pip, pode fazer conforme a msg.:
=> python.exe -m pip install --upgrade pip

06- Criar um Ambiente Virtual:
=> python -m venv .venv   ou  => py -3 -m venv .venv
(irá abrir uma pasta verde .venv no seu diretório)

07- Ativar o Ambiente Virtual (Venv):
=> .\.venv\Scripts\activate
ou
=> .venv\Scripts\activate
(aparecerá no terminal, o nome da sua pasta .venv em verde antes das descrição do diretório)

08- Para interromper o Ambiente Virtual:
=> deactivate

09- Instalação do FLASK no ambiente virtual:
=> pip install Flask

10- Se pedir novamente para atualizar o pip, pode fazer conforme a msg.:
=> python.exe -m pip install --upgrade pip
=> pip --version (No caso, foi para pip 24.0)

11- Para Ativar o Servidor no Flask:  "Levantar um Servidor Local":
=> flask --app app run
(onde o segundo app é o nome do seu arquivo de rota .py)

12- Para interromper o servidor:
=> Ctrl + C

13- Para Limpar a tela do Terminal:
=> clear (Limpa o Terminal)

(PRONTO - Podemos começar a criar as Rotas do Projeto!) 

----------------------------------------------------------------

14- Comandos Diversos:
=> clear (Limpa o Terminal)
=> pip list
=> pip --version
=> python --version
=> pip install virtualenv
=> python -m venv WEB-cafejas-Cafeteria_e_Cervejaria


DJANGO:
=> python manage.py runserver (No Django)
=> python manage.py startapp app_rest_api 
=> pip install djangorestframework
=> python manage.py startapp app_base_cafejas
=> django-admin startproject projeto_cafejas .
=> pip install django
=> python -m venv WEB-cafejas-Cafeteria_e_Cervejaria

'''

'''
pip list:
C:\CLONES-GitHub\ExerciciosPython_SquadAmeenahGuribFakim\ExercicioAPIs_SquadAmeenahGuribFakim> pip list
Package      Version
------------ -------
blinker      1.7.0
click        8.1.7
colorama     0.4.6
Flask        3.0.2
itsdangerous 2.1.2
Jinja2       3.1.3
MarkupSafe   2.1.5
pip          24.0
Werkzeug     3.0.1
'''