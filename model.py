from sklearn.neighbors import KNeighborsClassifier
import pickle
knn = pickle.load(open('models/knn.model', 'rb'))

classes = ['Setosa', 'Versicolor', 'Virginica']

def predict(s_length, s_width, p_length, p_width):
    result = knn.predict([[s_length, s_width, p_length, p_width]]).item()
    return classes[result]