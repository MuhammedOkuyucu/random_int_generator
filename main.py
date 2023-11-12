#from flask import Flask  
#
#
#import random
#
#
#list_of_questions_which_already_asked = []
#
#def generate_random_number():
#    return random.randint(1, 45)
#  
#app = Flask(__name__) #creating the Flask class object   
# 
#@app.route('/') #decorator drfines the   
#def home():  
#    random_number = generate_random_number()
#    if random_number not in list_of_questions_which_already_asked:
#        print("Random number between 1 and 45:", random_number)
#
#    return  str(random_number)
#  
#if __name__ =='__main__':  
#    app.run(debug = True)  

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)