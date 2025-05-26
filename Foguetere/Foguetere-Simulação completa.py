import math

def simular_voo(params):
    g = 9.81
    v_e = math.sqrt(2 * params['pressao'] * 1000 / params['massa'])  # estimativa
    angulo_rad = math.radians(params['angulo'])

    v0_x = v_e * math.cos(angulo_rad)
    v0_y = v_e * math.sin(angulo_rad)

    tempo_total = 2 * v0_y / g
    altura_max = (v0_y ** 2) / (2 * g)
    alcance = v0_x * tempo_total

    trajetoria = []
    t = 0
    dt = 0.1
    while t <= tempo_total:
        y = v0_y * t - 0.5 * g * t ** 2
        trajetoria.append(max(0, y))
        t += dt

    return {
        'velocidade_maxima': v_e,
        'altura_maxima': altura_max,
        'tempo_total': tempo_total,
        'alcance': alcance,
        'trajetoria': trajetoria
    }
