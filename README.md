# Todos DDD Example
An example todos app with DDD approach

## References
- http://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
- https://hackernoon.com/making-a-case-for-domain-modeling-17cf47030732
- https://medium.com/swlh/creating-coding-excellence-with-domain-driven-design-88f73d2232c3
- https://www.javacodegeeks.com/2016/10/architectural-layers-modeling-domain-logic.html
- https://www.alibabacloud.com/blog/handling-complex-business-scenarios-with-domain-modeling-%E2%80%93-part-1_593863?spm=a2c65.11461447.0.0.acc85f82jfZ0Us

# Domain Modeling Iteration

## Round 1

### User stories
- User will be logged in by providing a username (no need password, no need to register)
- User could manage one ore more todo task items
- Each task's state could be as follow: new -> doing -> done
- To stay focused, user could only have 3 doing tasks at a time.
But if he has finished at least 3 tasks in his lifetime usage,
he could have up to 5 concurrent doing tasks
- User could delete/remove any task in the list
- No need to manage task creation time

### Domain model
![](https://www.plantuml.com/plantuml/img/VP7DQm8n4CNl-Ik6FIcqYxqMAPRsua4fs9vbJ4Otc9r8CelQZ_-zIVgrKZ6tUVFUuvTa4WM3TArJAcujxp1W2zfXZFSYmQuweQdslB2l1AEU9JPe_Dxo1jRe8YbLCl0IAS2RWdGMAPxMNL8OMohQb0N42xgbyMcv58pRVmkcB_tZf_GvJQUbrlGdGr7tvtGbeHotB1JMgAbKp91nGosnF7bdzV6xSkMz0tJEx-TqaCVCbTs333xyWvZXuS6pxa8WriTVsqbLkKKJA3RUcHmjpr7TL70DrQYkkIeWjz0Mb0XtQf0jLqKUmhYkpv8gTPP__9xy5xcKcX2RzBkV)

### SQLite repository
![](https://www.plantuml.com/plantuml/img/TS-n2i9030RWFK-HkT0-W9JIoSN5GHyWU56FzbAvf8YqlhkzKpi8Rk7d8t_Igb6qCVG0sdcvKQI0UYKttBrSy4ozCW2BUNlWKJdY18W5Ziie57Y3QZ79kjxlcWQUApwGTX_itIz3BCj_UxPlKA1ZFNtp72otsYfJLJvedgjgc78Vj2mkFVC2)

## Round 2

### REST endpoints with Flask

1. Get all tasks of user
```
GET /tasks

Request
--------
Header::Authorization: Bearer <username>

Response
--------
[
    { "taskid": "abc...", "description": "...", "status": "..." },
    { "taskid": "xyz...", "description": "...", "status": "..." }
]

```

2. Add task
```
POST /tasks

Request
-------
Header::Authorization: Bearer <username>
Header::Content-Type: application/json
Body: {
    "description": "new task"
}
```

3. Update task status
```
PUT /tasks/<task_id>/status

Request
-------
Header::Authorization: Bearer <username>
Header::Content-Type: application/json
Body: {
    "status": 1  # 1: doing; 2: done
}
```