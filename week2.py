import nltk
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Tải xuống bộ dữ liệu cần thiết (chạy một lần nếu cần)
nltk.download('punkt_tab')

# Văn bản mẫu để huấn luyện mô hình
text = "The water of Walden Pond is so beautifully blue. The water of the lake is clear and clean. The water of the lake is deep and cold."

# Tiền xử lý văn bản
tokens = word_tokenize(text.lower())  # Chuyển thành chữ thường và token hóa

# Tạo trigram từ văn bản
trigrams = list(ngrams(tokens, 3))

# Xây dựng mô hình n-gram
def build_trigram_model(trigrams):
    model = defaultdict(Counter)
    for w1, w2, w3 in trigrams:
        model[(w1, w2)][w3] += 1
    return model

# Huấn luyện mô hình
trigram_model = build_trigram_model(trigrams)

# Hàm dự đoán từ tiếp theo
def predict_next_word(model, w1, w2):
    if (w1, w2) in model:
        possible_words = model[(w1, w2)]
        total_count = sum(possible_words.values())
        probabilities = {word: count / total_count for word, count in possible_words.items()}
        return probabilities
    else:
        return None

# Hàm vẽ biểu đồ phân phối xác suất
def plot_distribution(probabilities, w1, w2):
    if probabilities:
        words, probs = zip(*probabilities.items())
        plt.figure(figsize=(8, 4))
        plt.bar(words, probs, color='skyblue')
        plt.xlabel("Từ tiếp theo")
        plt.ylabel("Xác suất")
        plt.title(f"Phân phối xác suất từ tiếp theo sau '{w1} {w2}'")
        plt.show()
    else:
        print("Không có dữ liệu dự đoán cho cặp từ này.")

# Ví dụ dự đoán
test_w1, test_w2 = "beautiful", "blue"
predicted_probs = predict_next_word(trigram_model, test_w1, test_w2)
plot_distribution(predicted_probs, test_w1, test_w2)
