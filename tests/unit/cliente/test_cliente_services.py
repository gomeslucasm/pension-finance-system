from api.cliente.schemas import ClientCreate
from api.common.errors import ValidationError
from tests.unit.cliente.fixtures import *
from datetime import datetime


def test_create_client_service(
    client_service, mock_client_repository, valid_cpf, create_client
):
    birth_date = datetime(year=1975, month=4, day=1)
    client_data = ClientCreate(
        cpf=valid_cpf,
        nome="Test User",
        email="test@example.com",
        dataDeNascimento=birth_date,
        genero="Masculino",
        rendaMensal=1000.0,
    )

    mock_client_repository.get_by_cpf.return_value = None
    client = create_client(
        cpf=client_data.cpf,
        nome=client_data.nome,
        email=client_data.email,
        data_de_nascimento=client_data.data_de_nascimento,
        genero=client_data.genero,
        renda_mensal=client_data.renda_mensal,
    )
    mock_client_repository.create.return_value = client

    new_client = client_service.create_client(client_data)

    mock_client_repository.get_by_cpf.assert_called_once_with(client_data.cpf)
    mock_client_repository.create.assert_called_once_with(
        cpf=client_data.cpf,
        nome=client_data.nome,
        email=client_data.email,
        data_de_nascimento=client_data.data_de_nascimento,
        genero=client_data.genero,
        renda_mensal=client_data.renda_mensal,
    )
    assert new_client == client


def test_create_client_error_on_existent_cpf(
    client_service, mock_client_repository, valid_cpf, create_client
):
    birth_date = datetime(year=1975, month=4, day=1)
    client_data = ClientCreate(
        cpf=valid_cpf,
        nome="Test User",
        email="test@example.com",
        dataDeNascimento=birth_date,
        genero="Masculino",
        rendaMensal=1000.0,
    )

    client = create_client(
        cpf=client_data.cpf,
        nome="Test User",
        email="test@example.com",
        data_de_nascimento=birth_date,
        genero="Masculino",
        renda_mensal=1000.0,
    )

    mock_client_repository.get_by_cpf.return_value = client
    mock_client_repository.create.return_value = client_data

    with pytest.raises(
        ValidationError, match=f"Client with this CPF={client.cpf} already exists"
    ):
        client_service.create_client(client_data)
