import tkinter as tk
from tkinter import messagebox
import random


        # Колода
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("ОЧКО 21 — Казино")
        self.root.geometry("700x600")
        self.root.configure(bg='#1e3a2f')

        # Переменные
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False

        # Интерфейс
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Заголовок
        title = tk.Label(self.root, text="♠ ♥ ОЧКО 21 ♦ ♣", font=('Helvetica', 24, 'bold'),
                         fg='#ffd700', bg='#1e3a2f')
        title.pack(pady=10)

        # Рамка для карт дилера
        self.dealer_frame = tk.LabelFrame(self.root, text="Дилер", font=('Arial', 14, 'bold'),
                                          fg='white', bg='#2a4d3e', bd=3, relief='ridge')
        self.dealer_frame.pack(pady=10, padx=20, fill='x')

        self.dealer_label = tk.Label(self.dealer_frame, text="", font=('Arial', 16),
                                     fg='white', bg='#2a4d3e', justify='left')
        self.dealer_label.pack(pady=10, padx=10)

        # Рамка для карт игрока
        self.player_frame = tk.LabelFrame(self.root, text="Ваши карты", font=('Arial', 14, 'bold'),
                                          fg='white', bg='#2a4d3e', bd=3, relief='ridge')
        self.player_frame.pack(pady=10, padx=20, fill='x')

        self.player_label = tk.Label(self.player_frame, text="", font=('Arial', 16),
                                     fg='white', bg='#2a4d3e', justify='left')
        self.player_label.pack(pady=10, padx=10)

        # Счёт
        self.score_frame = tk.Frame(self.root, bg='#1e3a2f')
        self.score_frame.pack(pady=5)

        self.player_score_label = tk.Label(self.score_frame, text="Ваши очки: 0",
                                           font=('Arial', 14), fg='#aef0c8', bg='#1e3a2f')
        self.player_score_label.pack(side='left', padx=20)

        self.dealer_score_label = tk.Label(self.score_frame, text="Очки дилера: ?",
                                           font=('Arial', 14), fg='#f0c8a0', bg='#1e3a2f')
        self.dealer_score_label.pack(side='right', padx=20)

        # Кнопки управления
        self.btn_frame = tk.Frame(self.root, bg='#1e3a2f')
        self.btn_frame.pack(pady=15)

        self.hit_btn = tk.Button(self.btn_frame, text="ВЗЯТЬ КАРТУ", font=('Arial', 12, 'bold'),
                                 bg='#2e7d5e', fg='white', padx=20, pady=8,
                                 command=self.hit, activebackground='#3fa37c')
        self.hit_btn.pack(side='left', padx=10)

        self.stand_btn = tk.Button(self.btn_frame, text="ОСТАНОВИТЬСЯ", font=('Arial', 12, 'bold'),
                                   bg='#8b4c4c', fg='white', padx=20, pady=8,
                                   command=self.stand, activebackground='#b55a5a')
        self.stand_btn.pack(side='left', padx=10)

        self.new_btn = tk.Button(self.btn_frame, text="НОВАЯ ИГРА", font=('Arial', 12, 'bold'),
                                 bg='#4a6b8a', fg='white', padx=20, pady=8,
                                 command=self.new_game, activebackground='#5f8ab5')
        self.new_btn.pack(side='left', padx=10)

        # Статус
        self.status_label = tk.Label(self.root, text="", font=('Arial', 14, 'italic'),
                                     fg='#ffddaa', bg='#1e3a2f')
        self.status_label.pack(pady=10)