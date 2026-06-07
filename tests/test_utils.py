"""Tests for utils module."""

import pytest
from my_project.utils import calculate_sum, format_output, process_items


def test_calculate_sum():
    assert calculate_sum(2, 3) == 5


def test_format_output():
    result = format_output([1, 2, 3])
    assert "1" in result
    assert "2" in result


def test_process_items():
    result = process_items([1, 2, 3])
    assert result == [2, 4, 6]


def test_process_items_with_none():
    result = process_items([1, None, 3])
    assert result == [2, 6]
