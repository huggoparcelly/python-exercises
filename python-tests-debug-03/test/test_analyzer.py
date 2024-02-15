from unittest.mock import Mock, patch

import pytest

from analyzer import analyze_json_file, read_json_file

def test_analyze_json_file():

    # mock_read_json = Mock(return_value={"nome": "João", "idade": 31})
    mock_read_json = Mock(
        side_effect=[
            {"nome": "João", "idade": 31},
            {"nome": "Maria", "idade": 25}
        ]
    )
    fake_file_path = "invalid.json"

    with patch("analyzer.read_json_file", mock_read_json):
        assert (analyze_json_file(fake_file_path) == "A pessoa de nome João tem 31 anos de idade.")
        assert (analyze_json_file(fake_file_path) == "A pessoa de nome Maria tem 25 anos de idade.")
    
    mock_read_json.assert_called_with(fake_file_path)


def test_analyze_json_file_propagetes_exception():

    mock_read_json = Mock(side_effect=FileNotFoundError)
    fake_file_path = "invalid.json"

    with patch("analyzer.read_json_file", mock_read_json):
        with pytest.raises(FileNotFoundError):
            analyze_json_file(fake_file_path)

def test_read_json_file(tmp_path):
    fake_file_path = tmp_path / "fake.json"
    fake_file_path.touch()

    mock_json = Mock()
    mock_json.load = Mock(return_value={"nome": "João", "idade": 31})

    with patch("analyzer.json", mock_json):
        result = read_json_file(fake_file_path)

    assert result == {"nome": "João", "idade": 31}


def test_analyze_rise_exception_when_is_not_json_file():

    mock_read_json = Mock(side_effect=ValueError)
    fake_file_path = "invalid.txt"

    with patch("analyzer.read_json_file", mock_read_json):
        with pytest.raises(ValueError, match='File must be a JSON file'):
            analyze_json_file(fake_file_path)