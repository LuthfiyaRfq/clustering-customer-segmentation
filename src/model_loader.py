import pickle as pkl

def load_model(filename='model/classifier.pkl'):
  with open(filename, 'rb') as file:
    model = pkl.load(file)
  return model