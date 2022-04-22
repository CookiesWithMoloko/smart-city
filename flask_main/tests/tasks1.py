from models.task import Task

t = Task.query.all()[0].as_dict()
print(t)
assert isinstance(t, dict)
