import pytest
import allure

@allure.step
def simple_step(step_param1, step_param2 = None):
    pass

@pytest.mark.parametrize('param1', [True, False], ids=['1', '2'])
def test_parameterize_with_id(param1):
    simple_step(param1)

@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['1', '2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step(param1, param2)