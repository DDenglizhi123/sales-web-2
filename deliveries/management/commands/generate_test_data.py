from django.core.management.base import BaseCommand
from datetime import date, timedelta
from decimal import Decimal
import random

from customers.models import Customer
from products.models import Products
from orders.models import Order, OrderItem
from deliveries.models import Delivery, DeliveryItem


class Command(BaseCommand):
    help = '清空数据库并生成测试数据'

    def handle(self, *args, **options):
        self.stdout.write("=" * 50)
        self.stdout.write(self.style.SUCCESS("开始生成测试数据"))
        self.stdout.write("=" * 50)
        
        # 清空数据
        self.clear_all_data()
        
        # 生成数据
        customers = self.generate_customers()
        products = self.generate_products()
        orders = self.generate_orders(customers, products)
        deliveries = self.generate_deliveries(orders)
        
        self.stdout.write("=" * 50)
        self.stdout.write(self.style.SUCCESS("测试数据生成完成！"))
        self.stdout.write("=" * 50)
        self.stdout.write(f"客户数量: {Customer.objects.count()}")
        self.stdout.write(f"产品数量: {Products.objects.count()}")
        self.stdout.write(f"订单数量: {Order.objects.count()}")
        self.stdout.write(f"订单项数量: {OrderItem.objects.count()}")
        self.stdout.write(f"发货单数量: {Delivery.objects.count()}")
        self.stdout.write(f"发货项数量: {DeliveryItem.objects.count()}")
        self.stdout.write("=" * 50)

    def clear_all_data(self):
        """清空所有数据"""
        self.stdout.write("正在清空数据库...")
        DeliveryItem.objects.all().delete()
        Delivery.objects.all().delete()
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        Products.objects.all().delete()
        Customer.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("数据库已清空"))

    def generate_customers(self):
        """生成客户数据"""
        self.stdout.write("正在生成客户数据...")
        customers_data = [
            {
                'name': 'STEG Construction Ltd',
                'name_in_short': 'STEG',
                'TIN': '123-456-789',
                'VRN': '12-345678-9',
                'contact_person': 'John Smith',
                'phone': '255712345678',
                'emial': 'contact@steg.co.tz',
                'address_line1': '123 Main Street',
                'address_line2': 'Dar es Salaam',
                'business_type': 'REA'
            },
            {
                'name': 'TANESCO Government',
                'name_in_short': 'TANESCO',
                'TIN': '234-567-890',
                'VRN': '23-456789-0',
                'contact_person': 'Mary Johnson',
                'phone': '255712345679',
                'emial': 'info@tanesco.go.tz',
                'address_line1': '456 Government Road',
                'address_line2': 'Dodoma',
                'business_type': 'GOV'
            },
            {
                'name': 'ABC Trading Company',
                'name_in_short': 'ABC',
                'TIN': '345-678-901',
                'VRN': '34-567890-1',
                'contact_person': 'David Brown',
                'phone': '255712345680',
                'emial': 'sales@abc.co.tz',
                'address_line1': '789 Business Avenue',
                'address_line2': 'Arusha',
                'business_type': 'OTH'
            },
            {
                'name': 'XYZ Engineering',
                'name_in_short': 'XYZ',
                'TIN': '456-789-012',
                'VRN': '45-678901-2',
                'contact_person': 'Sarah Wilson',
                'phone': '255712345681',
                'emial': 'info@xyz.co.tz',
                'address_line1': '321 Industrial Zone',
                'address_line2': 'Mwanza',
                'business_type': 'REA'
            },
            {
                'name': 'Green Energy Solutions',
                'name_in_short': 'GES',
                'TIN': '567-890-123',
                'VRN': '56-789012-3',
                'contact_person': 'Michael Green',
                'phone': '255712345682',
                'emial': 'contact@ges.co.tz',
                'address_line1': '654 Eco Street',
                'address_line2': 'Zanzibar',
                'business_type': 'OTH'
            }
        ]
        
        customers = []
        for data in customers_data:
            customer = Customer.objects.create(**data)
            customers.append(customer)
            self.stdout.write(f"  创建客户: {customer.name}")
        
        return customers

    def generate_products(self):
        """生成产品数据"""
        self.stdout.write("正在生成产品数据...")
        products_data = [
            {'item_name': 'Cable 2.5mm²', 'base_price': Decimal('1500.00'), 'unit': 'M', 'stock_quantity': '5000'},
            {'item_name': 'Cable 4mm²', 'base_price': Decimal('2500.00'), 'unit': 'M', 'stock_quantity': '3000'},
            {'item_name': 'Cable 6mm²', 'base_price': Decimal('3500.00'), 'unit': 'M', 'stock_quantity': '2000'},
            {'item_name': 'Cable 10mm²', 'base_price': Decimal('5500.00'), 'unit': 'M', 'stock_quantity': '1500'},
            {'item_name': 'Cable 16mm²', 'base_price': Decimal('8500.00'), 'unit': 'M', 'stock_quantity': '1000'},
            {'item_name': 'Cable 25mm²', 'base_price': Decimal('12000.00'), 'unit': 'M', 'stock_quantity': '800'},
            {'item_name': 'Switch 20A', 'base_price': Decimal('5000.00'), 'unit': 'PC', 'stock_quantity': '500'},
            {'item_name': 'Switch 32A', 'base_price': Decimal('7500.00'), 'unit': 'PC', 'stock_quantity': '300'},
            {'item_name': 'MCB 20A', 'base_price': Decimal('8000.00'), 'unit': 'PC', 'stock_quantity': '400'},
            {'item_name': 'MCB 32A', 'base_price': Decimal('12000.00'), 'unit': 'PC', 'stock_quantity': '250'},
            {'item_name': 'Conduit Pipe 20mm', 'base_price': Decimal('2000.00'), 'unit': 'M', 'stock_quantity': '2000'},
            {'item_name': 'Conduit Pipe 25mm', 'base_price': Decimal('2500.00'), 'unit': 'M', 'stock_quantity': '1500'},
            {'item_name': 'Cable Tray', 'base_price': Decimal('15000.00'), 'unit': 'M', 'stock_quantity': '500'},
            {'item_name': 'Distribution Board', 'base_price': Decimal('50000.00'), 'unit': 'PC', 'stock_quantity': '100'},
            {'item_name': 'Earthing Rod', 'base_price': Decimal('3000.00'), 'unit': 'PC', 'stock_quantity': '300'},
        ]
        
        products = []
        for data in products_data:
            product = Products.objects.create(**data)
            products.append(product)
            self.stdout.write(f"  创建产品: {product.item_name}")
        
        return products

    def generate_orders(self, customers, products):
        """生成订单数据"""
        self.stdout.write("正在生成订单数据...")
        orders = []
        
        # 生成5个订单
        for i in range(5):
            customer = random.choice(customers)
            order_number = f'ORD{str(i+1).zfill(6)}'
            order = Order.objects.create(
                order_number=order_number,
                customer=customer
            )
            orders.append(order)
            self.stdout.write(f"  创建订单: {order_number} - 客户: {customer.name}")
            
            # 为每个订单添加2-4个订单项
            num_items = random.randint(2, 4)
            selected_products = random.sample(products, min(num_items, len(products)))
            
            for product in selected_products:
                quantity = random.randint(10, 100)
                # 单价可能略有浮动（±10%）
                price_multiplier = Decimal(str(random.uniform(0.9, 1.1)))
                unit_price = product.base_price * price_multiplier
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    unit_price=unit_price
                )
                self.stdout.write(f"    添加订单项: {product.item_name} x {quantity} @ {unit_price}")
        
        return orders

    def generate_deliveries(self, orders):
        """生成发货单数据"""
        self.stdout.write("正在生成发货单数据...")
        deliveries = []
        
        # 为前3个订单创建发货单
        for i, order in enumerate(orders[:3]):
            delivery_date = date.today() - timedelta(days=random.randint(0, 30))
            
            # 第一个发货单：已填写发货单号
            # 第二个发货单：未填写发货单号
            # 第三个发货单：已填写发货单号
            if i == 0:
                delivery_number = f'DEL{str(i+1).zfill(6)}'
                status = 'DELIVERED'
            elif i == 1:
                delivery_number = None
                status = 'DELIVERED'
            else:
                delivery_number = f'DEL{str(i+1).zfill(6)}'
                status = 'IN_TRANSIT'
            
            delivery = Delivery.objects.create(
                delivery_number=delivery_number,
                order=order,
                customer=order.customer,
                delivery_date=delivery_date,
                vehicle_number=f'T{random.randint(100, 999)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}',
                driver_phone=f'2557{random.randint(10000000, 99999999)}',
                driver_name=random.choice(['John Driver', 'Mary Driver', 'David Driver', None]),
                status=status
            )
            deliveries.append(delivery)
            self.stdout.write(f"  创建发货单: {delivery_number or '未填写'} - 订单: {order.order_number}")
            
            # 为发货单添加发货项
            order_items = order.ordered.all()
            for order_item in order_items:
                # 发货数量为订单数量的部分（50%-100%）
                delivered_quantity = random.randint(
                    int(order_item.quantity * 0.5),
                    order_item.quantity
                )
                
                DeliveryItem.objects.create(
                    delivery=delivery,
                    order_item=order_item,
                    delivered_quantity=delivered_quantity
                )
                self.stdout.write(f"    添加发货项: {order_item.product.item_name} x {delivered_quantity}")
        
        return deliveries

