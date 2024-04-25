import psycopg2

conn = psycopg2.connect(
	host="localhost",
	port=5432,
	database="yuc3",
	user="yuc3",
	password="tablet686pencil")

def create_tables(): 
	
	cur = conn.cursor()
	
	create_state_table = """
		DROP TABLE IF EXISTS statepopulation;
		CREATE TABLE statepopulation (
			statecode text,
			name text,
			statepopulation integer);""" 
	
	create_city_table = """
		DROP TABLE IF EXISTS citypopulation;
		CREATE TABLE citypopulation (
			city text,state text,
			population integer,
			latitude real,
			longitude real);""" 
	
	cur.execute(create_state_table) 
	cur.execute(create_city_table) 
	
	conn.commit()

	return None

def copy_data(): 
	
	cur = conn.cursor() 
	
	state_file = open('./us-state-pop.csv')
	city_file = open('./us-cities-top-1k.csv')
 
	cur.copy_from(state_file,'statepopulation',sep=',')	
	cur.copy_from(city_file,'citypopulation',sep=',')

	conn.commit() 

	return None

#create_tables()
#copy_data()

