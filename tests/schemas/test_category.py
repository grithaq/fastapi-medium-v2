from src.schemas.category import (
    CategoryRequest,
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
    CategorySchema,
    ListCategoryRespose
)


def test_category_request():
    category = CategoryRequest(id=1, name="test")
    assert category.id == 1
    assert category.name == "test"


def test_category_create():
    category = CategoryCreate(name="test")
    assert category.name == "test"


def test_category_update():
    category = CategoryUpdate(name="test")
    assert category.name == "test"


def test_category_response():
    category = CategoryResponse(data=[], message="success", status=str(200))
    assert category.data == []
    assert category.message == "success"
    assert category.status == str(200)


def test_category_schema():
    category = CategorySchema(id=1, name="test", user_id=1)
    assert category.id == 1
    assert category.name == "test"
    assert category.user_id == 1


def test_list_category_response():
    category = ListCategoryRespose(current=1, total=1, data=[], message="success", status=str(200))
    assert category.current == 1
    assert category.total == 1
    assert category.data == []
    assert category.message == "success"
    assert category.status == str(200)