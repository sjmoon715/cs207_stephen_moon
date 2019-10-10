import numpy as np

class Regression():
    params = {}
    def __init__(self):
        self.params = {}
    def get_params(self):
        return self.params
    # Allows user to set params
    def set_params(self, **kwargs):
        for key,value in kwargs.items():
            self.params[key] = value
    # To be implemented in subclasses
    def fit(self, X, y):
        raise NotImplementedError
    def predict(self, X):
        X = X
        My_y = np.dot(X, self.params['betas'])
        return My_y
    # Calculates R^2 score
    def score(self, X, y):
        My_y = self.predict(X)
        y_sum = 0
        for i in range(len(y)):
            y_sum += y[i]
        y_mean = y_sum/len(y)
        SSt = 0
        SSe = 0
        for i in range(len(y)):
            SSt += (y[i] - y_mean)**2
            SSe += (y[i] - My_y[i])**2
        R2 = 1 - SSe/SSt
        return R2

class LinearRegression(Regression):
    def __init__(self,X,y):
        super().__init__()
    def fit (self, X, y):
        # Appending column of ones
        n = X.shape[0]
        ones = np.ones(n).reshape(n,1)
        X = np.append(X,ones,1)
        Xt = X.transpose()
        # Calculating coefficients and intercept using OLS Linear Regression
        beta = np.dot(np.dot(np.linalg.pinv(np.dot(Xt,X)),Xt),y)
        # Storing coefficients and intercept seperately in params dict
        self.params['betas'] = beta[:-1]
        self.params['intercept'] = beta[-1]
        return(self.params)
    def predict(self, X):
        n = X.shape[0]
        ones = np.ones(n).reshape(n,1)
        X = np.append(X,ones,1)
        # Appending 'betas' and 'intercept' so that dimensions work for matrix multiplication
        betas = np.append(self.params['betas'],self.params['intercept'])
        My_y = np.dot(X, betas)
        return My_y

class RidgeRegression(LinearRegression):
    def __init__(self, X, y, alpha):
        super().__init__(X,y)
        self.alpha = alpha
        self.params['alpha'] = alpha
    def fit (self, X, y):
        # Reshaping matrices for both X and Gamma
        n = X.shape[0]
        ones = np.ones(n).reshape(n,1)
        X = np.append(X, ones, 1)
        Xt = X.transpose()
        gamma = np.identity(X.shape[1])*self.params['alpha']
        gammaT = gamma.transpose()
        # Calculating coefficients and intercepts using ridge regression
        inv_term = np.linalg.pinv(np.dot(Xt, X)+np.dot(gammaT,gamma))
        beta = np.dot(np.dot(inv_term, Xt),y)
        # Storing coefficients and intercepts seperately in params dict
        self.params['betas'] = beta[:-1]
        self.params['intercept'] = beta[-1]
        return self.params
    def predict(self, X):
        n = X.shape[0]
        ones = np.ones(n).reshape(n,1)
        X = np.append(X,ones,1)
        # Appending 'betas' and 'intercept' so that dimensions work for matrix multiplication
        betas = np.append(self.params['betas'],self.params['intercept'])
        My_y = np.dot(X, betas)
        return My_y