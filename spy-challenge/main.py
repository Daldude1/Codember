import requests

# Descarga el archivo con las políticas y claves de cifrado
url = "https://codember.dev/data/encryption_policies.txt"
response = requests.get(url)
data = response.text

# Divide el archivo en líneas y procesa cada una
lines = data.split("\n")
invalid_keys = []

for line in lines:
    # Divide la línea en la política y la clave
    policy, key = line.split(":")

    # Divide la política en el rango y el carácter
    range_, char = policy.split()
    min_, max_ = map(int, range_.split("-"))

    # Cuenta cuántas veces aparece el carácter en la clave
    count = key.count(char)

    # Verifica si la clave es válida según la política
    if count < min_ or count > max_:
        invalid_keys.append(key)

# Devuelve la clave inválida número 42
if len(invalid_keys) >= 42:
    invalid_key_42 = invalid_keys[41]
    print("La clave inválida número 42 es:", invalid_key_42)
else:
    print("No hay suficientes claves inválidas para encontrar la número 42")
