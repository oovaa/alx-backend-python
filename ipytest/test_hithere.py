
import uuid
from aiohttp import Payload
import requests


ENDPOINT = 'https://todo.pixegami.io'


def test_can_call_end_point():
    res = requests.get(ENDPOINT)
    assert res.status_code == 200


def test_can_create_task():
    payload = {
        "content": "i need to do something",
        "user_id": "test_user",
        "is_done": False
    }
    create_res = create_task(payload)
    assert create_res.status_code == 200
    data = create_res.json()

    task_id = data['task']['task_id']
    task_res = get_task(task_id)
    assert task_res.status_code == 200
    get_task_data = task_res.json()
    assert get_task_data['content'] == 'i need to do something'


def test_can_update_task():
    # create task
    payload = new_payload()
    create_res = create_task(payload)
    assert create_res.status_code == 200

    task_data = create_res.json()
    task_id = task_data['task']['task_id']

    # created
    # get_res = requests.get(ENDPOINT + '/get-task/' + task_id)
    # print(get_res.json())

    # update it
    payload = {
        "content": "my new content",
        "task_id": task_id,
        "user_id": "omarvx",
        "is_done": True
    }

    befor = get_task(task_id).json()

    # assert befor['content']
    update_res = update_task(payload)
    assert update_res.status_code == 200

    updated_id = update_res.json()['updated_task_id']

    updated_task = get_task(updated_id)
    assert updated_task.status_code == 200

    updated_data = updated_task.json()

    assert updated_data['content'] == payload["content"]

    # get it
    # check it


def test_can_list_tasks():
    num = 5
    for _ in range(num):
        Payload = new_payload()
        uid = Payload['user_id']
        print(Payload)
        res_create_task = create_task(Payload)
        assert res_create_task.status_code == 200

    list_tasks_res = list_task(uid)
    assert list_tasks_res.status_code == 200
    list_task_data = list_tasks_res.json()

    print(list_task_data)

    tasks = list_task_data['tasks']
    assert len(tasks) == num


def create_task(payload):
    return requests.put(ENDPOINT + '/create-task', json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + '/get-task/'+task_id)


def list_task(user_id):
    return requests.get(ENDPOINT + '/list-tasks/'+user_id)


def update_task(payload):
    return requests.put(ENDPOINT + '/update-task', json=payload)


def new_payload():
    id = uuid.uuid4().hex
    return {
        "content": "original task" + id,
        "user_id": "omarvx" + id,
        "is_done": True
    }
