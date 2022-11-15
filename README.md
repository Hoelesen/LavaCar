# Projeto LavaCar

Projeto desenvolvido como trabalho de conclusão do curso de Análise e Desenvolvimento de Sistemas do Instituto Federal de Educação, Ciência e Tecnologia de Rondônia Campus Vilhena.

 Autor: Hoelesen França

## Instalação

### **Passo 1:** Instale o Python **(3.8 ou superior)**
### **Passo 2 (Opcional):** Crie um ambiente virtual para os pacotes do projeto
* `py -m venv ${CAMINHO_AMBIENTE_VIRTUAL}` o ambiente virtual **DEVE** estar fora do repositório git para não entrar no tracking
* `source ${CAMINHO_AMBIENTE_VIRTUAL}/bin/activate` **NO LINUX**
* `${CAMINHO_AMBIENTE_VIRTUAL}/Scripts/activate.bat` **NO WINDOWS**
### **Passo 3:**  Instale o Django e confirme se está tudo ok
* `py -m pip install Django`
* `django-admin --version`
### **Passo 4:** No diretório **/lavacar**, instale os pacotes do projeto
* `py -m pip install -r requirements.txt`
### **Passo 5:** Execute as migrações para criar o banco de dados
* `py manage.py migrate`
### **Passo 6:** Crie o superuser para criar os usuários
* `py manage.py createsuperuser`
* Será solicitado o nome do usuário, informe-o no terminal
* Será solicitado o e-mail, informe-o no terminal
* Será solicitada a senha, informe-a no terminal
* Confirme a senha
* Finalize a criação
### **Passo 7:** Execute o projeto
* `py manage.py runserver` 
### **Passo 8:** Crie um usuário da aplicação
* Navegue até **http://127.0.0.1:8000/admin** e faça login com o superuser criado
* Com isso todos os cadastros referentes a autenticação estarão disponíveis

Para informações de como utilizar após a implantação esse repositório possui uma página wiki.
