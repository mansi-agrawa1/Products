from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from openpyxl import Workbook



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        quantity = self.request.query_params.get('quantity')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if quantity:
            qs = qs.filter(quantity=quantity)
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)

        return qs



def export_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    c = canvas.Canvas(response)
    y = 800
    c.drawString(100, y, "Inventory Report")
    products = Product.objects.all()
    for item in products:
        text = f"ID: {item.id}, Name: {item.name}, Qty: {item.quantity}, Price: {item.price}, Created: {item.created_at.strftime('%Y-%m-%d')}"
        y -= 20
        c.drawString(100, y, text)
        if y < 50:
            c.showPage()
            y = 800

    c.save()
    return response



def export_to_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Items Report"

    ws.append(["ID", "Name", "Quantity", "Price", "Created At"])

    items = Product.objects.all()
    for item in items:
        ws.append([
            item.id,
            item.name,
            item.quantity,
            float(item.price),
            item.created_at.strftime('%Y-%m-%d')
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=items_report.xlsx'

    wb.save(response)
    return response
