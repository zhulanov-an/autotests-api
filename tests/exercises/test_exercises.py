from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        create_exercise_request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        create_exercise_response = exercises_client.create_exercise_api(request=create_exercise_request)
        create_exercise_response_data = CreateExerciseResponseSchema.model_validate_json(create_exercise_response.text)

        assert_status_code(create_exercise_response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(create_exercise_schema_response=create_exercise_response_data.exercise,
                                        create_exercise_request=create_exercise_request)

        validate_json_schema(create_exercise_response.json(), create_exercise_response_data.model_json_schema())

    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        get_exercise_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        get_exercise_response_data = GetExerciseResponseSchema.model_validate_json(get_exercise_response.text)

        assert_status_code(get_exercise_response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(get_exercise_schema_response=get_exercise_response_data,
                                     create_exercise_response=function_exercise.response)
        validate_json_schema(get_exercise_response.json(), get_exercise_response_data.model_json_schema())
