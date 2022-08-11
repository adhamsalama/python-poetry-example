from fastapi import APIRouter
from rest_api.models.todo import TODO
from pydantic import Field
from rest_api.utils.generate_random_id import generate_random_id

router: APIRouter = APIRouter()

todos: list[dict[str, TODO]] = []


@router.get("")
def get_all():
    return todos


@router.post("")
def add_todo(todo: TODO):
    todo_id = generate_random_id()
    todos.append({todo_id: todo})
    return todos[-1]


@router.delete("/{todo_id}")
def delete_todo(todo_id: str = Field(min_length=10, max_length=10)):
    for i in range(len(todos)):
        todo = todos[i]
        current_id = list(todo.keys())[0]
        if current_id == todo_id:
            deleted = todo
            del todos[i]
            return deleted
    return None


@router.put("/{todo_id}")
def update_todo(updated_todo: TODO, todo_id: str = Field(max_length=10, min_length=10)):
    for todo in todos:
        current_id = list(todo.keys())[0]
        if current_id == todo_id:
            todo[todo_id] = updated_todo
            return todo
    return None
