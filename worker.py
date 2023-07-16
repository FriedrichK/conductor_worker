from conductor.client.automator.task_handler import TaskHandler
from conductor.client.worker.worker import Worker

from includes.configuration import conductor_configuration
from includes.database import interface
from includes.tasks import evaluate_games_starting_conditions_v1, add_player_v1, create_game_in_backend_v1

workers = [
    Worker(
        task_definition_name='evaluate_games_starting_conditions_v1',
        execute_function=evaluate_games_starting_conditions_v1,
        poll_interval=5,
    ),
    Worker(
        task_definition_name="create_game_in_backend_v1",
        execute_function=create_game_in_backend_v1,
        poll_interval=5,
    ),
    Worker(
        task_definition_name="add_player_v1",
        execute_function=add_player_v1,
        poll_interval=5,
    )
]

with TaskHandler(workers, conductor_configuration) as task_handler:
    task_handler.start_processes()
    task_handler.join_processes()
