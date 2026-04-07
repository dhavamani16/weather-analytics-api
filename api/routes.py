from fastapi import APIRouter
import sqlite3
import statistics
router=APIRouter()
@router.get("/weather/month/{month}")
def get_month_connection(month:int):
    conn=sqlite3.connect("weather.db")
    cursor=conn.cursor()
    cursor.execute("""select date,temperature,pressure,humidity,condition from weather where month=?""",(month,)
    )
    data=cursor.fetchall()
    conn.close()
    if not data:
        return {"message": "No data found for the specified month."}
    return {"data": data}