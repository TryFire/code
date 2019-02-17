import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # input and pre-handle data
    data = pd.read_csv('L100 P1 R1.csv',engine = 'python')
    data = data.iloc[:64,:12]
    data, throughout = np.split(data, (11,), axis=1)
    throughout = np.array(throughout, dtype = float).ravel()
    
    # Handle dummy variables
    features = np.zeros([64,14])
    features[:,:9] = data.iloc[:,:9]
    features[:,10:14] = pd.get_dummies(data.iloc[:,10])

    
    # normalization
    standard_scaler_X = StandardScaler()
    features = standard_scaler_X.fit_transform(features)
    
    # get the optimal hyperparameters
    my_model = Lasso()
    alpha_can = np.logspace(-3, 2, 10)
    lasso_my_model = GridSearchCV(my_model, param_grid={'alpha': alpha_can}, cv=5)
    lasso_my_model.fit(features, throughout)
    print ('超参数：\n', lasso_my_model.best_params_)
    
    # Re-fit function
    my_model = Lasso(alpha = 100)
    my_model.fit(features,throughout)
    print (my_model.coef_)
    print (my_model.intercept_)
    my_model_coef = my_model.coef_
    my_model_intercept = my_model.intercept_
    
    # calculate the average lose
    y_predicted = my_model.predict(features)
    mean_square_err = np.average((y_predicted - throughout) ** 2)  # Mean Squared Error
    root_mean_square_err = np.sqrt(mean_square_err)  # Root Mean Squared Error
    error_rate = root_mean_square_err/np.average(throughout)
    print (mean_square_err, root_mean_square_err, error_rate)
    
    # plot
    features_name = ['num.network.threads','num.io.threads',
                    'queued.max.requests','num.replica.fetchers',
                    'replica.fetch.min.bytes','replica.fetch.max.bytes',
                    'replica.fetch.wait.max.ms','num.partitions',
                    'min.insync.replicas','acks','buffer.memory',
                    'compression.type--gzip','compression.type--lz4',
                    'compression.type--producer','batch.size',
                    'linger.ms','timeout.ms','replication.factor',
                    'ProducerNum','topicnum','Sync--asnyc','Sync--sync'
                    ]
                    
    for i in range(0,22):
        plt.plot(features[:,i], throughout, 'r*', ms=10, label='Actual')
        plt.plot(features[:,i], y_predicted, 'g*', ms=10, label='Predict')
        plt.xlabel(features_name[i], fontsize=15)
        plt.ylabel(u'throughout', fontsize=15)
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()

