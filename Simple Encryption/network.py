








from tensorflow import keras
from tensorflow.keras import layers, models, callbacks



from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import mean_absolute_error

from tensorflow.keras.callbacks import EarlyStopping



def getConvertedFormatofText(x):

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(x)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    return X_train_tfidf


def getValidationData(xtest, ytest):
    xtest, xvalid, ytest, yvalid = train_test_split(xtest, ytest, test_size=0.50, random_state=42)
    return xtest, xvalid, ytest, yvalid

def getTrainTestData():

    data = pd.read_csv("../title.tsv", sep="\t")
    data.columns=["words","output"]
    x = getConvertedFormatofText(data.words)
    y = data.output
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.40, random_state = 42)
    xtest, xvalid, ytest, yvalid = getValidationData(xtest, ytest)
    return  xtrain, xtest, xvalid, ytrain, ytest, yvalid



def getTheNetwork(num=6):

    list_dense = []
    for x in range(1,num):
        list_dense.append(layers.Dense(units= 20*x, activation='relu', input_shape=[1]  ))
        list_dense.append(layers.BatchNormalization())
        list_dense.append(layers.Dropout(rate=0.3))

    list_dense.append(layers.Dense(units=1))

    return  list_dense




model = keras.Sequential([
    getTheNetwork(6)
])

model.compile(
    optimizer='adam',
    loss='mae',
    metrics='max_error'
)


early_stopping = EarlyStopping(
    min_delta=0.001,
    patience=40,
    restore_best_weights=True
)



xtrain, xtest, xvalid, ytrain, ytest, yvalid = getTrainTestData()






history = model.fit(
    xtrain, ytrain,
    validation_data=(xvalid, yvalid),
    batch_size=100,
    epochs=20,
    callbacks=[early_stopping],
    verbose=0
)





history_df = pd.DataFrame(history.history)
history_df.loc[5:, ['loss', 'val_loss']].plot()
history_df.loc[5:, ['max_error', 'val_max_error']].plot()




history_df['val_loss'].min()
history_df['val_max_error'].max()




export_path_keras = "simple_file_hacker.h5"
model.save(export_path_keras)




reloaded = models.load_model(export_path_keras)
reloaded.summary()

ypred = reloaded.predict(xtest)


mean_absolute_error(ytest, ypred)




































