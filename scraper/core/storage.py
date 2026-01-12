import aiosqlite

async def init_db():
    db = await aiosqlite.connect("data.db")
    await db.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            url TEXT PRIMARY KEY,
            content TEXT
        )
    """)
    await db.commit()
    return db

