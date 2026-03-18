from render_sdk import Workflows

app = Workflows()

@app.task(
  plan="pro_max" 
)
def capitalize(s: str) -> str:
  return s.upper()
