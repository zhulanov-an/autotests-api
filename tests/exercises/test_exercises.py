from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response
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
