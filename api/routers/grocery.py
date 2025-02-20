from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import sqlite3

router = APIRouter(prefix='/grocery', tags=['grocery'])

@router.get('/orders')
def get_orders():
  '''
      Grocery endpoint
      We dont need any arguments
  '''
  try:
    conn = sqlite3.connect('./db.db')
    c = conn.cursor()
    c.execute('select * from orders')
    columns = [desc[0] for desc in c.description]
    orders = [dict(zip(columns, row)) for row in c.fetchall()]
    response = jsonable_encoder(orders)
    return JSONResponse(content={"error": 0, "success": True, "data": response})
    
  except ValueError as e:
    return JSONResponse(content={"error": 1, "success": False, "msg": str(e)})