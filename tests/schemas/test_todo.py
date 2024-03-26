from src.schemas.todo import (
    TodoRequest,
    TodoCreate,
    TodoUpdate,
    TodoResponse,
    TodoSchema,
    ListTodoResponse,
    CategoryRequest
)


def test_todo_request():
    todo = TodoRequest(title="test", description="ini ngetest", category_id=1)
    assert todo.title == "test"
    assert todo.description == "ini ngetest"
    assert todo.category_id == 1


def test_todo_create():
    todo = TodoCreate(title="test", description="ini ngetest", category_id=1)
    assert todo.title == "test"
    assert todo.description == "ini ngetest"
    assert todo.category_id == 1


def test_todo_update():
    todo = TodoUpdate(title="test", description="ini ngetest", category_id=1)
    assert todo.title == "test"
    assert todo.description == "ini ngetest"
    assert todo.category_id == 1

def test_todo_response():
    todo = TodoResponse(data=[], message="success", status=str(200))
    assert todo.data == []
    assert todo.message == "success"
    assert todo.status == str(200)


def test_todo_schema():
    category = CategoryRequest(id=1, name="test")
    todo = TodoSchema(id=1, title="test", description="ini ngetest", user_id=1, category=category)
    assert todo.id == 1
    assert todo.title == "test"
    assert todo.description == "ini ngetest"
    assert todo.user_id == 1
    assert todo.category.id == 1
    assert todo.category.name == "test"


def test_list_todo_response():
    todo = ListTodoResponse(current=1, total=1, data=[], message="success", status=str(200))
    assert todo.current == 1
    assert todo.total == 1
    assert todo.data == []
    assert todo.message == "success"
    assert todo.status == str(200)
