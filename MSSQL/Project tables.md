
table names
attribute names
datatypes
primary keys
foreign keys/relationships

Employees
Customers
Sales
Inventory

20 active and 5 former employees
6 customers
3 sales orders per customer each year
inventory of items for sale, and used to build products

script

Questions:
5 best customers
	need to sum for each customer id in the Sales table
which year sold most coops
	max value of sum per year in sales table
items in inventory in need of reorder
	add columns to inventory:
	StockLevel
	ReorderLevel
	StockOnORder
most expensive item in inventory
	WholeSaleCost
	RetailPrice (null for supplies)
most expensive item sold
	max Retail Price
names of employees in design
	simple query of employees
former employees, when released
	simple query
best and worst selling item
	max and min of count of sales
		[separate table for Sales and SalesOrderLine?
]



### Example Database tables
Customer

CustomerID
CompanyName
CustFirstName
CustLastName
CustTitle
Address
City
State
PostalCode
Phone
EmailAddr


Employee
EmployeeID
LastName
FirstName
JobTitle
StreetAddress
City
State
PostalCode
HomePhone
SetupAllowed
HireDate
ReleaseDate
Type
TempService
LockerNumber
BirthDate
EmailAddr
SalaryWage

Shipper
ShipperID
ShipperName
ContactName
Phone
EmailAddr
Fax
MaxPackageWeight
FrieghtPerLb

Supplier
SupplierID
etc

CustOrder
OrderID
CustomerID
OrderDate
RequiredDate

CustOrderLine
OrderID
PartNumber
UnitPrice
OrderQuantity
Discount
Status

Inventory Part
PartNumber
PartDescription
CategoryID
StockPrice
ReorderLevel
StockLevel
StockOnOrder
Weight

PurchaseOrder
PurchOrderID
SupplierID
EmployeeID
DateOrdered
DateDelivered
PaidInFull

Shipment
ShipmentID
OrderID
ShipperID
ShipName
ShipAddress
ShipCity
ShipState
ShipPostalCode

PackingSlip
ShipmentID
PackageNumber
EmployeeID
ShippedDate

ShippedItem
OrderID
PartNumber
ShipmentID
PackageNumber
QuantityShipped

