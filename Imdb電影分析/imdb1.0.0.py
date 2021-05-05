from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence



top_words =1000
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=top_words)
print("X_train.shape:", X_train.shape)
print("Y_train.shape:", Y_train.shape)
print("X_test.shape:", X_test.shape)
print("Y_test.shape:", Y_test.shape)

print(X_train[0])
print(Y_train[0])

max_index =max(max(sequence) for sequence in X_train)
print("Max Index:", max_index)

word_index = imdb.get_word_index()
we_index = word_index["we"]
print("'we' index: ", we_index)

decoded_word_map = dict([(value, key)for (key,value) in word_index.items()])
print(decoded_word_map[we_index])

decoded_indices = [decoded_word_map.get(i-3, "?") for i in X_train[0]]

print(decoded_indices)

decoded_review = " ".join(decoded_indices)
print(decoded_review)

max_words = 100
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)

print("X_trian.shape:", X_train.shape)
print("X_test.shape:", X_test.shape)



