from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

# Path to the current directory (where both HTML and Python files are stored)
current_dir = os.getcwd()
data_folder = current_dir+'\data'
# Path to the JSON file
employee_file_path = os.path.join(data_folder, 'employees.json')
customer_file_path = os.path.join(data_folder, 'customers.json')
vendor_file_path = os.path.join(data_folder,'vendors.json')
balance_sheet_path = os.path.join(data_folder,'balance_sheet.json')
income_statement_path = os.path.join(data_folder,'income_statement.json')
payroll_history_path = os.path.join(data_folder,'payroll_history.json')
invoice_history_path = os.path.join(data_folder,'invoice_history.json')
PO_history_path = os.path.join(data_folder,'PO_history.json')
federal_tax_bracket_path = os.path.join(data_folder,'federal_tax_bracket.json')
inventory_path = os.path.join(data_folder,'inventory.json')
# parts_index_path = os.path.join(data_folder,'parts_index.json')
state_tax_rate = 0.0495 #for illinois
social_security_tax_rate = 0.062
medical_tax_rate = 0.0145
cog_unit = 0.57 #according to units needed per truck for part 2


# print(employee_file_path)

def federal_tax_calc(income):
    if os.path.exists(federal_tax_bracket_path):
        with open(federal_tax_bracket_path,'r') as file:
            bracket = json.load(file)
    else:
        bracket = []
        return 0

    if(income<0):
        print("invalid income! income must be no less than 0!\n")
        return 0

    for rg in bracket:
        if(rg['lowerBound']<=income and rg['upperBound']>=income):
            return income*rg['rate']
    return income*bracket[-1]['rate']

# Route to serve the index.html file at the root URL
@app.route('/')
def serve_index():
    return send_from_directory(current_dir,"index.html")




# Route to handle saving employee data to a JSON file
@app.route('/add_employee', methods=['POST'])
def add_employee():
    # Get the new employee data from the request
    new_employee = request.get_json()
    # print(new_employee)

    # Check if the JSON file exists, if not create it
    if os.path.exists(employee_file_path):
        # If the file exists, load the current data
        with open(employee_file_path, 'r') as file:
            employees = json.load(file)
    else:
        # If the file doesn't exist, create an empty list
        employees = []

    # Add the new employee to the list
    employees.append(new_employee)

    # Save the updated employee list back to the file
    with open(employee_file_path, 'w') as file:
        json.dump(employees, file, indent=4)

    # Return a success message as JSON
    return jsonify({"message": "Employee added successfully!"})

@app.route('/add_customer', methods=['POST'])
def add_customer():
    # Get the new employee data from the request
    new_customer = request.get_json()

    # Check if the JSON file exists, if not create it
    if os.path.exists(customer_file_path):
        # If the file exists, load the current data
        with open(customer_file_path, 'r') as file:
            customers = json.load(file)
    else:
        # If the file doesn't exist, create an empty list
        customers = []

    # Add the new employee to the list
    customers.append(new_customer)

    # Save the updated employee list back to the file
    with open(customer_file_path, 'w') as file:
        json.dump(customers, file, indent=4)

    # Return a success message as JSON
    return jsonify({"message": "Customer added successfully!"})

# Route to serve other static files (like CSS or JS)
# def serve_view_employee():
#     return send_from_directory(current_dir, 'view_employee.html')

# Route to fetch employee data (GET request)
@app.route('/add_vendor', methods=['POST'])
def add_vendor():

    new_vendor = request.get_json()

    # Check if the JSON file exists, if not create it
    if os.path.exists(vendor_file_path):
        # If the file exists, load the current data
        with open(vendor_file_path, 'r') as file:
            vendors = json.load(file)
    else:
        # If the file doesn't exist, create an empty list
        vendors = []


    vendors.append(new_vendor)


    with open(vendor_file_path, 'w') as file:
        json.dump(vendors, file, indent=4)

    # Return a success message as JSON
    return jsonify({"message": "Vendor added successfully!"})




@app.route('/get_employees', methods=['GET'])
def get_employees():
    if os.path.exists(employee_file_path):
        with open(employee_file_path, 'r') as file:
            employees = json.load(file)
    else:
        employees = []
    return jsonify(employees)

@app.route('/get_customers', methods=['GET'])
def get_customers():
    if os.path.exists(customer_file_path):
        with open(customer_file_path, 'r') as file:
            customers = json.load(file)
    else:
        customers = []
    # print(customers)
    return jsonify(customers)


@app.route('/get_vendors', methods=['GET'])
def get_vendors():
    if os.path.exists(vendor_file_path):
        with open(vendor_file_path, 'r') as file:
            vendors = json.load(file)
    else:
        vendors = []
    # print(vendors)
    return jsonify(vendors)

@app.route('/get_balance_sheet',methods=['GET'])
def get_balance_sheet():
    if os.path.exists(balance_sheet_path):
        with open(balance_sheet_path,'r') as file:
            balance_sheet = json.load(file)
    else:
        balance_sheet = []
    return jsonify(balance_sheet)

@app.route('/get_income_statement',methods=['GET'])
def get_income_statement():
    if os.path.exists(income_statement_path):
        with open(income_statement_path,'r') as file:
            income_statement = json.load(file)
    else:
        income_statement = []
    return jsonify(income_statement)


@app.route('/get_payrolls',methods=['GET'])
def get_payrolls():
    if os.path.exists(payroll_history_path):
        with open(payroll_history_path,'r') as file:
            payroll = json.load(file)
    else:
        payroll = []
    return jsonify(payroll)

@app.route('/get_invoices',methods=['GET'])
def get_invoices():
    if os.path.exists(invoice_history_path):
        with open(invoice_history_path,'r') as file:
            invoice = json.load(file)
    else:
        invoice = []
    # print(invoice)
    return jsonify(invoice)

@app.route('/get_POs',methods=['GET'])
def get_POs():
    if os.path.exists(PO_history_path):
        with open(PO_history_path,'r') as file:
            POs = json.load(file)
    else:
        POs = []
    return jsonify(POs)

@app.route('/get_inventories',methods=['GET'])
def get_inventories():
    if os.path.exists(inventory_path):
        with open(inventory_path,'r') as file:
            inventories = json.load(file)
            # print("inventories={}".format(inventories))
            ret_inventory = []
            for _key in inventories.keys():
                if(type(inventories[_key])==int or type(inventories[_key])==float): continue
                ret_inventory.append(inventories[_key])
                ret_inventory[-1]['part'] = _key
        return jsonify(ret_inventory)
    else:
        inventories = []
    return jsonify(inventories)

@app.route('/get_completed_unit',methods=['GET'])
def get_completed_stocks():
    if os.path.exists(inventory_path):
        with open(inventory_path,'r') as file:
            inventories = json.load(file)
        return str(inventories['completed_unit'])
    else:
        return "0"


# Route to delete an employee (DELETE request)
@app.route('/delete_employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    if os.path.exists(employee_file_path):
        with open(employee_file_path, 'r') as file:
            employees = json.load(file)
    else:
        return jsonify({"message": "No employee found"}), 404

    # Find and remove the employee with the matching ID
    employees = [emp for emp in employees if emp['id'] != id]

    # Save the updated list back to the file
    with open(employee_file_path, 'w') as file:
        json.dump(employees, file, indent=4)

    return jsonify({"message": "Employee deleted successfully!"})

@app.route('/delete_customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    if os.path.exists(customer_file_path):
        with open(customer_file_path, 'r') as file:
            customers = json.load(file)
    else:
        return jsonify({"message": "No customer found"}), 404

    # Find and remove the employee with the matching ID
    customers = [cus for cus in customers if cus['id'] != id]

    # Save the updated list back to the file
    with open(customer_file_path, 'w') as file:
        json.dump(customers, file, indent=4)

    return jsonify({"message": "Customer deleted successfully!"})


@app.route('/delete_vendor/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    if os.path.exists(vendor_file_path):
        with open(vendor_file_path, 'r') as file:
            vendors = json.load(file)
    else:
        return jsonify({"message": "No vendor found"}), 404

    # Find and remove the employee with the matching ID
    vendors = [ven for ven in vendors if ven['id'] != id]

    # Save the updated list back to the file
    with open(vendor_file_path, 'w') as file:
        json.dump(vendors, file, indent=4)

    return jsonify({"message": "Vendor deleted successfully!"})

@app.route('/pay_employee/<int:id>', methods=['POST'])
def pay_employee(id):
    # print("start paying\n")
    # Get the new employee data from the request

    # Check if the JSON file exists, if not create it
    if os.path.exists(balance_sheet_path):
        # If the file exists, load the current data
        with open(balance_sheet_path, 'r') as file:
            balance_sheet = json.load(file)
    else:
        print("error! No balance sheet file!\n")
        return jsonify({"message":"Balance Sheet update failed!"})

    if os.path.exists(income_statement_path):
        # If the file exists, load the current data
        with open(income_statement_path, 'r') as file:
            income_statement = json.load(file)
    else:
        print("error! No income statement file!\n")
        return jsonify({"message":"Income Statement update failed!"})

    if os.path.exists(employee_file_path):
        # If the file exists, load the current data
        with open(employee_file_path, 'r') as file:
            employee = json.load(file)
    else:
        print("error! No Employee file!\n")
        return jsonify({"message":"Employee retrieving failed!"})

    if os.path.exists(payroll_history_path):
        # If the file exists, load the current data
        with open(payroll_history_path, 'r') as file:
            payroll_hist = json.load(file)
    else:
        # If the file doesn't exist, create an empty list
        payroll_hist = []

    new_payroll = dict()
    payroll_hist.append(new_payroll)


    emp_order = 1000
    for _i in range(len(employee)):
        if(employee[_i]['id']==id):
            emp_order = _i
            break
    salary = float(employee[emp_order]['salary'])
    withold = 0 if len(employee[emp_order]['witholdings'])==0 else float(employee[emp_order]['witholdings'])
    all_taxes = federal_tax_calc(salary)+salary*(state_tax_rate+social_security_tax_rate+medical_tax_rate)+withold
    total_pay = salary+all_taxes
    minus_asset,plus_debt = salary,0

    balance_sheet['assets']['cash'] -= total_pay
    if(balance_sheet['assets']['cash']<0):
        minus_asset += balance_sheet['assets']['cash']
        plus_debt += balance_sheet['assets']['cash']
        balance_sheet['liabilities']['account_payable'] -= balance_sheet['assets']['cash']
        balance_sheet['liabilities']['total_current_liabilities'] -= balance_sheet['assets']['cash']
        balance_sheet['liabilities']['total_liabilities'] -= balance_sheet['assetes']['cash']
        balance_sheet['assets']['cash'] = 0
    balance_sheet['assets']['total_current_assets'] -= minus_asset
    balance_sheet['assets']['total_assets'] -= minus_asset
    balance_sheet['net_worth']['net_worth'] -= total_pay
    balance_sheet['net_worth']['liabilities_networth'] -= total_pay

    income_statement['expenses']['payroll'] += salary
    income_statement['expenses']['payroll_withholding'] += withold
    income_statement['other']['net_income'] -= (total_pay+withold)

    employee[emp_order]['payment_status'] = True

    payroll_hist[-1]['salary'] = salary
    payroll_hist[-1]['bounce'] = withold
    payroll_hist[-1]['fed_tax'] = federal_tax_calc(salary)
    payroll_hist[-1]['state_tax'] = salary*state_tax_rate
    payroll_hist[-1]['security_tax'] = salary*social_security_tax_rate
    payroll_hist[-1]['midcare_tax'] = salary*medical_tax_rate
    payroll_hist[-1]['total_paid'] = total_pay




    # Save the updated employee list back to the file
    with open(balance_sheet_path, 'w') as file:
        json.dump(balance_sheet, file, indent=4)

    with open(income_statement_path,'w') as file:
        json.dump(income_statement,file,indent=4)

    with open(employee_file_path,'w') as file:
        json.dump(employee,file,indent=4)

    with open(payroll_history_path,'w') as file:
        json.dump(payroll_hist,file,indent=4)

    # Return a success message as JSON
    return jsonify({"message": "Payroll updated successfully!"})

@app.route('/add_invoice',methods=['post'])
def make_invoice():
    new_invoice = request.get_json()
    # print(new_invoice)
    if os.path.exists(balance_sheet_path):
        # If the file exists, load the current data
        with open(balance_sheet_path, 'r') as file:
            balance_sheet = json.load(file)
    else:
        print("error! No balance sheet file!\n")
        return jsonify({"message":"Balance Sheet update failed!"})

    if os.path.exists(income_statement_path):
        # If the file exists, load the current data
        with open(income_statement_path, 'r') as file:
            income_statement = json.load(file)
    else:
        print("error! No income statement file!\n")
        return jsonify({"message":"Income Statement update failed!"})

    if os.path.exists(customer_file_path):
        # If the file exists, load the current data
        with open(customer_file_path, 'r') as file:
            customers = json.load(file)
    else:
        print("error! No customer file!\n")
        return jsonify({"message":"Customer file not exist!"})

    if os.path.exists(invoice_history_path):
        # If the file exists, load the current data
        with open(invoice_history_path, 'r') as file:
            invoices = json.load(file)
    else:
        invoices = []

    if os.path.exists(inventory_path):
        # If the file exists, load the current data
        with open(inventory_path, 'r') as file:
            inventories = json.load(file)
    else:
        print("error! No inventory file!\n")
        return jsonify({"message":"Inventory file not exist!"})

    cust_order = len(customers)
    new_invoice['company_id'] = int(new_invoice['company_id'])
    new_invoice['quantity'] = float(new_invoice['quantity'])
    for _i in range(len(customers)):
        if(customers[_i]['id']==new_invoice['company_id']):
            cust_order = _i
            break
    customers[cust_order]['price'] = float(customers[cust_order]['price'])
    gross_profit = (customers[cust_order]['price']-cog_unit)*new_invoice['quantity']
    print("Gross Profit={}".format(gross_profit))
    balance_sheet['assets']['account_receivable'] += customers[cust_order]['price']*new_invoice['quantity']
    balance_sheet['assets']['total_current_assets'] += customers[cust_order]['price']*new_invoice['quantity']
    balance_sheet['assets']['total_assets'] += customers[cust_order]['price']*new_invoice['quantity']
    balance_sheet['net_worth']['net_worth'] += customers[cust_order]['price']*new_invoice['quantity']
    balance_sheet['net_worth']['liabilities_networth'] += customers[cust_order]['price']*new_invoice['quantity']

    income_statement['sales']['sales'] += customers[cust_order]['price']*new_invoice['quantity']
    income_statement['sales']['cogs'] += cog_unit*new_invoice['quantity']
    income_statement['sales']['gross_profit'] += gross_profit
    income_statement['other']['net_income'] += gross_profit

    inventories['completed_unit'] -= new_invoice['quantity']

    new_invoice['company_name'] = customers[cust_order]['company_name']
    new_invoice['price_unit'] = customers[cust_order]['price']
    new_invoice['total'] = customers[cust_order]['price']*new_invoice['quantity']

    invoices.append(new_invoice)

    with open(balance_sheet_path, 'w') as file:
        json.dump(balance_sheet, file, indent=4)

    with open(income_statement_path,'w') as file:
        json.dump(income_statement,file,indent=4)

    with open(invoice_history_path,'w') as file:
        json.dump(invoices,file,indent=4)

    with open(inventory_path,'w') as file:
        json.dump(inventories,file,indent=4)


    # Return a success message as JSON
    return jsonify({"message": "Invoice created successfully!"})

@app.route('/add_PO',methods=['post'])
def make_PO():
    new_PO = request.get_json()
    if os.path.exists(balance_sheet_path):
        # If the file exists, load the current data
        with open(balance_sheet_path, 'r') as file:
            balance_sheet = json.load(file)
    else:
        print("error! No balance sheet file!\n")
        return jsonify({"message":"Balance Sheet update failed!"})

    if os.path.exists(vendor_file_path):
        # If the file exists, load the current data
        with open(vendor_file_path, 'r') as file:
            vendors = json.load(file)
    else:
        print("error! No vendor file!\n")
        return jsonify({"message":"Vendor file not exist!"})

    if os.path.exists(inventory_path):
        # If the file exists, load the current data
        with open(inventory_path, 'r') as file:
            inventories = json.load(file)
    else:
        print("error! No inventory file!\n")
        return jsonify({"message":"Inventory file not exist!"})

    if os.path.exists(PO_history_path):
        # If the file exists, load the current data
        with open(PO_history_path, 'r') as file:
            POs = json.load(file)
    else:
        POs = []

    vendor_order = len(vendors)
    new_PO['company_id'] = int(new_PO['company_id'])
    new_PO['quantity'] = float(new_PO['quantity'])
    for _i in range(len(vendors)):
        if(vendors[_i]['id']==new_PO['company_id']):
            vendor_order = _i
            break

    minus_asset = new_PO['quantity']*vendors[vendor_order]['price_unit']
    balance_sheet['liabilities']['account_payable'] += minus_asset
    balance_sheet['liabilities']['total_current_liabilities'] += minus_asset
    balance_sheet['liabilities']['total_liabilities'] += minus_asset
    balance_sheet['assets']['inventory'] += minus_asset
    # balance_sheet['assets']['cash'] -= minus_asset
    # if(balance_sheet['assets']['cash']<0):
    #     minus_asset += balance_sheet['assets']['cash']
    #     balance_sheet['liabilities']['account_payable'] -= balance_sheet['assets']['cash']
    #     balance_sheet['liabilities']['total_current_liabilities'] -= balance_sheet['assets']['cash']
    #     balance_sheet['liabilities']['total_liabilities'] -= balance_sheet['assetes']['cash']
    #     balance_sheet['assets']['cash'] = 0


    inventories[vendors[vendor_order]['part']]['quantity'] += new_PO['quantity']
    inventories[vendors[vendor_order]['part']]['value'] += new_PO['quantity']*vendors[vendor_order]['price_unit']
    inventories['total_value'] += new_PO['quantity']*vendors[vendor_order]['price_unit']
    new_PO['company_name'] = vendors[vendor_order]['company_name']
    new_PO['price_unit'] = vendors[vendor_order]['price_unit']
    new_PO['total'] = new_PO['price_unit']*new_PO['quantity']
    POs.append(new_PO)

    with open(balance_sheet_path, 'w') as file:
        json.dump(balance_sheet, file, indent=4)

    with open(inventory_path,'w') as file:
        json.dump(inventories,file,indent=4)

    with open(PO_history_path,'w') as file:
        json.dump(POs,file,indent=4)
    return jsonify({"message": "Purchase order created successfully!"})

@app.route('/settle_balance_sheet',methods=['post'])
def settle_balance_sheet():
    if os.path.exists(balance_sheet_path):
        # If the file exists, load the current data
        with open(balance_sheet_path, 'r') as file:
            balance_sheet = json.load(file)
    else:
        print("error! No balance sheet file!\n")
        return jsonify({"message":"Balance Sheet update failed!"})

    balance_sheet['assets']['cash'] += balance_sheet['assets']['account_receivable']
    balance_sheet['assets']['account_receivable'] = 0
    balance_sheet['assets']['cash'] -= balance_sheet['liabilities']['account_payable']
    balance_sheet['assets']['account_payable'] = 0

    with open(balance_sheet_path,'w') as file:
        json.dump(balance_sheet,file,indent=4)
    return jsonify({"message":"balance sheet settled for this month!"})

    

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(current_dir, path)

if __name__ == '__main__':
    app.run(debug=True)
