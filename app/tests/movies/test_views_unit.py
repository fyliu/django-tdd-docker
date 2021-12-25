import pytest
from django.http import Http404

from movies.views import MovieSerializer, MovieDetail, Movie


def test_add_movie(client, monkeypatch):
    pass


def test_add_movie_invalid_json(client):
    pass


def test_add_movie_invalid_json_keys(client):
    pass


def test_get_single_movie(client, monkeypatch):
    pass


def test_get_single_movie_incorrect_id(client):
    pass


def test_get_all_movies(client, monkeypatch):
    pass


def test_remove_movie(client, monkeypatch):
    pass


def test_remove_movie_incorrect_id(client, monkeypatch):
    pass


def test_update_movie(client, monkeypatch):
    pass


def test_update_movie_incorrect_id(client, monkeypatch):
    pass


@pytest.mark.parametrize(
    "payload, status_code",
    [[{}, 400], [{"title": "The Big Lebowski", "genre": "comedy"}, 400]],
)
def test_update_movie_invalid_json(client, monkeypatch, payload, status_code):
    pass