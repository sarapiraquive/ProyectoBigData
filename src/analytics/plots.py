import matplotlib.pyplot as plt
import seaborn as sns
import folium

# 1. Conteo diario
def plot_daily_crimes(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["day"], df["crimes"], label="Crímenes diarios")
    plt.title("Tendencia de crímenes por día en 2025")
    plt.xlabel("Fecha")
    plt.ylabel("Número de crímenes")
    plt.grid(True)
    plt.legend()
    plt.show()

# 2. Mapa
def plot_map(df, output_file="mapa_crimenes.html"):
    m = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=12)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=2,
            color="red",
            fill=True,
            fill_opacity=0.6
        ).add_to(m)
    m.save(output_file)
    print(f"Mapa guardado en {output_file}")

# 3. Top wards
def plot_top_wards(df):
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x="ward", y="total_crimes", palette="viridis")
    plt.title("Top 10 Wards con más delitos")
    plt.xlabel("Ward")
    plt.ylabel("Número de crímenes")
    plt.show()

# 4. Delitos más comunes
def plot_top_offenses(df):
    plt.figure(figsize=(12,6))
    sns.barplot(data=df, x="total", y="offense", palette="mako")
    plt.title("Delitos más comunes")
    plt.xlabel("Número de crímenes")
    plt.ylabel("Tipo de delito")
    plt.show()

# 5. Distribución por turno
def plot_shift_distribution(df):
    plt.figure(figsize=(8,6))
    sns.barplot(data=df, x="shift", y="total", palette="Set2")
    plt.title("Distribución de crímenes por turno")
    plt.xlabel("Turno")
    plt.ylabel("Número de crímenes")
    plt.show()