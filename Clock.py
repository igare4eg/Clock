import tkinter as tk
import time

class Clock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Часы")

        # Создаем Label для отображения времени
        self.time_label = tk.Label(self.root, bg='black', font=('Arial', 80), fg='white')
        self.time_label.pack()

        # Запускаем таймер обновления времени
        self.update_time()

        # Запускаем главный цикл приложения
        self.root.mainloop()

    def update_time(self):
        # Обновляем время
        current_time = time.strftime('%H:%M:%S')
        self.time_label.configure(text=current_time)

        # Запускаем обновление времени через 1 секунду
        self.root.after(1000, self.update_time)

# Создаем экземпляр класса Clock
clock = Clock()
