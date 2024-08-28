from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
classifier = joblib.load('model/fake_news_classifier.joblib')
tfidf_vectorizer = joblib.load('model/tfidf_vectorizer.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        # Get the news text from the form
        news_text = request.form['news']
        
        # Vectorize the input text
        text_vectorized = tfidf_vectorizer.transform([news_text])
        
        # Make prediction
        prediction = classifier.predict(text_vectorized)
        
        # Determine the result based on prediction
        result = "Fake News" if prediction[0] == 0 else "Real News"
        
        # Return result as JSON
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
