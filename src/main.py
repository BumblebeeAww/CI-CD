from flask import Flask, jsonify, request

app = Flask(__name__)

# Определяем маршрут для сложения двух чисел
@app.route('/add', methods=['GET'])
def add_route():
    # Получаем параметры a и b из URL
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    
    # Возвращаем результат сложения в формате JSON
    result = a + b
    return jsonify(result=result)

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    app.run(debug=True)
