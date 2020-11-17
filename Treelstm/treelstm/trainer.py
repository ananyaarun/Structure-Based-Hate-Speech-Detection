from tqdm import tqdm

import torch
import torch.nn.functional as F

from . import utils


class Trainer(object):
    def __init__(self, args, model, criterion, optimizer, device):
        super(Trainer, self).__init__()
        self.args = args
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        self.epoch = 0

    # helper function for training
    def train(self, dataset):
        error_count=0
        self.model.train()
        self.optimizer.zero_grad()
        total_loss = 0.0
        indices = torch.randperm(len(dataset), dtype=torch.long, device='cpu')
        for idx in tqdm(range(len(dataset)), desc='Training epoch ' + str(self.epoch + 1) + ''):
            ltree, linput, label,tweet = dataset[indices[idx]]
            target = utils.map_label_to_target(label, 3)
            linput = linput.to(self.device)
            target = target.to(self.device)
            output = self.model(ltree, linput)
            loss = self.criterion(output, target)
            total_loss += loss.item()
            loss.backward()
            if idx % self.args.batchsize == 0 and idx > 0:
                self.optimizer.step()
                self.optimizer.zero_grad()

        self.epoch += 1
        return total_loss / len(dataset)

    # helper function for testing
    def test(self, dataset):
        self.model.eval()
        with torch.no_grad():
            error_count=0
            total_loss = 0.0
            predictions = torch.zeros(len(dataset), dtype=torch.float, device='cpu')
            accuracy=0
            for idx in tqdm(range(len(dataset)), desc='Testing epoch  ' + str(self.epoch) + ''):
                ltree, linput, label,tweet = dataset[idx]
                target = utils.map_label_to_target(label, 3)
                linput= linput.to(self.device)
                target = target.to(self.device)
                output = self.model(ltree, linput)
                loss = self.criterion(output, target)
                total_loss += loss.item()
                output = output.squeeze().to('cpu')
                predictions[idx] = torch.argmax(F.softmax(output))

        return total_loss / len(dataset), predictions

