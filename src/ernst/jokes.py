"""Module for fetching jokes."""

import requests
import random

from pydantic import BaseModel, ConfigDict

from .content import data


class DadJoke(BaseModel):
    """A dad joke."""

    model_config = ConfigDict(extra="ignore")

    id: str
    joke: str


class DadJokeSearch(BaseModel):
    """A dad joke search."""

    model_config = ConfigDict(extra="ignore")

    total_jokes: int
    results: list[DadJoke]


class DadJokeClient:
    """Client for fetching dad jokes."""

    def __init__(self, timeout: int = 10):
        """Initialize the client."""
        self.base_url = "https://icanhazdadjoke.com/"
        self.headers = {
            "Accept": "application/json",
        }
        self.timeout = timeout

    def get_random_joke(self) -> DadJoke:
        """Get a random joke."""
        response = requests.get(
            self.base_url, headers=self.headers, timeout=self.timeout
        )
        response.raise_for_status()
        return DadJoke.model_validate(response.json())

    def get_search_jokes(self, search: str) -> DadJokeSearch:
        """Get jokes that match the search query."""
        response = requests.get(
            f"{self.base_url}/search",
            headers=self.headers,
            params={"term": search},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return DadJokeSearch.model_validate(response.json())


def search_joke_online(search: str) -> DadJoke:
    """Search for jokes."""
    client = DadJokeClient()
    jokes = client.get_search_jokes(search)
    if jokes.total_jokes == 0:
        joke = client.get_random_joke()
        return joke
    return random.choice(jokes.results)


def fallback_joke(search: str) -> DadJoke:
    """Fallback joke."""
    return DadJoke(
        id="fallback",
        joke=random.choice(data.joke),
    )


def get_joke(search: str) -> DadJoke:
    """Try to get a joke from the internet, fallback to a default joke."""
    try:
        return search_joke_online(search.strip())
    except (requests.RequestException, ValueError, KeyError):
        return fallback_joke(search)
