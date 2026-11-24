from flask import Flask
from flask import jsonify
import string

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, Flask!"

# @app.route('/alpha/<string:word>',methods=['GET'])
# def alphabets(word):
#     try:
#         alphabets = string.ascii_uppercase
#         # print(alphabets)
#         alphabet_to_number={}
#         for index,char in enumerate(alphabets):
#             number=(index % 9) +1
#             alphabet_to_number[char]=number
#         # print(alphabet_to_number)
#         sum=0
#         for char in word:
#             # print(char)
#             sum+=alphabet_to_number[char]
#             # print(alphabet_to_number[char])
#             ans=[]
#             for char in word:
#                 ans.append((char,alphabet_to_number[char]))
#         print(ans)
#         return jsonify({'sum':sum,'ans':ans}), 200
#     except Exception as e:
#         return jsonify({'message': 'Error', 'error': str(e)}), 500

@app.route('/alpha/<string:word>', methods=['GET'])
def alphabets(word):
    try:
        alphabets = string.ascii_uppercase
        alphabet_to_number = {char: (index % 9) + 1 for index, char in enumerate(alphabets)}
        sum = 0
        ans = []
        for char in word:
            sum += alphabet_to_number[char]
            ans.append((char, alphabet_to_number[char]))
        return jsonify({'sum': sum, 'ans': ans}), 200
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')