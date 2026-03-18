from render_sdk import Workflows

app = Workflows()

@app.task(
  plan="pro_ultra" 
)
def add(a: int, b: int) -> int:
  return a + b
