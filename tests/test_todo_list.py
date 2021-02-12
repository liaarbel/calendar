from datetime import date, time

import pytest
from sqlalchemy.orm.exc import NoResultFound

from app.database.models import Task, User
from app.internal.todo_list import by_id
from tests.utils import create_model, delete_instance

DATE = date(2021, 2, 2)
TIME = time(20, 0)


@pytest.fixture
def task(session, user):
    task_example = create_model(
        session, Task, id=1, title="Test", description="test my create",
        is_done=False, is_important=False, date=DATE, time=TIME,
        owner_id=1, owner=user
    )
    yield task_example
    delete_instance(session, task_example)


@pytest.fixture
def task2(session, user):
    task_example = create_model(
        session, Task, id=1, title="Test2", description="test my create2",
        is_done=False, is_important=True, date=DATE, time=TIME,
        owner_id=1, owner=user
    )
    yield task_example
    delete_instance(session, task_example)


@pytest.fixture
def test1():
    return User(username='test1', email='blala@something.com',
                password='123456', full_name='any name')


def test_if_task_deleted(home_test_client, task: Task, session):
    response = home_test_client.post("/task/delete", data={"taskId": task.id})
    assert response.status_code == 302
    with pytest.raises(NoResultFound):
        by_id(session, task.id)


def test_if_task_created(home_test_client, session, task: Task, test1):
    session.add(test1)
    response = home_test_client.post("/task/add",
                                     data={"title": task.title,
                                           "description": task.description,
                                           "datestr": task.date,
                                           "timestr": task.time,
                                           "is_important": task.is_important,
                                           "session": session})
    assert response.status_code == 303
    task_ex = by_id(session, task.id)
    assert task == task_ex


def test_if_task_edited(home_test_client, session, task2: Task):
    response = home_test_client.post("/task/edit",
                                     data={"task_id": task2.id,
                                           "title": task2.title,
                                           "description": task2.description,
                                           "datestr": task2.date,
                                           "timestr": task2.time,
                                           "is_important": task2.is_important,
                                           "session": session})
    assert response.status_code == 303
    task_ex = by_id(session, task2.id)
    assert task2.title == task_ex.title
    assert task2.description == task_ex.description
    assert task2.time == task_ex.time
    assert task2.is_important == task_ex.is_important


def test_if_task_has_done(home_test_client, session, task: Task):
    response = home_test_client.post(f"/task/setDone/{task.id}",
                                     data={"task_id": task.id,
                                           "session": session})
    assert response.status_code == 303
    task_ex = by_id(session, task.id)
    assert task_ex.is_done is True


def test_if_task_has_not_done(home_test_client, session, task: Task):
    response = home_test_client.post(f"/task/setUndone/{task.id}",
                                     data={"task_id": task.id,
                                           "session": session})
    assert response.status_code == 303
    task_ex = by_id(session, task.id)
    assert task_ex.is_done is False