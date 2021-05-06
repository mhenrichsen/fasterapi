from fastapi import FastAPI
import uvicorn

separator = ', '

app = FastAPI()


class Endpoint:
    def get(self, path, queries, return_function_name):
        queries = separator.join(queries)
        exec(f"""@app.get("{path}")
async def end({queries}): return {return_function_name}({queries})""")


end = Endpoint()


def plus(a, b):
    return a + b


end.get(path="/hi", queries=['a', 'b'], return_function_name="plus")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
