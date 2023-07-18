import json
from typing import List

from conductor.client.http.models import TaskResult, Task
from conductor.client.http.models.task_result_status import TaskResultStatus

from includes.api.interface import (
    create_game,
    create_user,
    get_game,
    get_player_list,
    stop_waiting_to_start_game,
    create_player_topic,
)
from includes.api.schemas import GameSchema, PlayerListSchema, GameTopicSchema


def evaluate_games_starting_conditions_v1(task: Task) -> TaskResult:
    game_info: GameSchema = get_game(game_id=task.workflow_instance_id)
    min_players: int = game_info.min_players

    player_list: PlayerListSchema = get_player_list(game_id=task.workflow_instance_id)

    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    task_result.add_output_data(
        "evaluation_successful", player_list.count >= min_players
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def create_game_in_backend_v1(task: Task) -> TaskResult:
    name: str = task.input_data.get("game_name")
    create_game(game_id=task.workflow_instance_id, game_name=name)
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def add_player_v1(task: Task) -> TaskResult:
    create_user(
        user_id=task.workflow_instance_id,
        game_id=task.input_data.get("game_round_workflow_id"),
        user_name=task.input_data.get("player_name"),
    )
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def stop_waiting_to_start_game_if_max_player_count_is_reached_v1(
    task: Task,
) -> TaskResult:
    game_id: str = task.input_data.get("game_round_workflow_id")

    game_info: GameSchema = get_game(game_id=game_id)
    max_players: int = game_info.max_players

    player_list: PlayerListSchema = get_player_list(game_id=game_id)

    if player_list.count == max_players:
        stop_waiting_to_start_game(game_id=game_id)

    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def get_list_of_active_players_v1(task: Task) -> TaskResult:
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )

    game_id: str = task.input_data.get("game_id")

    player_list: PlayerListSchema = get_player_list(game_id=game_id)
    active_players: List[str] = [game_user.id for game_user in player_list.results]

    task_result.add_output_data("players", active_players)
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def create_player_topic_v1(task: Task) -> TaskResult:
    game_id: str = task.input_data.get("game_id")
    iteration: int = task.input_data.get("iteration")
    players: List[str] = task.input_data.get("players")

    user_id: str = players[iteration - 1]

    result: GameTopicSchema = create_player_topic(
        user_id=user_id,
        game_id=game_id,
    )
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    # task_result.add_output_data("topic_xsfrz", result.id)
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def set_variables_for_start_player_interactions_v1(task: Task) -> TaskResult:
    game_id: str = task.input_data.get("game_id")
    iteration: int = task.input_data.get("iteration")
    players: List[str] = task.input_data.get("players")

    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    task_result.add_output_data(
        "forkedTasks",
        [
            {
                "name": f"player_interaction_workflow_task_v1_{i}",
                "taskReferenceName": f"player_interaction_workflow_task_v1",
                "type": "SUB_WORKFLOW",
                "startDelay": 0,
                "subWorkflowParam": {"name": "player_interaction", "version": 43},
                "optional": False,
                "asyncComplete": False,
            }
            for i, player in enumerate((players or []))
        ],
    )
    task_result.add_output_data(
        "forkedTasksInputs",
        {
            f"player_interaction_workflow_task_v1": {
                "game_id": game_id,
                "players": players,
                "iteration": iteration,
                "player_id": player,
            }
            for i, player in enumerate((players or []))
        },
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def prompt_player_interaction_v1(task: Task) -> TaskResult:
    game_id: str = task.input_data.get("game_id")
    iteration: int = task.input_data.get("iteration")
    players: List[str] = task.input_data.get("players")

    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id="your_custom_id",
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result
