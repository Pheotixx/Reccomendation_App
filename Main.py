from flask import Flask, jsonify, request
import csv

all_movies = []
with open("movies1.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
unseen_movies = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route("/liked-movies",methods = ["POST"])
def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-movies",methods = ["POST"])
def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unseen-movies",methods = ["POST"])
def unseen_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unseen_movies.append(movie)
    return jsonify({
        "status":"success"
    }),201

    
if __name__ == "__main__":
    app.run()
