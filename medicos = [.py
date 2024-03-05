medicos = [
  {"nombre": "Dr.general 1", "especialidad":"general","tiempo_consulta": 15},
  {"nombre": "Dr.general 2", "especialidad":"general","tiempo_consulta": 15},
  {"nombre": "Dr.general 3", "especialidad":"general","tiempo_consulta": 15},
  {"nombre": "Dentista", "especialidad":"Dientes","tiempo_consulta": 30},
  {"nombre": "Oftalmologia", "especialidad":"ojos","tiempo_consulta":20}
]
citas = []

def agregar_cita(hora,medico_id):
  cita = {"hora": hora, "medico_id": medico_id }
  citas.append(cita)

def eliminar_cita(hora, medico_id):
  global citas
  citas = [cita for cita in citas if cita["hora"] != hora or cita["medico_id"] != medico_id ]

def editar_cita(hora_antigua, hora_nueva, medico_id_antiguo, medico_id_nuevo):
  global citas
  for i, cita in enumerate(citas):
    if cita["hora"] == hora_antigua and cita["medico_id"] == medico_id_antiguo:
      citas[i]["hora"]={"hora":hora_nueva,"medico_id":medico_id_nuevo}

def mostrar_agenda ():
  for cita in citas:
    medico = next((medico for medico in medicos if medico["id"]==cita["medico_id"]),None)