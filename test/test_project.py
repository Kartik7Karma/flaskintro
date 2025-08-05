from flaskintro import create_app, db

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_task(client):
    response = client.post('/', data={'content': 'Test task'}, follow_redirects=True)
    assert b'Test task' in response.data  # Should appear on the homepage

# from app import Todo

# def test_task_saved(app):
#     with app.app_context():
#         task = Todo.query.filter_by(content='Test task').first()
#         assert task is not None
from flaskintro.models import Todo, db

def test_task_saved(app):
    with app.app_context():
        db.session.add(Todo(content='Test task'))
        db.session.commit()

        assert Todo.query.filter_by(content='Test task').first() is not None

def test_update_task(client, app):
    with app.app_context():
        task = Todo(content="Old Task")
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.post(f'/update/{task_id}', data={'content': 'Updated Task'}, follow_redirects=True)
    assert b'Updated Task' in response.data


def test_delete_task(client, app):
    with app.app_context():
        task = Todo(content="Task to delete")
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.get(f'/delete/{task_id}', follow_redirects=True)
    assert b'Task to delete' not in response.data


def test_empty_task_validation(client):
    response = client.post('/', data={'content': '   '}, follow_redirects=True)
    assert b'Task cannot be empty' in response.data
