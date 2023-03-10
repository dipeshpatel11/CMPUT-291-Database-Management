import sqlite3
import time
import matplotlib.pyplot as plt
import numpy as np

print("------Starting A3Small Database------")
conn = sqlite3.connect('A3Small.db')
c = conn.cursor()

# UNINFORMED

print("...Executing Uninformed Scenario...")

c.execute('PRAGMA autoindex = 0')
c.execute('PRAGMA foreign_keys = OFF')

c.execute("ALTER TABLE Customers RENAME TO oldCustomers;")
c.execute("""CREATE TABLE Customers ( customer_id TEXT,customer_postal_code INTEGER);""")
c.execute("INSERT INTO Customers SELECT * FROM oldCustomers;")

c.execute("ALTER TABLE Sellers RENAME TO oldSellers;")
c.execute("""CREATE TABLE Sellers ( seller_id TEXT,seller_postal_code INTEGER);""")
c.execute("INSERT INTO Sellers SELECT * FROM oldSellers;")

c.execute("ALTER TABLE Orders RENAME TO oldOrders;")
c.execute("""CREATE TABLE Orders ( order_id TEXT,customer_id TEXT);""")
c.execute("INSERT INTO Orders SELECT * FROM oldOrders;")

c.execute("ALTER TABLE Order_items RENAME TO oldOrdersItems;")
c.execute("""CREATE TABLE Order_items ( order_id TEXT,order_item_id INTEGER,product_id TEXT , seller_id TEXT);""")
c.execute("INSERT INTO Order_items SELECT * FROM oldOrdersItems;")

start1 = time.time()

for q in range(0, 50):

    Uni_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

end1 = time.time()
Uni_f = Uni_q.fetchone()

S_uni_time = ((end1 - start1) * 10 ** 3)/50

print("SmallDB Uninformed Query Average Runtime: ", S_uni_time)

conn.commit()
conn.close()

# Self-optimized:

print("Executing Self-optimized...")

conn = sqlite3.connect('A3Small.db')
c = conn.cursor()

c.execute('PRAGMA autoindex = 1;')
c.execute('PRAGMA foreign_keys = ON;')

c.execute("DROP TABLE Customers;")
c.execute("ALTER TABLE oldCustomers RENAME TO Customers;")

c.execute("DROP TABLE Sellers;")
c.execute("ALTER TABLE oldSellers RENAME TO Sellers;")

c.execute("DROP TABLE Orders;")
c.execute("ALTER TABLE oldOrders RENAME TO Orders;")

c.execute("DROP TABLE Order_items;")
c.execute("ALTER TABLE oldOrdersItems RENAME TO Order_items;")

start2 = time.time()

for q in range(0, 50):

    self_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

end2 = time.time()
self_f = self_q.fetchall()


S_self_time = ((end2 - start2) * 10 ** 3)/50

print("SmallDB Self-optimized Query Average Runtime: ", S_self_time)

conn.commit()
conn.close()

# User-optimized:

print("Executing User-optimized...")

conn = sqlite3.connect('A3Small.db')
c = conn.cursor()

c.execute('PRAGMA automatic_index = true;')
c.execute('CREATE INDEX cid_index ON Customers(customer_postal_code);')
c.execute('CREATE INDEX oid_index ON Orders(customer_id);')

start3 = time.time()

for q in range(0, 50):

    User_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

end3 = time.time()
User_f = User_q.fetchall()

S_user_time = ((end3 - start3) * 10 ** 3)/50

print("SmallDB User-optimized Query Average Runtime: ", S_user_time)

c.execute('DROP INDEX IF EXISTS cid_index;')
c.execute('DROP INDEX IF EXISTS oid_index;')

conn.commit()
conn.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
print("------Starting A3Medium Database------")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

conn = sqlite3.connect('A3Medium.db')
c = conn.cursor()

# UNINFORMED

print("Executing Uninformed...")

c.execute('PRAGMA autoindex = 0')
c.execute('PRAGMA foreign_keys = OFF')

c.execute("ALTER TABLE Customers RENAME TO oldCustomers;")
c.execute("""CREATE TABLE Customers ( customer_id TEXT,customer_postal_code INTEGER);""")
c.execute("INSERT INTO Customers SELECT * FROM oldCustomers;")

c.execute("ALTER TABLE Sellers RENAME TO oldSellers;")
c.execute("""CREATE TABLE Sellers ( seller_id TEXT,seller_postal_code INTEGER);""")
c.execute("INSERT INTO Sellers SELECT * FROM oldSellers;")

c.execute("ALTER TABLE Orders RENAME TO oldOrders;")
c.execute("""CREATE TABLE Orders ( order_id TEXT,customer_id TEXT);""")
c.execute("INSERT INTO Orders SELECT * FROM oldOrders;")

c.execute("ALTER TABLE Order_items RENAME TO oldOrdersItems;")
c.execute("""CREATE TABLE Order_items ( order_id TEXT,order_item_id INTEGER,product_id TEXT , seller_id TEXT);""")
c.execute("INSERT INTO Order_items SELECT * FROM oldOrdersItems;")

M_start1 = time.time()

for q in range(0, 50):

    M_Uni_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

M_end1 = time.time()
M_Uni_f = M_Uni_q.fetchall()

M_uni_time = ((M_end1 - M_start1) * 10 ** 3)/50

print("MediumDB Uninformed Query Average Runtime: ", M_uni_time)

conn.commit()
conn.close()

# Self-optimized:

print("Executing Self-optimized...")

conn = sqlite3.connect('A3Medium.db')
c = conn.cursor()

c.execute('PRAGMA autoindex = 1;')
c.execute('PRAGMA foreign_keys = ON;')

c.execute("DROP TABLE Customers;")
c.execute("ALTER TABLE oldCustomers RENAME TO Customers;")

c.execute("DROP TABLE Sellers;")
c.execute("ALTER TABLE oldSellers RENAME TO Sellers;")

c.execute("DROP TABLE Orders;")
c.execute("ALTER TABLE oldOrders RENAME TO Orders;")

c.execute("DROP TABLE Order_items;")
c.execute("ALTER TABLE oldOrdersItems RENAME TO Order_items;")

M_start2 = time.time()

for q in range(0, 50):

    M_self_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

M_end2 = time.time()
M_self_f = M_self_q.fetchall()

M_self_time = ((M_end2 - M_start2) * 10 ** 3)/50

print("MediumDB Self-optimized Query Average Runtime: ", M_self_time)

conn.commit()
conn.close()

# User-optimized:

print("Executing User-optimized...")

conn = sqlite3.connect('A3Medium.db')
c = conn.cursor()

c.execute('PRAGMA automatic_index = true;')
c.execute('CREATE INDEX cid_index ON Customers(customer_postal_code);')
c.execute('CREATE INDEX oid_index ON Orders(customer_id);')

M_start3 = time.time()

for q in range(0, 50):

    M_User_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

M_end3 = time.time()
M_User_f = M_User_q.fetchall()

M_user_time = ((M_end3 - M_start3) * 10 ** 3)/50

print("MediumDB User-optimized Query Average Runtime: ", M_user_time)

c.execute('DROP INDEX IF EXISTS cid_index;')
c.execute('DROP INDEX IF EXISTS oid_index;')

conn.commit()
conn.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
print("------Starting A3Large Database------")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

conn = sqlite3.connect('A3Large.db')
c = conn.cursor()

# UNINFORMED

print("Executing Uninformed...")

c.execute('PRAGMA autoindex = 0')
c.execute('PRAGMA foreign_keys = OFF')

c.execute("ALTER TABLE Customers RENAME TO oldCustomers;")
c.execute("""CREATE TABLE Customers ( customer_id TEXT,customer_postal_code INTEGER);""")
c.execute("INSERT INTO Customers SELECT * FROM oldCustomers;")

c.execute("ALTER TABLE Sellers RENAME TO oldSellers;")
c.execute("""CREATE TABLE Sellers ( seller_id TEXT,seller_postal_code INTEGER);""")
c.execute("INSERT INTO Sellers SELECT * FROM oldSellers;")

c.execute("ALTER TABLE Orders RENAME TO oldOrders;")
c.execute("""CREATE TABLE Orders ( order_id TEXT,customer_id TEXT);""")
c.execute("INSERT INTO Orders SELECT * FROM oldOrders;")

c.execute("ALTER TABLE Order_items RENAME TO oldOrdersItems;")
c.execute("""CREATE TABLE Order_items ( order_id TEXT,order_item_id INTEGER,product_id TEXT , seller_id TEXT);""")
c.execute("INSERT INTO Order_items SELECT * FROM oldOrdersItems;")

L_start1 = time.time()

for q in range(0, 50):

    L_Uni_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

L_end1 = time.time()
L_Uni_f = L_Uni_q.fetchall()

L_uni_time = ((L_end1 - L_start1) * 10 ** 3)/50

print("LargeDB Uninformed Query Average Runtime: ", L_uni_time)

conn.commit()
conn.close()

# Self-optimized:

print("Executing Self-optimized...")

conn = sqlite3.connect('A3Large.db')
c = conn.cursor()

c.execute('PRAGMA autoindex = 1;')
c.execute('PRAGMA foreign_keys = ON;')

c.execute("DROP TABLE Customers;")
c.execute("ALTER TABLE oldCustomers RENAME TO Customers;")

c.execute("DROP TABLE Sellers;")
c.execute("ALTER TABLE oldSellers RENAME TO Sellers;")

c.execute("DROP TABLE Orders;")
c.execute("ALTER TABLE oldOrders RENAME TO Orders;")

c.execute("DROP TABLE Order_items;")
c.execute("ALTER TABLE oldOrdersItems RENAME TO Order_items;")

L_start2 = time.time()
for q in range(0, 50):

    L_self_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

L_end2 = time.time()
L_self_f = L_self_q.fetchall()

L_self_time = ((L_end2 - L_start2) * 10 ** 3)/50

print("LargeDB Self-optimized Query Average Runtime: ", L_self_time)

conn.commit()
conn.close()

# User-optimized:

print("Executing User-optimized...")

conn = sqlite3.connect('A3Large.db')
c = conn.cursor()

c.execute('PRAGMA automatic_index = true;')
c.execute('CREATE INDEX cid_index ON Customers(customer_postal_code);')
c.execute('CREATE INDEX oid_index ON Orders(customer_id);')

L_start3 = time.time()
for q in range(0, 50):

    L_User_q = c.execute(''' SELECT COUNT(O.order_id)
                    FROM Customers C, Orders O
                    WHERE C.customer_postal_code = (SELECT customer_postal_code FROM Customers ORDER BY RANDOM() LIMIT 1)
                    AND C.customer_id = O. customer_id 
                    AND (SELECT COUNT(OI.order_item_id)
                        FROM Order_items OI
                        WHERE O.order_id = OI.order_id) > 1;
                     ''')

L_end3 = time.time()
L_User_f = L_User_q.fetchall()

L_user_time = ((L_end3 - L_start3) * 10 ** 3)/50

print("LargeDB User-optimized Query Average Runtime: ", L_user_time)

c.execute('DROP INDEX IF EXISTS cid_index;')
c.execute('DROP INDEX IF EXISTS oid_index;')

conn.commit()
conn.close()

# plotting graph

S_time_list = [S_uni_time, S_self_time, S_user_time]
M_time_list = [M_uni_time, M_self_time, M_user_time]
L_time_list = [L_uni_time, L_self_time, L_user_time]

print(S_time_list, M_time_list, L_time_list)

species = (
    "SmallDB\n",
    "MediumDB\n",
    "LargeDB\n",
)
weight_counts = {
    "Uninformed": np.array([S_uni_time, M_uni_time, L_uni_time]),
    "Self-optimized": np.array([S_self_time, M_self_time, L_self_time]),
    "User-optimized": np.array([S_user_time, M_user_time, L_user_time]),

}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Query 1 (runtime in ms)")
ax.legend(loc="upper left")

plt.show()
