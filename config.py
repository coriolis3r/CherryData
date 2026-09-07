# config.py

# ==========================================
# DEFINICIÓN DE VOLTAJES NOMINALES GLOBALES
# ==========================================
VOLTAJE_NOMINAL_LINEA = 220.0  # V_nl (Línea a Línea)
VOLTAJE_NOMINAL_FASE = 127.0   # V_nf (Línea a Neutro)

# Rangos numéricos automáticos
limite_fase_inferior = round(VOLTAJE_NOMINAL_FASE * 0.90, 1)
limite_fase_superior = round(VOLTAJE_NOMINAL_FASE * 1.10, 1)

limite_linea_inferior = round(VOLTAJE_NOMINAL_LINEA * 0.90, 1)
limite_linea_superior = round(VOLTAJE_NOMINAL_LINEA * 1.10, 1)

columnas_seleccionadas = [
    "UA", "UB", "UC",
    "UAB", "UBC", "UCA",
    "FA",
    "U-Unb-Neg",
    "I-Unb-Neg",
    "UA-THD", "UB-THD", "UC-THD",
    "IA-THD", "IB-THD", "IC-THD",
    "IA", "IB", "IC",
    "PFTotal",
    "PSum",
    "QSum",
    "SSum",
    "IA-CF", "IB-CF", "IC-CF",
    "IA-KF", "IB-KF", "IC-KF"
]

configuracion_reporte = [
    {
        "titulo": "1. Perfil de Tensión de Fase (Fase-Neutro)",
        "variables": [("UA", "V1"), ("UB", "V2"), ("UC", "V3")],
        "ylabel": "Voltaje (V)",
        "archivo_img": "01_perfil_tension_fase.png",
        "descripcion": "Gráfica 1: Comportamiento del voltaje de fase en las tres líneas.",
        "requerimientos": {
            "Norma Aplicable": "Código de Red",
            "Rango de Aceptación / Límite": f"±10% ({limite_fase_inferior} V - {limite_fase_superior} V)",
            "Criterio de Aceptación": "El promedio y P95 deben mantenerse dentro del rango permitido."
        }
    },
    {
        "titulo": "2. Perfil de Tensión de Línea (Fase-Fase)",
        "variables": [("UAB", "V12"), ("UBC", "V23"), ("UCA", "V31")],
        "ylabel": "Voltaje (V)",
        "archivo_img": "02_perfil_tension_linea.png",
        "descripcion": "Gráfica 2: Comportamiento del voltaje de línea entre fases.",
        "requerimientos": {
            "Norma Aplicable": "Código de Red / ANSI C84.1",
            "Rango de Aceptación / Límite": f"±10% ({limite_linea_inferior} V - {limite_linea_superior} V)",
            "Criterio de Aceptación": "Los valores calculados no deben vulnerar los umbrales nominales de suministro."
        }
    },
    {
        "titulo": "3. Perfil de Frecuencia",
        "variables": [("FA", "Frecuencia")],
        "ylabel": "Frecuencia (Hz)",
        "archivo_img": "03_perfil_frecuencia.png",
        "descripcion": "Gráfica 3: Comportamiento de la frecuencia del sistema.",
        "requerimientos": {
            "Norma Aplicable": "Código de Red",
            "Rango de Aceptación / Límite": "59.00 Hz - 61.00 Hz",
            "Criterio de Aceptación": "El sistema debe operar de forma continua y estable en el rango establecido."
        }
    },
    {
        "titulo": "4. Desbalance de Tensión (Secuencia Negativa)",
        "variables": [("U-Unb-Neg", "U-Unb-Neg")],
        "ylabel": "Desbalance (%)",
        "archivo_img": "04_desbalance_tension.png",
        "descripcion": "Gráfica 4: Porcentaje de desbalance de tensión de secuencia negativa.",
        "requerimientos": {
            "Norma Aplicable": "IEEE 1159 / Código de Red",
            "Rango de Aceptación / Límite": "≤ 2.0 %",
            "Criterio de Aceptación": "El valor del percentil 95 (P95) no debe superar el límite fijado."
        }
    },
    {
        "titulo": "5. Desbalance de Corriente (Secuencia Negativa)",
        "variables": [("I-Unb-Neg", "I-Unb-Neg")],
        "ylabel": "Desbalance (%)",
        "archivo_img": "05_desbalance_corriente.png",
        "descripcion": "Gráfica 5: Porcentaje de desbalance de corriente de secuencia negativa.",
        "requerimientos": {
            "Norma Aplicable": "IEEE 141",
            "Rango de Aceptación / Límite": "≤ 10.0 %",
            "Criterio de Aceptación": "El valor de desbalance en condiciones operativas normales debe estar bajo el umbral."
        }
    },
    {
        "titulo": "6. Distorsión Armónica Total de Tensión (THD V)",
        "variables": [("UA-THD", "THD V1"), ("UB-THD", "THD V2"), ("UC-THD", "THD V3")],
        "ylabel": "THD (%)",
        "archivo_img": "06_thd_tension.png",
        "descripcion": "Gráfica 6: Distorsión armónica total de tensión por fase.",
        "requerimientos": {
            "Norma Aplicable": "IEEE 519",
            "Rango de Aceptación / Límite": "≤ 5.0 %",
            "Criterio de Aceptación": "La distorsión del voltaje P95 no debe comprometer la calidad de la onda."
        }
    },
    {
        "titulo": "7. Distorsión Armónica Total de Corriente (THD I)",
        "variables": [("IA-THD", "THD I1"), ("IB-THD", "THD I2"), ("IC-THD", "THD I3")],
        "ylabel": "THD (%)",
        "archivo_img": "07_thd_corriente.png",
        "descripcion": "Gráfica 7: Distorsión armónica total de corriente por fase.",
        "requerimientos": {
            "Norma Aplicable": "IEEE 519",
            "Rango de Aceptación / Límite": "≤ 20.0 %",
            "Criterio de Aceptación": "Los niveles de distorsión inyectados a la red deben permanecer bajo el 20% en el P95."
        }
    },
    {
        "titulo": "8. Perfil de Corriente de Línea",
        "variables": [("IA", "I1"), ("IB", "I2"), ("IC", "I3")],
        "ylabel": "Corriente (A)",
        "archivo_img": "08_perfil_corriente.png",
        "descripcion": "Gráfica 8: Comportamiento de la corriente en las tres fases.",
        "requerimientos": {
            "Norma Aplicable": "Capacidad de Conducción",
            "Rango de Aceptación / Límite": "Capacidad Nominal de Barras / Interruptor",
            "Criterio de Aceptación": "La corriente máxima registrada no debe superar la nominal de los equipos de protección."
        }
    },
    {
        "titulo": "9. Perfil del Factor de Potencia Total",
        "variables": [("PFTotal", "FP Total")],
        "ylabel": "Factor de Potencia",
        "archivo_img": "09_perfil_fp.png",
        "descripcion": "Gráfica 9: Evolución del factor de potencia total del sistema.",
        "requerimientos": {
            "Norma Aplicable": "Código de Red",
            "Rango de Aceptación / Límite": "> 0.97",
            "Criterio de Aceptación": "Debe mantenerse por encima de 0.97 al menos el 95% del tiempo evaluado."
        }
    },
    {
        "titulo": "10. Perfil de Potencia Activa Total",
        "variables": [("PSum", "P Total (kW)")],
        "ylabel": "Potencia Activa (kW)",
        "archivo_img": "10_perfil_potencia_activa.png",
        "descripcion": "Gráfica 10: Comportamiento de la potencia activa total demandada.",
        "requerimientos": {
            "Norma Aplicable": "Contrato de Suministro",
            "Rango de Aceptación / Límite": "Demanda Contratada (kW)",
            "Criterio de Aceptación": "La demanda máxima registrada no debe exceder el límite establecido con la suministradora."
        }
    },
    {
        "titulo": "11. Perfil de Potencia Reactiva Total",
        "variables": [("QSum", "Q Total (kVAR)")],
        "ylabel": "Potencia Reactiva (kVAR)",
        "archivo_img": "11_perfil_potencia_reactiva.png",
        "descripcion": "Gráfica 11: Comportamiento de la potencia reactiva total del sistema.",
        "requerimientos": {
            "Norma Aplicable": "Operación Interna",
            "Rango de Aceptación / Límite": "Control de Reactivos",
            "Criterio de Aceptación": "Mantener los niveles reactivos en rangos mínimos para evitar penalizaciones por bajo factor de potencia."
        }
    },
    {
        "titulo": "12. Perfil de Potencia Aparente Total",
        "variables": [("SSum", "S Total (kVA)")],
        "ylabel": "Potencia Aparente (kVA)",
        "archivo_img": "12_perfil_potencia_aparente.png",
        "descripcion": "Gráfica 12: Comportamiento de la potencia aparente total del sistema.",
        "requerimientos": {
            "Norma Aplicable": "Capacidad del Transformador",
            "Rango de Aceptación / Límite": "KVA Nominal del Transformador Principal",
            "Criterio de Aceptación": "El valor máximo alcanzado (SSum) debe permanecer por debajo de la capacidad crítica del equipo."
        }
    },
    {
        "titulo": "13. Perfil de Factor de Cresta de Corriente",
        "variables": [("IA-CF", "CF I1"), ("IB-CF", "CF I2"), ("IC-CF", "CF I3")],
        "ylabel": "Factor de Cresta",
        "archivo_img": "13_perfil_factor_cresta.png",
        "descripcion": "Gráfica 13: Comportamiento dinámico del factor de cresta por fase (Ref: 1.41 senoidal).",
        "requerimientos": {
            "Norma Aplicable": "Informativo / Cargas No Lineales",
            "Rango de Aceptación / Límite": "Ideal: 1.41 | Crítico: > 2.0",
            "Criterio de Aceptación": "Valores elevados indican presencia severa de armónicos y picos de corriente."
        }
    },
    {
        "titulo": "14. Perfil de Factor K de Corriente",
        "variables": [("IA-KF", "KF I1"), ("IB-KF", "KF I2"), ("IC-KF", "KF I3")],
        "ylabel": "Factor K",
        "archivo_img": "14_perfil_factor_k.png",
        "descripcion": "Gráfica 14: Comportamiento dinámico del Factor K por fase (Ref: ANSI/IEEE C57.110).",
        "requerimientos": {
            "Norma Aplicable": "ANSI/IEEE C57.110",
            "Rango de Aceptación / Límite": "Ideal: 1.0 | Informativo s/Diseño de Transformador",
            "Criterio de Aceptación": "Valores elevados indican calentamiento armónico severo en los devanados del trafo."
        }
    }
]
