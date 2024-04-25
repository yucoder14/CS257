import psycopg2 

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="yuc3",
    user="yuc3",
    password="tablet686pencil")

def find_city(): 
	cur = conn.cursor() 
	city = input("Enter city:")
	sql = "SELECT latitude, longitude,state FROM citypopulation WHERE city = %s;"   
	cur.execute(sql,[city]) 
	row_list = cur.fetchall()

	if (len(row_list) < 1): 
		print(f"{city} does not exist among data set") 
	else: 
		for row in row_list: 
			print(f"{city},{row[2]} is located at lat:{row[0]} long:{row[1]}")

	return None

def largest_city(): 
	cur = conn.cursor() 
	sql = "SELECT city FROM citypopulation ORDER BY population DESC LIMIT 1;"
	cur.execute(sql)
	row = cur.fetchall() 
	print(f"The largest city in the US is {row[0][0]}")

	return None

def smallest_city_MN(): 
	cur = conn.cursor() 
	sql = "SELECT city FROM citypopulation WHERE state='Minnesota' ORDER BY population ASC LIMIT 1;"
	cur.execute(sql) 
	row = cur.fetchall()
	print(f"The smallest city in Minnesota is {row[0][0]}")

	return None

def extreme_cities(): 
	cur = conn.cursor()

	northern = "SELECT city FROM citypopulation ORDER BY latitude DESC LIMIT 1;" 
	southern = "SELECT city FROM citypopulation ORDER BY latitude ASC LIMIT 1;" 
	western  = "SELECT city FROM citypopulation ORDER BY longitude ASC LIMIT 1;" 
	eastern  = "SELECT city FROM citypopulation ORDER BY longitude DESC LIMIT 1;" 

	compass = ["east", "west", "south", "north"]
	i = 0; 
	
	for sql in [eastern, western, southern, northern]:
		cur.execute(sql) 
		row = cur.fetchall()
		print(f"The furthest {compass[i]} city in US is {row[0][0]}")
		i += 1;
	
	return None

def find_city_by_state(): 
	cur = conn.cursor() 
	
	found = False
	
	while (not found): 
		state_input = input("Enter state: ")  
		state_query = "SELECT name FROM statepopulation WHERE name=%s OR statecode=%s;"
		cur.execute(state_query,[state_input, state_input])
		row = cur.fetchall()
		if (len(row) == 0):
			print("Cannot find state") 		
		else: 
			found = True 
			state = row[0][0]
			city_query = "SELECT SUM(population) FROM citypopulation WHERE state =%s;" 
			cur.execute(city_query, [state])  
			row = cur.fetchall() 
			print(f"Total population of cities in {state} is {row[0][0]}")
		
	return None
#find_city()
#largest_city()
#smallest_city_MN()
#extreme_cities()
#find_city_by_state()
