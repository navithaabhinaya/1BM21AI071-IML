#Stack Exchange
# Enter your code here. Read input from STDIN. Print output to STDOUT
import json, sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.preprocessing import LabelEncoder

if sys.version_info[0] >= 3:
    raw_input = input

transformer = HashingVectorizer(stop_words='english')
label_encoder = LabelEncoder()

_train = []
train_label = []
f = open('training.json')

for i in range(int(f.readline())):
    h = json.loads(f.readline())
    _train.append(h['question'] + "\r\n" + h['excerpt'])
    train_label.append(h['topic'])

f.close()

# Convert text labels to numerical labels
train_label = label_encoder.fit_transform(train_label)

train = transformer.fit_transform(_train)
svm = LinearSVC()
svm.fit(train, train_label)

_test = []
for i in range(int(raw_input())):
    h = json.loads(raw_input())
    _test.append(h['question'] + "\r\n" + h['excerpt'])

test = transformer.transform(_test)
test_label = svm.predict(test)

# Convert numerical labels back to text labels before printing
test_label_text = label_encoder.inverse_transform(test_label)
for e in test_label_text:
    print(e)
