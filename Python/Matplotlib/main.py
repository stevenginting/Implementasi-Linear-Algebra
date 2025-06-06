import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# 1. Visualisasi Persegi
def visualisasi_persegi(sisi=4):
    fig, ax = plt.subplots()
    square = plt.Rectangle((0, 0), sisi, sisi, fill=True, color='skyblue', edgecolor='black')
    ax.add_patch(square)
    
    # Tambahkan teks keliling dan luas
    keliling = 4 * sisi
    luas = sisi * sisi
    ax.text(0.1, sisi + 0.5, f'Keliling = {keliling}', fontsize=12)
    ax.text(0.1, sisi + 1, f'Luas = {luas}', fontsize=12)

    ax.set_xlim(-1, sisi + 2)
    ax.set_ylim(-1, sisi + 3)
    ax.set_aspect('equal')
    ax.set_title('Persegi: Luas & Keliling')
    plt.grid(True)
    plt.show()


# 2. Visualisasi Kubus
def visualisasi_kubus(sisi=4):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = [0, sisi]
    vertices = [
        [r[0], r[0], r[0]], [r[1], r[0], r[0]],
        [r[1], r[1], r[0]], [r[0], r[1], r[0]],
        [r[0], r[0], r[1]], [r[1], r[0], r[1]],
        [r[1], r[1], r[1]], [r[0], r[1], r[1]]
    ]

    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[4], vertices[7], vertices[3], vertices[0]]
    ]

    face_colors = ['skyblue'] * 6
    ax.add_collection3d(Poly3DCollection(faces, facecolors=face_colors, edgecolors='black', linewidths=1, alpha=0.8))

    luas_permukaan = 6 * (sisi ** 2)
    volume = sisi ** 3

    ax.text(0, 0, sisi + 1, f'Luas Permukaan = {luas_permukaan}', fontsize=10)
    ax.text(0, 0, sisi + 2, f'Volume = {volume}', fontsize=10)

    ax.set_xlim(0, sisi + 1)
    ax.set_ylim(0, sisi + 1)
    ax.set_zlim(0, sisi + 3)
    ax.set_title('Kubus: Luas Permukaan & Volume')
    plt.show()

# Tampilkan semuanya
visualisasi_persegi(4)
visualisasi_kubus(4)
