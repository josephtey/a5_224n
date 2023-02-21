# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils
from tqdm import tqdm

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path', default=None)
args = argp.parse_args()

predictions = []
file = open(args.eval_corpus_path, encoding='utf-8')
for line in file:
    predictions.append("London")

total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
print("Accuracy with London Baseline: ", str(correct / total))