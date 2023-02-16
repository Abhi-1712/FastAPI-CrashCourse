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
@app.post("/todo",tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data":"A todo has been added! "
    }


# Put --> Update Todo
@app.put("/todo/{id}",tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            return{
                "data":f"Todo with id:{id} has been updated"
            }
    return{
            "data":f"Todo with id:{id} not found!"
    }    
        



# Delete --> Delete Todo
