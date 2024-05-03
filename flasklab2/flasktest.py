from flask import Flask
from flask import render_template
import psycopg2

app = Flask(__name__) 

@app.route('/')
def welcome(): 
	return render_template("index.html")

@app.route('/<stateCode>') 
def state_info(stateCode): 
	conn = psycopg2.connect(
		host='localhost',
		port=5432,
		database='yuc3',
		user='yuc3',
		password='tablet686pencil')
	cur = conn.cursor()
	sql = """
		SELECT name FROM statepopulation WHERE statecode=%s
	      """
	cur.execute(sql,[stateCode])
	row = cur.fetchall()
	state_name = row[0][0] 

	sql = """
		SELECT city, population FROM citypopulation WHERE 
		state=%s ORDER BY population desc 	
	      """
	cur.execute(sql,[state_name]) 
	rows = cur.fetchall() 
	csv = "city,population\\n"
	for tuple in rows: 
		line = ",".join([tuple[0],str(tuple[1])])
		csv = csv + line + "\\n"  
	print(csv)
	return render_template("state.html",state = state_name,cities = csv)

if __name__ == '__main__':
    my_port = 5132
    app.run(host='0.0.0.0', port = my_port)
