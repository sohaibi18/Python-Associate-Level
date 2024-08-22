from sys import path
#OR
# import sys
# sys.path

payment_path = r'C:\Users\Sohaib\anaconda3\envs\Navttc_Class\ShoesEcommerceSystem\PaymentMethod'
path.append(payment_path)


sales_path = r'C:\Users\Sohaib\anaconda3\envs\Navttc_Class\ShoesEcommerceSystem\SalesRecord'
path.append(sales_path)

shoescrud_path = r'C:\Users\Sohaib\anaconda3\envs\Navttc_Class\ShoesEcommerceSystem\ShoesCrudOperations'
path.append(shoescrud_path)

import shoescrud
import sales
import payment