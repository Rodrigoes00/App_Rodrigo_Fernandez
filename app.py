import streamlit as st
import numpy as np
import pandas as pd

#CLASE
class Actividad:
    def __init__(self,nombre,tipo,ppto,gasto_real):
        self.nombre =       nombre
        self.tipo =         tipo
        self.ppto =         ppto
        self.gasto_real =   gasto_real
    
    def esta_en_ppto(self):
        return self.gasto_real <= self.ppto
            
    def mostrar_info(self):
        return f"La actividad {self.nombre} es del {self.tipo} y tiene un presupuesto de $ {self.ppto} con un gasto de $ {self.gasto_real}"

#FUNCIONES
#############################
def calcular_retorno (actividad,tasa,meses):
    retorno = actividad["presupuesto"]*tasa*meses
    return(retorno)

#STREAMLIT
#############################
st.title("¡BIENVENIDO A MI PRIMERA APP!")

st.sidebar.image("Logo_DMC.png")
st.sidebar.title("Módulos")
pagina = st.sidebar.selectbox("Elige el módulo a visualizar:", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

#HOME
#############################
if pagina == "Home":
    st.header("Proyecto Aplicado en Streamlit")
    st.write("Curso: Python fundamentals")
    st.write("Año: 2026")
    st.write("Objetivo del proyecto: Realizar una apicación para portafolio personal")
    st.write("Tecnologías: Python, Streamlit")
    st.write("Elaborado por Rodrigo Fernandez Arce")
    #st.markdown("1️⃣ **Clase Persona**: Para manejar información personal (nombre, edad, profesión).")

#EJERCICIO 1
#############################
elif pagina == "Ejercicio 1":
    st.subheader("Variables y Condicionales")
    ppto =              st.number_input("Ingrese su presupuesto:",step=0.01)
    gasto =             st.number_input("Ingrese su gasto:",step=0.01)
    dif = gasto - ppto

    if st.button("Evaluar"):
        if gasto <= ppto:
            st.write("El presupuesto es mayor por $",(-dif))
            st.success("Gasto dentro del presupuesto")
        else:
            st.write("El gasto es mayor por $",(dif))
            st.warning("El presupuesto fue excedido")

#EJERCICIO 2
#############################
elif pagina == "Ejercicio 2":
    st.subheader("Listas y Diccionarios")
    act =               st.text_input("Ingresa nombre de la actividad:")
    tipo =              st.selectbox("Elige el tipo de actividad",["Tipo A","Tipo B","Tipo C"])
    ppto =              st.number_input("Ingresa el presupuesto:",min_value=0)
    gasto_real =        st.number_input("Ingresa el gasto real:",min_value=0)
    
    
    if "actividades" not in st.session_state:
        st.session_state.actividades = []
        
    if st.button("Agregar"):
        actividad = {"nombre": act,"tipo": tipo,"presupuesto": ppto,"gasto_real": gasto_real}
        
        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente")
 
    if st.session_state.actividades:
        st.subheader("Lista de Actividades Registradas")

        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df)

        st.subheader("Estado de cada actividad")
        for actividad in st.session_state.actividades:

            if actividad["gasto_real"] <= actividad["presupuesto"]:
                estado = "Gasto dentro del presupuesto"
            else:
                estado = "Gasto excede el presupuesto"

            st.write(f"Estado de la actividad '{actividad['nombre']}': {estado}")

#EJERCICIO 3
#############################
elif pagina == "Ejercicio 3":
    st.subheader("Funciones y Programación Funcional")
    tasa =              st.slider("Ingrese la tasa:",min_value=0.0,max_value=30.0,value=0.1,step=0.1)
    meses =             st.number_input("Cantidad de meses:",min_value=0,step=1)
    
    if st.button("Calcular"):
        retornos = list(map(lambda actividad: {"actividad":         actividad["nombre"],
                                               "retorno":           calcular_retorno(actividad, tasa, meses)},
                            st.session_state.actividades
                            )
                        )
    
    for r in retornos:
        st.write(f"El retorno esperado para la actividad '{r['actividad']}' es: ${r['retorno']:.2f}")

#EJERCICIO 4
#############################
elif pagina == "Ejercicio 4":
    st.header("Programación Orientada a Objetos (POO)")

    actividades_objetos =   [Actividad(act["nombre"],act["tipo"],act["presupuesto"],act["gasto_real"])
                             for act in st.session_state.actividades
                            ]   
    
    if st.button("Analizar"):
        for Actividad in actividades_objetos:
            st.write(Actividad.mostrar_info())

            if Actividad.esta_en_ppto():
                st.success("Está dentro del presupuesto")
            else:
                st.warning("Excede el presupuesto")
