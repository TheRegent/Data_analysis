import math as mt
import random

import matplotlib.pyplot as plt
import numpy as np


def smooth_mnk(sample: np.ndarray):
    Yin = np.zeros((sample.size, 1))
    F = np.ones((sample.size, 3))

    for i in range(sample.size):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(sample[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)

    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)

    Yout = F.dot(C)

    return Yout


def anomaly_delete_sliding_window(sample: np.ndarray, window_size: int) -> tuple[np.ndarray, np.ndarray]:
    k = int(len(sample) * (window_size / 2 / 100))

    get_bands = lambda x: (np.mean(x) + 3 * np.std(x), np.mean(x) - 3 * np.std(x))

    bands = [
        get_bands(
            sample[
                range(
                    0 if i - k < 0 else i - k,
                    i + k if i + k < sample.size else sample.size
                )
            ]
        )
        for i in range(0, sample.size)
    ]

    upper, lower = zip(*bands)

    anomalies = (sample > upper) | (sample < lower)
    not_anomalies = np.array([not anomaly for anomaly in anomalies])

    return sample[not_anomalies], np.array([index for index in range(not_anomalies.size) if not not_anomalies[index]])


# ----------------------------------------------------------------------------------------------------------------------
#                                               Змінні налаштування
# ----------------------------------------------------------------------------------------------------------------------
sample_median = 0  # Мат. очікування похибки розподіленої за нормальним законом
sample_std = 5  # СКВ похибки розподіленої за нормальним законом
sample_len = 10000  # Кількість елементів у виборці
anomaly_percentage = 10  # Відсоток аномальних вимірів


# ----------------------------------------------------------------------------------------------------------------------
#                                                      Аномальні виміри
# ----------------------------------------------------------------------------------------------------------------------
# Кількість аномалій на вибірку
anomalies_number = int((sample_len * anomaly_percentage) / 100)

# Порядкові номери аномальних вимірів розподілені рівномірно
anomaly_indexes = random.sample(range(sample_len), anomalies_number)

# Аномальна похибка вимірів розподілена за нормальним законом з СКВ = 3 * sigma
anomaly_values = np.random.normal(sample_median, (sample_std * 3), anomalies_number)


# ----------------------------------------------------------------------------------------------------------------------
#                                                      Похибки
# ----------------------------------------------------------------------------------------------------------------------
# Похибка без АВ розподілена за нормальним законом
noise_sample = np.random.normal(sample_median, sample_std, sample_len)

# Копія похибки без АВ
noise_sample_anomalous = noise_sample.copy()

# Заміна усіх похибок на аномальні похибки за аномальними індексами
for num_of_anomaly, anomaly_index in enumerate(anomaly_indexes):
    noise_sample_anomalous[anomaly_index] = anomaly_values[num_of_anomaly]


# ----------------------------------------------------------------------------------------------------------------------
#                                                      Моделі
# ----------------------------------------------------------------------------------------------------------------------

# Ідеальна модель квадратичного процессу
model_ideal = np.zeros(sample_len)

# Модель з похибкою без АВ
model_noised = np.zeros(sample_len)

# Модель з аномальними похибками
model_anomalous = np.zeros(sample_len)


# Генерація моделей
for i in range(sample_len):
    model_ideal[i] = (0.000_000_5 * i * i)  # Ідеальне значення
    model_noised[i] = model_ideal[i] + noise_sample[i]  # Ідеальне значення + Похибка
    model_anomalous[i] = model_ideal[i] + noise_sample_anomalous[i]  # # Ідеальне значення + Похибка + АВ


# Модель очищена від АВ та індекси видалених АВ
model_cleared, deleted_indexes = anomaly_delete_sliding_window(model_anomalous, window_size=5)


# Згладжена модель
model_smoothed = smooth_mnk(model_cleared)

# Похибка згладженої моделі
noise_sample_smoothed = np.zeros(sample_len - deleted_indexes.size)

new_index = 0  # Новий іднекс виміру ідеальної моделі після видалення АВ

for old_index in range(model_ideal.size):
    if old_index not in deleted_indexes:
        noise_sample_smoothed[new_index] = abs(model_ideal[old_index] - model_smoothed[new_index])
        new_index += 1


# ----------------------------------------------------------------------------------------------------------------------
#                                   Статистичні характеристики випадкової похибки
# ----------------------------------------------------------------------------------------------------------------------
print('\n' + ("-" * 20) + "ВВ похибки" + ("-" * 20))
print("Матиматичне сподівання ВВ похибки: ", np.median(noise_sample))
print("Дисперсія ВВ похибки: ", np.var(noise_sample))
print("СКВ ВВ похибки: ", mt.sqrt(np.var(noise_sample)))


# ----------------------------------------------------------------------------------------------------------------------
#                                   Статистичні характеристики вибірки з похибкою без АВ
# ----------------------------------------------------------------------------------------------------------------------
print('\n' + ("-" * 20) + "Вибірка з похибкою без АВ" + ("-" * 20))
print("Матиматичне сподівання вибірки з похибкою без АВ: ", np.median(model_noised))
print("Дисперсія вибірки з похибкою без АВ: ", np.var(model_noised))
print("СКВ вибірки з похибкою без АВ: ", mt.sqrt(np.var(model_noised)))


# ----------------------------------------------------------------------------------------------------------------------
#                                   Статистичні характеристики вибірки з похибкою та АВ
# ----------------------------------------------------------------------------------------------------------------------
print('\n' + ("-" * 20) + "Вибірка з похибкою та АВ" + ("-" * 20))
print("Матиматичне сподівання вибірки з похибкою та АВ: ", np.median(model_anomalous))
print("Дисперсія вибірки з похибкою та АВ: ", np.var(model_anomalous))
print("СКВ вибірки з похибкою та АВ: ", mt.sqrt(np.var(model_anomalous)))


# ----------------------------------------------------------------------------------------------------------------------
#                  Статистичні характеристики вибірки після видалення АВ та згаджування МНК
# ----------------------------------------------------------------------------------------------------------------------
print('\n' + ("-" * 20) + "Згладжена вибірка" + ("-" * 20))
print("Матиматичне сподівання згладженої вибірки: ", np.median(model_smoothed))
print("Дисперсія згладженої вибірки: ", np.var(model_smoothed))
print("СКВ згладженої вибірки: ", mt.sqrt(np.var(model_smoothed)))


# ----------------------------------------------------------------------------------------------------------------------
#                                                          Графіки
# ----------------------------------------------------------------------------------------------------------------------
plt.plot(model_noised, color='blue', label='Модель з похибкою без АВ')
plt.plot(model_anomalous, color='red', alpha=.8, label='Модель с похибкою та АВ')
plt.plot(model_ideal, color='orange', label='Модель без похибки та АВ')
plt.plot(model_smoothed, color="green", alpha=0.5, label="Згладжена модель")
plt.legend()
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
#                                                          Гістограми
# ----------------------------------------------------------------------------------------------------------------------
plt.hist(noise_sample, color='blue', label='Нормальна похибка', bins=100)
plt.hist(noise_sample_anomalous, color='red', alpha=.5, label='Нормальна похибка + АВ', bins=100)
plt.hist(noise_sample_smoothed, color='yellow', label='Похибка після МНК', bins=100)
plt.legend()
plt.show()

