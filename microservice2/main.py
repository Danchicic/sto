from fastapi import FastAPI
import uvicorn
app = FastAPI()
items = [{'name': "item1"}]


@app.get("/items")
async def get_items():
    return items

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8120)