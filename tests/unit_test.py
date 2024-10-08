import click.testing
import pytest

from learn_python import client


@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock

def test_main_success(runner, mock_requests_get):
    result = runner.invoke(client.main)

    assert result.exit_code == 0

def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(client.main)
    assert "Lorem Ipsum" in result.output

def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(client.main)
    assert mock_requests_get.called

def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    runner.invoke(client.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]
