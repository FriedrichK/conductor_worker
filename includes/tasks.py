from conductor.client.http.models import TaskResult, Task
from conductor.client.http.models.task_result_status import TaskResultStatus

from includes.database.model_functions import create_user, create_game


def evaluate_games_starting_conditions_v1(task: Task) -> TaskResult:
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id='your_custom_id'
    )
    task_result.add_output_data('evaluation_successful', True)
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def create_game_in_backend_v1(task: Task) -> TaskResult:
    create_game(id=task.workflow_instance_id)
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id='your_custom_id'
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result


def add_player_v1(task: Task) -> TaskResult:
    create_user(id=task.workflow_instance_id, game_id=task.input_data.get("game_round_workflow_id"), name=task.input_data.get("player_name"))
    task_result = TaskResult(
        task_id=task.task_id,
        workflow_instance_id=task.workflow_instance_id,
        worker_id='your_custom_id'
    )
    task_result.status = TaskResultStatus.COMPLETED
    return task_result
