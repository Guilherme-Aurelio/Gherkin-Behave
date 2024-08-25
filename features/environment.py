from behave import fixture, use_fixture
from src.user_manager import UserManager

@fixture
def setup_user_manager(context):
    context.user_manager = UserManager()

def before_scenario(context, scenario):
    use_fixture(setup_user_manager, context)
