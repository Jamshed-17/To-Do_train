import aiosqlite


async def get_all():
    async with aiosqlite.connect("persistence/app.db") as db:
        async with db.execute("SELECT * FROM tasks;") as cursor:
            data = await cursor.fetchall()
            list = []
            for i in data:
                list.append({"id": i[0], "name": i[1]})
            return list

async def insert( task_name: str):
    async with aiosqlite.connect("persistence/app.db") as db:
        await db.execute(f"INSERT INTO tasks (name) VALUES ('{task_name}');")
        await db.commit()


async def remove(task_id: int):
    async with aiosqlite.connect("persistence/app.db") as db:
        async with db.execute(f"SELECT id FROM tasks WHERE id = {task_id}") as cursor:
            data = await cursor.fetchone()
            if data is None:
                return {"Error": "Task not found"}
        await db.execute(f"DELETE FROM tasks WHERE id = {task_id}")
        await db.commit()
