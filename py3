import torch
import torch.nn as nn
import torch.optim as optim

class MyFormulaNet(nn.Module):
    def __init__(self, n_in, n_h1, n_h2, n_out):
        super().__init__()
        # Веса и сдвиги для двух слоев
        self.w1 = nn.Parameter(torch.randn(n_in, n_h1) * 0.2)
        self.b1 = nn.Parameter(torch.zeros(n_h1))

        self.w2 = nn.Parameter(torch.randn(n_h1, n_h2) * 0.2)
        self.b2 = nn.Parameter(torch.zeros(n_h2))

        # Выходной слой
        self.w_out = nn.Parameter(torch.randn(n_h2, n_out) * 0.2)
        self.b_out = nn.Parameter(torch.zeros(n_out))

    def forward(self, x):
        # --- СЛОЙ 1 ---
        z1 = x @ self.w1 + self.b1
        # Твоя формула: z^2 * (1 - z) + b
        h1 = torch.tanh((z1**2) * (1 - z1) + self.b1)

        # --- СЛОЙ 2 ---
        z2 = h1 @ self.w2 + self.b2
        # Снова твоя формула во втором слое
        h2 = torch.tanh((z2**2) * (1 - z2) + self.b2)

        # ФИНАЛ
        return h2 @ self.w_out + self.b_out

# ПАРАМЕТРЫ (100 нейронов в каждом слое)
N = 100
custom_model = MyFormulaNet(1, N, N, 1)
base_model = nn.Sequential(
    nn.Linear(1, N), nn.ReLU(),
    nn.Linear(N, N), nn.ReLU(),
    nn.Linear(N, 1)
)

# ДАННЫЕ (Аппроксимируем сложную волну)
x = torch.linspace(-3, 3, 300).view(-1, 1)
y = torch.sin(x**2)

def train(m, name):
    optimizer = optim.Adam(m.parameters(), lr=0.005)
    crit = nn.MSELoss()
    for i in range(2001):
        optimizer.zero_grad()
        loss = crit(m(x), y)
        loss.backward()
        optimizer.step()
    print(f"{name} Ошибка (Loss): {loss.item():.6f}")

train(custom_model, "Твоя сеть (z^2 * (1-z) + b)")
train(base_model, "Базовая сеть (ReLU)")
