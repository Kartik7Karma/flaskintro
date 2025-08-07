from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import Todo, db
from flask import jsonify

main = Blueprint('main', __name__)

# --------------------
# HTML Interface Routes
# --------------------

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return handle_add_task()
    return render_task_list()

def handle_add_task():
    task_content = request.form.get('content', '').strip()
    if not task_content:
        flash("Task cannot be empty.", "error")
        return redirect(url_for('main.index'))

    new_task = Todo(content=task_content)
    try:
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"There was an error adding your task: {e}", "error")
    return redirect(url_for('main.index'))

def render_task_list():
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)

@main.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash("Task deleted.", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting task: {e}", "error")
    return redirect(url_for('main.index'))


@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        return handle_update_task(task)
    return render_template('update.html', task=task)

def handle_update_task(task):
    new_content = request.form.get('content', '').strip()
    if new_content == task.content:
        flash("No changes were made.", "info")
        return redirect(url_for('main.index'))

    if not new_content:
        flash("Task content cannot be empty.", "error")
        return redirect(url_for('main.update', id=task.id))

    task.content = new_content
    try:
        db.session.commit()
        flash("Task updated successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error updating task: {e}", "error")
    return redirect(url_for('main.index'))

@main.route('/api/tasks', methods=['GET'])
def api_list_tasks():
    try:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return jsonify([{"id": t.id, "content": t.content} for t in tasks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
