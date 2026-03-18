from render_sdk import Workflows

app = Workflows()

@app.task(
  plan="pro_ultra" 
)
def capitalize(s: str) -> str:
  return s.upper()
