from fastapi import FastAPI
app = FastAPI()


# minimal app - get request
@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return{'Ping':'Pong'}


# Get --> Read Todo
@app.get('/todo',tags=['todos'])
async def get_todo() -> dict:
    return{"data": todos}


todos = [
    {
        "id":"1",
        "Activity":"Jogging for 2 hours at 7:00 AM."
    },
    {
        "id":"2",
        "Activity":"Writing 3 pages of my new book at 2:00 PM."
    }
]



# Post --> Create Todo
# Put --> Update Todo
# Delete --> Delete Todo
