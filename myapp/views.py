from django.db.models.sql.datastructures import Join
from django.db.models.fields.related import ForeignObject
from django.db.models.options import Options

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from myapp.models import Record, Customer


@api_view(["GET"])
def get_join(request: Request) -> Response:
  # ForeignObjectのtoに結合したいテーブルを指定
  fo = ForeignObject(
    to=Customer,
    on_delete=lambda: x,
    from_fields=[None],
    to_fields=[None],
    rel=None,
    related_name=None
  )

  # 結合処理
  fo.opts = Options(Record._meta)
  fo.opts.model = Record
  fo.get_joining_columns = lambda: (("phone_number", "phone_number"), )

  jo = Join(
    table_name=Customer._meta.db_table,
    parent_alias=Record._meta.db_table,
    table_alias="T1",
    join_type="LEFT JOIN",
    join_field=fo,
    nullable=False # 結合したカラムがNullの時にレコードを削除するか
  )

  # phone_numberが0から始まるレコードを抽出（objects.allだと何故か動かない）
  q = Record.objects.filter(phone_number__startswith="0")

  q.query.join(jo)

  q = q.extra(
    select={
      "customer_name": "myapp_customer.customer_name",
    }
  ).values(
    "id", "phone_number", "customer_name" 
  )

  res = [
    {
      "id": r["id"],
      "phone_number": r["phone_number"],
      "customer_name": r["customer_name"],
    }
    for r in q
  ]

  return Response(res)


@api_view(["GET"])
def get_raw_query(request: Request) -> Response:
  rec = Record.objects.raw("""
    SELECT
      r.id AS id,
      r.phone_number AS phone_number,
      c.customer_name AS customer_name
    FROM
      myapp_record AS r
    LEFT OUTER JOIN
      myapp_customer AS C
    ON r.phone_number = c.phone_number
    WHERE
      r.phone_number LIKE "0%"
  """)

  res = [
    {
      "id": r.id,
      "phone_number": r.phone_number,
      "customer_name": r.customer_name
    }
    for r in rec
  ]

  return Response(res)
  