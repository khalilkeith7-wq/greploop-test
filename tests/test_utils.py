"""Tests for utils module."""

import pytest
from my_project.utils import calculate_sum, format_output, process_items, read_config, get_user_input
from unittest.mock import patch


def test_calculate_sum():
    assert calculate_sum(2, 3) == 5


def test_format_output():
    result = format_output([1, 2, 3])
    assert result == "1\n2\n3\n"


def test_format_output_empty():
    result = format_output([])
    assert result == ""


def test_process_items():
    result = process_items([1, 2, 3])
    assert result == [2, 4, 6]


def test_process_items_with_none():
    result = process_items([1, None, 3])
    assert result == [2, 6]


def test_read_config(tmp_path):
    config_file = tmp_path / "config.txt"
    config_file.write_text("test_config_content")
    result = read_config(str(config_file))
    assert result == "test_config_content"


def test_read_config_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_config("/nonexistent/path/config.txt")


def test_get_user_input():
    with patch("builtins.input", return_value="hello"):
        result = get_user_input("Enter: ")
    assert result == "hello"
