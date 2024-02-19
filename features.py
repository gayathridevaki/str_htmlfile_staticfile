from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/String')
def String():
    return 'this is first view'


@FAI.route('/htmlfile')
def htmlfile():
    return render_template('htmlfile.html')

@FAI.route('/staticpage')
def staticpage():
    return render_template('static.html')







if __name__ =='__main__':
    FAI.run(debug=True)

