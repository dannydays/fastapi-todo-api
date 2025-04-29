# ToDo List - API

Este é um projeto de API para gerenciamento de tarefas, desenvolvido com **FastAPI** e **SQLAlchemy**. Ele permite que os usuários criem, visualizem, atualizem e excluam tarefas, além de autenticação e autorização com tokens JWT.

## Funcionalidades

- **Autenticação e Autorização**:
  - Login com geração de tokens JWT.
- **Gerenciamento de Tarefas**:
  - Criar tarefas.
  - Listar tarefas.
  - Atualizar tarefas.
  - Marcar tarefas como concluídas.
  - Excluir tarefas individualmente ou todas de uma vez.
- **Gerenciamento de Usuários**:
  - Cadastro de novos usuários.
  - Atualização de informações do usuário.
  - Exclusão de usuários.

## Tecnologias Utilizadas

- **Python** com **FastAPI**
- **SQLAlchemy** para ORM
- **SQLite** como banco de dados
- **JWT** para autenticação
- **Passlib** para hashing de senhas

## Requisitos

- Python 3.9 ou superior
- Gerenciador de pacotes `pip`

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/dannydays/fastapi-todo-api.git
   cd fastapi-todo-api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:
   - O banco de dados padrão é o SQLite, configurado no arquivo `database.py`. Caso deseje usar outro banco, atualize a variável `DATABASE_URL`.

5. Execute a aplicação:
   ```bash
   uvicorn main:app
   ```

6. Acesse a documentação interativa da API:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)

![ToDo_swagger](docs/ToDo_swagger.png)

## Estrutura do Projeto

```
task_manager/
├── crud/               # Operações de banco de dados
├── routers/            # Rotas da API
├── schemas/            # Schemas Pydantic
├── models.py           # Modelos do banco de dados
├── database.py         # Configuração do banco de dados
├── JWTtoken.py         # Funções para geração e verificação de tokens JWT
├── oauth2.py           # Middleware de autenticação
├── hash.py             # Função de hashing de senhas
├── main.py             # Ponto de entrada da aplicação
└── README.md           # Documentação do projeto
```

## Endpoints Principais

### Autenticação
- **POST** `/login`: Realiza login e retorna um token JWT.

### Usuários
- **GET** `/users/`: Lista todos os usuários (requer autenticação).
- **GET** `/users/{id}`: Retorna os detalhes de um usuário específico.
- **POST** `/users/register`: Registra um novo usuário.
- **PUT** `/users/`: Atualiza as informações do usuário autenticado.
- **DELETE** `/users/`: Exclui o usuário autenticado.

### Tarefas
- **GET** `/tasks/`: Lista todas as tarefas do usuário autenticado.
- **POST** `/tasks/`: Cria uma nova tarefa.
- **PUT** `/tasks/check/{task_id}`: Marca/desmarca uma tarefa como concluída.
- **PUT** `/tasks/{task_id}`: Atualiza os detalhes de uma tarefa específica.
- **DELETE** `/tasks/{task_id}`: Exclui uma tarefa específica.
- **DELETE** `/tasks/`: Exclui todas as tarefas do usuário autenticado.

## Observações

Este projeto é um **MVP (Mínimo Produto Viável)**, desenvolvido para fins de estudo e demonstração de habilidades técnicas.

Possíveis melhorias futuras:
- Implementação de **testes automatizados** (unitários e de integração).
- Inclusão de **logs estruturados** para monitoramento e identificação de erros.
- Criação de **endpoints mais específicos** (ex: filtros de tarefas por status ou data).
- Implementação de **padrões de resposta** (JSON padronizado para sucesso e erro).
- Suporte a **paginação** em listagens de tarefas e usuários.
- Uso de **outros bancos de dados** (PostgreSQL, MySQL) com ambiente configurável.
- **Validação mais robusta** de entradas (ex: tamanho mínimo/máximo de campos).
- Melhorias de **segurança**, como controle de tentativas de login e proteção contra ataques comuns.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
