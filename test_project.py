import pytest
from datetime import datetime
from project import add_task, mark_task_completed, get_progress_summary, save_tasks, load_tasks, delete_tasks, tasks

@pytest.fixture
def setup_tasks():
    global tasks
    tasks.clear()
    tasks.extend([
        {"task": "Read book", "frequency": "daily", "end_date": datetime(2024, 11, 10).date(), "completion_status": False},
        {"task": "Exercise", "frequency": "weekly", "end_date": datetime(2024, 12, 1).date(), "completion_status": True},
    ])
    print("Tasks after setup:", tasks)

def test_add_task(setup_tasks, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "Write Code" if "name" in prompt else "daily" if "frequency" in prompt else "2024-12-01")
    assert "✅ Task added successfully 👍" in add_task()

    monkeypatch.setattr("builtins.input", lambda _: "2024/12/01")
    assert "⚠ Invalid date format" in add_task()

def test_mark_task_completed(setup_tasks, monkeypatch):
    global tasks
    print("Tasks before marking completed:", tasks)

    monkeypatch.setattr("builtins.input", lambda _: "Read book")
    assert "✅ Task: Read book completed. Congrats 🎉" in mark_task_completed()

    monkeypatch.setattr("builtins.input", lambda _: "Nonexistent task")
    assert "❌ Task: Nonexistent task not found" in mark_task_completed()

def test_get_progress_summary(setup_tasks):
    global tasks
    print("Tasks during summary check:", tasks)

    summary = get_progress_summary()
    assert "📃 Task: Read book" in summary
    assert "📃 Task: Exercise" in summary

    tasks.clear()
    assert get_progress_summary() == "No tasks found."

def test_save_tasks(setup_tasks, tmp_path):
    temp_file = tmp_path / "temp_tasks.csv"
    save_tasks(temp_file)
    assert temp_file.exists()

def test_load_tasks(tmp_path):
    temp_file = tmp_path / "tasks.csv"
    temp_file.write_text("task,frequency,end_date,completion_status\nRead book,daily,2024-11-10,False\n")
    load_tasks(temp_file)
    assert len(tasks) > 0
    assert tasks[0]["task"] == "Read book"

def test_delete_tasks(setup_tasks, monkeypatch):
    global tasks
    print("Tasks before deletion:", tasks)

    monkeypatch.setattr("builtins.input", lambda _: "Read book")
    assert "Task: Read book has been deleted" in delete_tasks()

    monkeypatch.setattr("builtins.input", lambda _: "Nonexistent task")
    assert "Task: Nonexistent task not found" in delete_tasks()
