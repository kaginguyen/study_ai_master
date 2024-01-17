# Importing Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class LinearRegression:
    def __init__(self):
        self.Q0 = np.random.uniform(1000, 10000) * -1  # Intercept Random value between 1k and 10k VND
        self.Q1 = np.random.uniform(100, 1000) * -1  # Coefficient of X generated randomly between 100 and 1k VND
        self.losses = []  # Storing the loss of each iteration


    def forward_propogation(self, training_input):
        predicted_values = np.multiply(self.Q1, training_input) + self.Q0  # y = mx + c
        return predicted_values


    def cost(self, predictions, training_output):
        return np.mean((predictions - training_output) ** 2)  # Calculating the cost


    def finding_derivatives(self, cost, predictions, training_input, training_output):
        diff = predictions - training_output
        dQ0 = np.mean(diff)  # d(J(Q0, Q1))/d(Q0)
        dQ1 = np.mean(np.multiply(diff, training_input))  # d(J(Q0, Q1))/d(Q1)
        return dQ0, dQ1


    def train(self, x_train, y_train, lr, itrs):
        for i in range(itrs):
            # Finding the predicted values (Using the linear equation y=mx+c)
            predicted_values = self.forward_propogation(x_train)

            # Calculating the Loss
            loss = self.cost(predicted_values, y_train)
            # Saving Loss history for testing 
            self.losses.append(loss)

            # Back Propagation 
            dQ0, dQ1 = self.finding_derivatives(
                loss, predicted_values, x_train, y_train
            )

            # Updating the Weights
            self.Q0 = self.Q0 - lr * (dQ0)
            self.Q1 = self.Q1 - lr * (dQ1)

        return (
            self.Q0,
            self.Q1,
            self.losses,
        )  # Returning the final model weights and the losses
    


# Import data
df = pd.read_csv("dataset.csv")
df = df.sort_values("X")
df["Y"] = df["Y"].rolling(3).mean()
df.dropna(inplace = True)

# Train-Test on the same dataset 
N = len(df)
x_train, y_train = np.array(df.X), np.array(df.Y)
x_test, y_test = x_train, y_train



lr = 0.01  # Learning Rate
itrs = 10000  # No. of iterations
model = LinearRegression()
Q0, Q1, losses = model.train(x_train, y_train, lr, itrs)



# Prediction on test data
y_pred = Q0 + x_test * Q1
print(f"Best-fit Line: (Y = {Q1}*X + {Q0})")
print(f"Prediction for Day 15:", Q1*15 + Q0)

# Plot the regression line with actual data pointa
plt.plot(x_test, y_test, "+", label="Data Points")
plt.plot(x_test, y_pred, label="Prediction Line")
plt.xlabel("Previous Days")
plt.ylabel("MSN Stock Price")
plt.legend()
plt.savefig("prediction.jpeg")