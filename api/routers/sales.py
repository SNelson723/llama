from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import sqlite3
import pandas as pd

router = APIRouter(prefix='/sales', tags=['sales'])

@router.get('/sales')
def get_sales():
  '''
      Sales endpoint
      We dont need any arguments
  '''
  try:
    conn = sqlite3.connect('./db.db')
    c = conn.cursor()
    c.execute('select * from orders')
    columns = [desc[0] for desc in c.description]
    orders = [dict(zip(columns, row)) for row in c.fetchall()]
    response = jsonable_encoder(orders)
    
    df = pd.DataFrame(response)
    
    df['revenue'] = df['price'] * df['quantity']
    df['cost'] = df['cost'] * df['quantity']
    df['gross_profit'] = df['revenue'] - df['cost']
    df['gross_margin'] = (df['gross_profit'] / df['revenue']) * 100
    
    total_revenue = df['revenue'].sum()
    total_cost = df['cost'].sum()
    total_profit = df['gross_profit'].sum()
    overall_margin = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0
    low_margin_items = df[df['gross_margin'] < 20].to_dict(orient='records')
    
    recommendations = []
    if total_profit < 5000:
      recommendations.append('Introduce promotional bundles or discounts on high-margin items to drive volume')
    if overall_margin < 25:
      recommendations.append('Consider adjusting pricing strategies or reducing costs for low margin items')
    if len(low_margin_items) > 0:
      recommendations.append(f'Review {len(low_margin_items)} low margin items for potential cost savings or price increases')
    
    results = {
      'total_revenue': total_revenue,
      'total_cost': total_cost,
      'total_profit': total_profit,
      'overall_gross_margin': f"{overall_margin}%",
      'overall_gross_margin': overall_margin,
      'low_margin_items': low_margin_items,
      'recommendations': recommendations
    }
    response = jsonable_encoder(results)
    
    return JSONResponse(content={"error": 0, "success": True, "results": response})
    
  except ValueError as e:
    return JSONResponse(content={"error": 1, "success": False, "msg": str(e)})