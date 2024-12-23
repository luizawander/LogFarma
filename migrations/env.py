from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Importando o Base do seu projeto
from app.database import Base

# Configurando o MetaData do Alembic para rastrear os modelos
target_metadata = Base.metadata

# Este é o objeto de configuração do Alembic, que fornece
# acesso aos valores dentro do arquivo .ini em uso.
config = context.config

# Interpreta o arquivo de configuração para Python logging.
# Esta linha basicamente configura os registradores.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# outros valores da configuração, definidos pelas necessidades de env.py,
# podem ser adquiridos:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Executa as migrações no modo 'offline'.

    Esta função configura o contexto apenas com uma URL,
    sem criar um Engine, embora um Engine também seja aceitável
    aqui. Sem a criação do Engine, não é necessário
    que um DBAPI esteja disponível.

    As chamadas para context.execute() aqui emitem as instruções
    para o output do script.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações no modo 'online'.

    Nesse cenário, precisamos criar um Engine
    e associar uma conexão ao contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
