from render_sdk import Workflows

app = Workflows()

@app.task
def add(a: int, b: int) -> int:
  return a + b
