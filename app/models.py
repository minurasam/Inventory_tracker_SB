from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Association Table for Order and Product (Many-to-Many)
order_products = Table('order_products', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.order_id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.product_id'), primary_key=True),
    Column('quantity_ordered', Integer)
)

class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String)
    supplier_email = Column(String)
    supplier_contact = Column(String)
    supplier_address = Column(String)
    products = relationship("Product", back_populates="supplier")

    # def __repr__(self):
    #     return f"<Supplier(supplier_id={self.supplier_id}, supplier_name='{self.supplier_name}')>"

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    stock_id = Column(Integer, ForeignKey('stock.stock_id'))  
    product_name = Column(String)
    product_description = Column(String)
    product_price = Column(Numeric(10, 2))  # Precision 10, 2 decimal places
    product_quantity = Column(Integer)
    product_category = Column(String)

    supplier = relationship("Supplier", back_populates="products")
    stock_entries = relationship("Stock", back_populates="product") # Relationship to Stock
    # orders = relationship("Order", secondary=order_products, back_populates="products") # M2M with Order

    # def __repr__(self):
    #     return f"<Product(product_id={self.product_id}, product_name='{self.product_name}')>"

class Stock(Base):
    __tablename__ = 'stock'

    stock_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    warehouse_id = Column(Integer, ForeignKey('warehouse.warehouse_id'))  # Prospective FK
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))  # Prospective FK
    product_warehouse_stock_amount = Column(Integer)
    total_products = Column(Integer)

    product = relationship("Product", back_populates="stock_entries")
    employee = relationship("Employee", back_populates="stock_managed_entries")
    warehouse = relationship("Warehouse", back_populates="stock_items") # Relationship to Warehouse

    # def __repr__(self):
    #     return f"<Stock(stock_id={self.stock_id}, product_id={self.product_id}, product_warehouse_stock_amount={self.product_warehouse_stock_amount})>"

class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_role = Column(String)

    stock_managed_entries = relationship("Stock", back_populates="employee")

    # def __repr__(self):
    #     return f"<Employee(employee_id={self.employee_id}, employee_name='{self.employee_name}')>"

class Warehouse(Base):
    __tablename__ = 'warehouse'

    warehouse_id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.stock_id')) # As per ERD
    warehouse_location = Column(String)
    warehouse_capacity = Column(Integer)
    warehouse_contact = Column(String)
    warehouse_manager_name = Column(String)

    stock_items = relationship("Stock", back_populates="warehouse")
    shipments = relationship("Shipment", back_populates="warehouse") # One Warehouse to Many Shipments

    # def __repr__(self):
    #     return f"<Warehouse(warehouse_id={self.warehouse_id}, warehouse_location='{self.warehouse_location}')>"

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))  # Prospective FK
    order_date = Column(DateTime)
    order_quantity = Column(Integer) # Total items in order, as per ERD

    # products = relationship("Product", secondary=order_products, back_populates="orders")
    customer = relationship("Customer", back_populates="orders") # Relationship to Customer
    shipments = relationship("Shipment", back_populates="order") # One Order to Many Shipments

    # def __repr__(self):
    #     return f"<Order(order_id={self.order_id}, order_date={self.order_date})>"

class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_contact = Column(String)

    orders = relationship("Order", back_populates="customer") # One Customer to Many Orders

    # def __repr__(self):
    #     return f"<Customer(customer_id={self.customer_id}, customer_name='{self.customer_name}')>"

class Shipment(Base):
    __tablename__ = 'shipments'

    shipment_id = Column(Integer, primary_key=True)
    warehouse_id = Column(Integer, ForeignKey('warehouse.warehouse_id'))
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    shipment_date = Column(DateTime)
    shipment_status = Column(String)

    warehouse = relationship("Warehouse", back_populates="shipments")
    order = relationship("Order", back_populates="shipments")

    # def __repr__(self):
    #     return f"<Shipment(shipment_id={self.shipment_id}, status='{self.shipment_status}')>"

