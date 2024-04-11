import pytest
from lib.task_tracker import *

def test_initially_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

def test_task_tracker_adds_and_marks_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the frog"]

def test_task_tracker_mark_task_incorrect_index():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(1)
    assert str(e.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]
    
        

