import os

import arrow
import requests
from dacite import from_dict
from requests import Response

from includes import settings
from includes.api.schemas import GameSchema, PlayerListSchema, GameTopicSchema


def create_game(game_id: str, game_name: str) -> dict:
    url: str = os.path.join(settings.REST_API_URL, "games") + "/"
    data: dict = {
        "id": game_id,
        "name": game_name,
        "min_players": 2,
        "max_players": 10,
    }
    response: Response = requests.post(url, data=data, json=True)
    if response.status_code != 201:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )

    return response.json()


def get_game(game_id: str) -> GameSchema:
    url: str = os.path.join(settings.REST_API_URL, "games", game_id)
    response: Response = requests.get(url, json=True)
    if response.status_code != 200:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )
    return GameSchema(**response.json())


def mark_game_as_failed(game_id: str) -> GameSchema:
    url: str = os.path.join(settings.REST_API_URL, "games", game_id) + "/"
    data: dict = {"failed": arrow.utcnow().format()}
    response: Response = requests.patch(url, data=data, json=True)
    if response.status_code != 200:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )
    return GameSchema(**response.json())


def create_user(user_id: str, game_id: str, user_name: str) -> dict:
    url: str = os.path.join(settings.REST_API_URL, "game_users") + "/"
    data: dict = {
        "id": user_id,
        "game": game_id,
        "name": user_name,
    }
    response: Response = requests.post(url, data=data, json=True)
    if response.status_code != 201:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )

    return response.json()


def get_player_list(game_id: str) -> PlayerListSchema:
    url: str = os.path.join(settings.REST_API_URL, "game_users")

    response: Response = requests.get(url, params={"game": game_id})
    if response.status_code != 200:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )

    return from_dict(data_class=PlayerListSchema, data=response.json())


def stop_waiting_to_start_game(game_id: str) -> None:
    wait_task_ref: str = "wait_for_players_v1"

    url: str = os.path.join(
        settings.CONDUCTOR_API_URL,
        "queue",
        "update",
        game_id,
        wait_task_ref,
        "COMPLETED",
    )

    response: Response = requests.post(url, json=True)
    if response.status_code != 200:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )


def create_player_topic(game_id: str, user_id: str) -> GameTopicSchema:
    url: str = os.path.join(settings.REST_API_URL, "game_topics") + "/"
    data: dict = {
        "game": game_id,
        "player": user_id,
    }
    response: Response = requests.post(url, data=data, json=True)
    if response.status_code != 201:
        raise AssertionError(
            f"unexpected error with code {response.status_code}: {response.content}"
        )

    return from_dict(data_class=GameTopicSchema, data=response.json())
