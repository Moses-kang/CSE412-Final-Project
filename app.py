import psycopg2
from flask import Flask, render_template, request, redirect, url_for

#connecting to database
#con = psycopg2.connect(
#    database = "AnimalCrossingDB"
#    user = "postgres"
#    password = "password"
#)
#call cursor when need... cur = con.cursor()
#use query:
#query = "SELECT * FROM species WHERE sName = '" + _search +"';"
#cur.execute(query)
#rows = cur.fetchall()
#remember to close connection... con.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homePage.html')

@app.route('/villagerRecs')
def villagerRec():
    return render_template('villRecs.html')

@app.route('/cart')
def myCart():
    return render_template('cart.html')

@app.route('/getRecs', methods = ['GET'])
def recomendations():
    print(request.values)
    try:
        con = psycopg2.connect("dbname=AnimalCrossingDB user=postgres password=password host=localhost")
        cur = con.cursor()   

        if 'villagerButton' in request.values:
            type = 0
            _villager = request.values.get('villagers')
            query = "SELECT furniture.name, furniture.furn_type, furniture.image FROM furniture INNER JOIN owns ON owns.name = '"+_villager+"' AND furniture.furn_id = owns.furn_id;"
            
            cur.execute(query)
            rows = cur.fetchall()
            print(rows)
            return render_template('villRecs.html', types = type, dataset = rows)

    except Exception as e:
        print(e)
        return str(e)
    finally:
        cur.close()
        con.close()

@app.route('/searchResult', methods = ['GET'])
def searching():
    print(request.values)
    try:
        con = psycopg2.connect("dbname=AnimalCrossingDB user=postgres password=password host=localhost")
        cur = con.cursor()  

        if 'furnitureButton' in request.values:
            type = 0
            _furniture = request.values.get('furnitureType')
            query = "SELECT * FROM furniture WHERE furn_type = '" + _furniture + "';"
            cur.execute(query)
            rows = cur.fetchall()
            if rows is None:
                return "No items found"
            else:
                return render_template('result.html', types = type, dataset = rows)
        elif 'interactButton' in request.values:
            type = 0
            _interact = request.values.get('interactions')
            query = "SELECT * FROM furniture WHERE interactive = '"+ _interact +"';"
            cur.execute(query)
            rows = cur.fetchall()
            if rows is None:
                return "No items found"
            else:
                return render_template('result.html', types = type, dataset = rows)
        elif 'originButton' in request.values:
            type = 4
            _origin = request.values.get('originType')
            query = "SELECT furniture.name, furniture.furn_type, furniture.image FROM furniture INNER JOIN origin ON "+_origin+" = 'TRUE' AND origin.furn_id = furniture.furn_id;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows is None:
                return "No items found"
            else:
                return render_template('result.html', types = type, dataset = rows)
        elif 'collectionButton' in request.values:
            type = 1
            _collect = request.values.get('collectType')
            query = "SELECT furniture.name, furniture.furn_type, collectible.collect_type, furniture.image FROM furniture INNER JOIN collectible ON collectible.collect_type = '"+_collect+"' AND furniture.furn_id = collectible.furn_id;"
            print(query)
            cur.execute(query)
            rows = cur.fetchall()
            if rows is None:
                return "No items found"
            else:
                return render_template('result.html', types = type, dataset = rows)
        elif 'flowerButton' in request.values:
            type = 2
            _flower = request.values.get('flowerColor')
            
            query = "SELECT furniture.name, furniture.furn_type, flowers.color, furniture.image FROM furniture INNER JOIN flowers ON flowers.color = '"+_flower+"' AND furniture.furn_id = flowers.furn_id;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows is None:
                return "No items found"
            else:
                return render_template('result.html', types = type, dataset = rows)

    except Exception as e:
        print(e)
        return str(e)
    finally:
        cur.close()
        con.close()


if __name__ == "__main__":
    app.run(debug=True)
