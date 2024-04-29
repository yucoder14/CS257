import flask
import psycopg2 


app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>') 
def my_add(num1,num2):
	x = eval(num1) 
	y = eval(num2)  
	result = x + y
	return f'{result}'

@app.route('/pop/<abbrev>') 
def my_pop(abbrev): 
	conn = psycopg2.connect(
	    host="localhost",
	    port=5432,
	    database="yuc3",
	    user="yuc3",
	    password="tablet686pencil")
	cur = conn.cursor() 
	sql = """
		SELECT name, statepopulation FROM statepopulation 
		WHERE statecode=%s
	      """
	cur.execute(sql, [abbrev])
	row = cur.fetchall()
	if (len(row) == 0): 
		return "Invalid State Code"
	else: 
		return f"{row[0][0]} has population of {row[0][1]}"


if __name__ == '__main__':
    my_port = 5132 
    app.run(host='0.0.0.0', port = my_port) 
