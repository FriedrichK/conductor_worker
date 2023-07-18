from conductor.client.automator.task_handler import TaskHandler
from conductor.client.worker.worker import Worker

from includes.configuration import conductor_configuration
from includes.tasks import (
    evaluate_games_starting_conditions_v1,
    add_player_v1,
    create_game_in_backend_v1,
    stop_waiting_to_start_game_if_max_player_count_is_reached_v1,
    get_list_of_active_players_v1,
    create_player_topic_v1,
    prompt_player_interaction_v1,
    set_variables_for_start_player_interactions_v1,
)

workers = [
    Worker(
        task_definition_name="evaluate_games_starting_conditions_v1",
        execute_function=evaluate_games_starting_conditions_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="create_game_in_backend_v1",
        execute_function=create_game_in_backend_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="add_player_v1",
        execute_function=add_player_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="stop_waiting_to_start_game_if_max_player_count_is_reached_v1",
        execute_function=stop_waiting_to_start_game_if_max_player_count_is_reached_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="get_list_of_active_players_v1",
        execute_function=get_list_of_active_players_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="create_player_topic_v1",
        execute_function=create_player_topic_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="set_variables_for_start_player_interactions_v1",
        execute_function=set_variables_for_start_player_interactions_v1,
        poll_interval=1,
    ),
    Worker(
        task_definition_name="prompt_player_interaction_v1",
        execute_function=prompt_player_interaction_v1,
        poll_interval=1,
    ),
]

with TaskHandler(workers, conductor_configuration) as task_handler:
    task_handler.start_processes()
    task_handler.join_processes()
