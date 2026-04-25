from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseSchema, GetExerciseResponseSchema, \
    CreateExerciseResponseSchema, UpdateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(create_exercise_schema_response: ExerciseSchema,
                                    create_exercise_request: CreateExerciseRequestSchema):
    """
    Проверяет, что модель упражнения из ответа на создание упражнения
    соответствует данным из запроса создания упражнения.
    :param create_exercise_schema_response: Модель упражнения из ответа на создание упражнения.
    :param create_exercise_request: Запрос на создание упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(create_exercise_schema_response.title,
                 create_exercise_schema_response.title, "title")
    assert_equal(create_exercise_schema_response.course_id,
                 create_exercise_schema_response.course_id, "course_id")
    assert_equal(create_exercise_schema_response.max_score,
                 create_exercise_request.max_score, "max_score")
    assert_equal(create_exercise_schema_response.min_score,
                 create_exercise_request.min_score, "min_score")
    assert_equal(create_exercise_schema_response.order_index,
                 create_exercise_request.order_index, "order_index")
    assert_equal(create_exercise_schema_response.description,
                 create_exercise_request.description, "description")
    assert_equal(create_exercise_schema_response.estimated_time,
                 create_exercise_request.estimated_time, "estimated_time")


def assert_exercise(actual_exercise_schema: ExerciseSchema, expected_exercise_schema: ExerciseSchema):
    """
    Проверяет фактическую и ожидаемую модель упражнения
    :param actual_exercise_schema: Актуальная модель упражнения
    :param expected_exercise_schema: Ожидаемая модель упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual_exercise_schema.id, expected_exercise_schema.id, "id")
    assert_equal(actual_exercise_schema.title, expected_exercise_schema.title, "title")
    assert_equal(actual_exercise_schema.course_id, expected_exercise_schema.course_id, "course_id")
    assert_equal(actual_exercise_schema.max_score, expected_exercise_schema.max_score, "max_score")
    assert_equal(actual_exercise_schema.min_score, expected_exercise_schema.min_score, "min_score")
    assert_equal(actual_exercise_schema.order_index, expected_exercise_schema.order_index, "order_index")
    assert_equal(actual_exercise_schema.description, expected_exercise_schema.description, "description")
    assert_equal(actual_exercise_schema.estimated_time, expected_exercise_schema.estimated_time, "estimated_time")


def assert_get_exercise_response(get_exercise_schema_response: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema):
    """
    Проверяет модель упражнения от запроса получения упражнения с моделью ответа на создание упражнения
    :param get_exercise_schema_response: Ответ получения упражнения.
    :param create_exercise_response: Ответ создания упражнения.
    :raises AssertionError: Если хотя бы одно поле упражнения в ответах не совпадает.
    """
    assert_exercise(actual_exercise_schema=get_exercise_schema_response.exercise,
                    expected_exercise_schema=create_exercise_response.exercise)


def assert_update_exercise_response(update_exercise_schema_response: ExerciseSchema,
                                    update_exercise_request: UpdateExerciseRequestSchema):
    """
    Проверяет ответ обновления упражнения с запросом обновления упражнения
    :param update_exercise_schema_response: Ответ обновления упражнения.
    :param update_exercise_request: Запрос обновления упражнения.
    :raises AssertionError: Если хотя бы одно поле обновления упражнения в ответе и запросе не совпадает.
    """
    assert_equal(update_exercise_schema_response.title, update_exercise_request.title, "title")
    assert_equal(update_exercise_schema_response.max_score, update_exercise_request.max_score, "max_score")
    assert_equal(update_exercise_schema_response.min_score, update_exercise_request.min_score, "min_score")
    assert_equal(update_exercise_schema_response.order_index, update_exercise_request.order_index, "order_index")
    assert_equal(update_exercise_schema_response.description, update_exercise_request.description, "description")
    assert_equal(update_exercise_schema_response.estimated_time,
                 update_exercise_request.estimated_time, "estimated_time")
