import torch.nn
from ai.model import TextCNNDataset

import sys

sys.path.insert(0, 'ai/')
model = torch.load('ai/TCNN-E750-L1.0438289642333984.pt')
dataset = TextCNNDataset(path='ai/data/train.json', lang="uk", vs=100000)


def get_prediction(text):
    """ Повертає сортований список (назва класу, ймовірність)"""
    embed_data = dataset.embed(text)
    intent_tensor = torch.tensor(embed_data)
    intent_tensor = TextCNNDataset.upsize(intent_tensor, 10).unsqueeze(0)

    output = model(intent_tensor)

    info = []
    for class_number, probability in enumerate(output[0]):
        info.append((dataset.get_label_by_index(class_number), probability))
    info.sort(key=lambda x: -x[1])
    return info


if __name__ == '__main__':
    while True:
        user_requests = input("Введіть запит: ")
        info = get_prediction(user_requests)
        for x, y in info:
            print("{}: {}".format(x, y))
