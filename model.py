from sklearn.neighbors import KNeighborsClassifier
import pickle
knn = pickle.load(open('models/knn.model', 'rb'))

classes = ['Setosa', 'Versicolor', 'Virginica']

arguments = ['s_length', 's_width', 'p_length', 'p_width']
def predict(*arguments):
    result = knn.predict([[s_length, s_width, p_length, p_width]]).item()
    return classes[result]