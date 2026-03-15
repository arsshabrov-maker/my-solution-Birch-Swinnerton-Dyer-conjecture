import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# --- ОПРЕДЕЛЕНИЕ СЕТЕЙ ---

class NetV1(nn.Module): # Формула: z^2 * (1 - z) + b
    def __init__(self, n=100):
        super().__init__()
        self.fc1 = nn.Linear(1, n); self.fc2 = nn.Linear(n, n); self.fc3 = nn.Linear(n, 1)
    def forward(self, x):
        z1 = self.fc1(x); h1 = torch.tanh((z1**2) * (1 - z1) + self.fc1.bias)
        z2 = self.fc2(h1); h2 = torch.tanh((z2**2) * (1 - z2) + self.fc2.bias)
        return self.fc3(h2)

class NetV2(nn.Module): # Формула: z^3 + wz + b
    def __init__(self, n=100):
        super().__init__()
        self.fc1 = nn.Linear(1, n); self.fc2 = nn.Linear(n, n); self.fc3 = nn.Linear(n, 1)
        self.w_f1 = nn.Parameter(torch.randn(n) * 0.1); self.w_f2 = nn.Parameter(torch.randn(n) * 0.1)
    def forward(self, x):
        z1 = self.fc1(x); h1 = torch.tanh(torch.pow(z1, 3) + z1 * self.w_f1 + self.fc1.bias)
        z2 = self.fc2(h1); h2 = torch.tanh(torch.pow(z2, 3) + z2 * self.w_f2 + self.fc2.bias)
        return self.fc3(h2)

# --- 10 ТЕСТОВЫХ СЦЕНАРИЕВ ---

x = torch.linspace(-3, 3, 200).view(-1, 1)
targets = {
    "1. Чистый Синус": torch.sin(x),
    "2. Квадратный Синус": torch.sin(x**2),
    "3. Шумные данные": torch.sin(x) + torch.randn(x.size()) * 0.1,
    "4. Экспонента": torch.exp(-x**2),
    "5. Пилообразная": x - torch.floor(x),
    "6. Абсолютное значение": torch.abs(x),
    "7. Ступенчатая": (x > 0).float(),
    "8. Комбо (Sin+Cos)": torch.sin(x) * torch.cos(x*2),
    "9. Логарифм": torch.log(torch.abs(x) + 1),
    "10. Квадратичная": x**2 / 9
}

def train(model, target):
    opt = optim.Adam(model.parameters(), lr=0.01)
    crit = nn.MSELoss()
    for _ in range(800):
        opt.zero_grad(); loss = crit(model(x), target); loss.backward(); opt.step()
    return loss.item()

# --- ЗАПУСК БИТВЫ ---

print(f"{'Тест':<25} | {'V1 Loss':<12} | {'V2 Loss':<12} | {'Победитель'}")
print("-" * 70)

for name, target in targets.items():
    l1 = train(NetV1(), target)
    l2 = train(NetV2(), target)
    winner = "V1 (z^2)" if l1 < l2 else "V2 (z^3)"
    print(f"{name:<25} | {l1:.8f} | {l2:.8f} | {winner}")
