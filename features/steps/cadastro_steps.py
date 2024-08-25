from behave import given, when, then
from src.user_manager import UserManager, UserAlreadyExistsError, UserNotFoundError

@given('que não há usuários cadastrados')
def step_impl(context):
    context.user_manager = UserManager()

@given('que o usuário "{name}" com email "{email}" está cadastrado')
def step_impl(context, name, email):
    context.user = context.user_manager.add_user(name, email)

@given('que não há usuários com o email "{email}"')
def step_impl(context, email):
    users = context.user_manager.get_users()
    assert all(user.email != email for user in users)

@when('eu cadastro um usuário com nome "{name}" e email "{email}"')
@when('eu tento adicionar um usuário com o email "{email}"')
def step_impl(context, name=None, email=None):
    try:
        if name:
            context.user = context.user_manager.add_user(name, email)
        else:
            context.user_manager.add_user("Nome Placeholder", email)
        context.error = None
    except UserAlreadyExistsError as e:
        context.error = str(e)

@when('eu atualizo o nome do usuário para "{new_name}" e o email para "{new_email}"')
def step_impl(context, new_name, new_email):
    try:
        context.user = context.user_manager.update_user(context.user.email, new_name, new_email)
        context.error = None
    except (UserAlreadyExistsError, UserNotFoundError) as e:
        context.error = str(e)

@when('eu tento atualizar o usuário com o email "{email}"')
def step_impl(context, email):
    try:
        context.user = context.user_manager.update_user(email, "Novo Nome", "novoemail@example.com")
        context.error = None
    except UserNotFoundError as e:
        context.error = str(e)
        
@when('eu removo o usuário com email "{email}"')
def step_impl(context, email):
    try:
        context.user_manager.remove_user(email)
        context.error = None
    except UserNotFoundError as e:
        context.error = str(e)

@then('o sistema deve registrar o usuário "{name}" com o email "{email}"')
def step_impl(context, name, email):
    user = context.user
    assert user.name == name
    assert user.email == email

@then('o sistema deve atualizar o usuário para o nome "{new_name}" e o email "{new_email}"')
def step_impl(context, new_name, new_email):
    assert context.user.name == new_name
    assert context.user.email == new_email

@then('o sistema não deve ter nenhum usuário com email "{email}"')
def step_impl(context, email):
    users = context.user_manager.get_users()
    assert all(user.email != email for user in users)

@then('o sistema deve ter {count} usuário cadastrado')
@then('o sistema deve ter {count} usuário(s) cadastrado(s)')
def step_impl(context, count):
    assert len(context.user_manager.get_users()) == int(count)

@then('o sistema deve retornar um erro dizendo que o usuário não foi encontrado')
def step_impl(context):
    assert context.error is not None
    assert "não encontrado" in context.error

@then('o sistema deve retornar um erro dizendo que o email já está registrado')
def step_impl(context):
    assert context.error is not None
    assert "já está registrado" in context.error

@then('o sistema não deve retornar nenhum erro')
def step_impl(context):
    assert context.error is None
