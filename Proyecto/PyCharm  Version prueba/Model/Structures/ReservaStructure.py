# -*- coding: cp1252 -*- 
class Reserva(object):
	'''
	Clase con Constructor, Getters y Setters
	de la relacion Reserva
	'''
	#Constructor con paso de parametros 
	def __init__(self, idReserva= None, idEspacio= None, idNivel= None, idBloque= None, idSede= None, idOrgCreador= None, idOrgConsecutivo= None, idUsuario= None, idDiasReserva= None, fechaInicio= None, fechaFin= None, horaInicio= None, horaFin= None, fechaReserva= None):
		self.idReserva = idReserva 
		self.idEspacio = idEspacio 
		self.idNivel = idNivel 
		self.idBloque = idBloque 
		self.idSede = idSede 
		self.idOrgCreador = idOrgCreador 
		self.idOrgConsecutivo = idOrgConsecutivo 
		self.idUsuario = idUsuario 
		self.idDiasReserva = idDiasReserva 
		self.fechaInicio = fechaInicio 
		self.fechaFin = fechaFin 
		self.horaInicio = horaInicio 
		self.horaFin = horaFin 
		self.fechaReserva = fechaReserva 


	#Getters y Setters de idReserva

	def getIdReserva(self):
		return self.idReserva
	def setIdReserva(self,idReserva):
		self.idReserva = idReserva



	#Getters y Setters de idEspacio

	def getIdEspacio(self):
		return self.idEspacio
	def setIdEspacio(self,idEspacio):
		self.idEspacio = idEspacio



	#Getters y Setters de idNivel

	def getIdNivel(self):
		return self.idNivel
	def setIdNivel(self,idNivel):
		self.idNivel = idNivel



	#Getters y Setters de idBloque

	def getIdBloque(self):
		return self.idBloque
	def setIdBloque(self,idBloque):
		self.idBloque = idBloque



	#Getters y Setters de idSede

	def getIdSede(self):
		return self.idSede
	def setIdSede(self,idSede):
		self.idSede = idSede



	#Getters y Setters de idOrgCreador

	def getIdOrgCreador(self):
		return self.idOrgCreador
	def setIdOrgCreador(self,idOrgCreador):
		self.idOrgCreador = idOrgCreador



	#Getters y Setters de idOrgConsecutivo

	def getIdOrgConsecutivo(self):
		return self.idOrgConsecutivo
	def setIdOrgConsecutivo(self,idOrgConsecutivo):
		self.idOrgConsecutivo = idOrgConsecutivo



	#Getters y Setters de idUsuario

	def getIdUsuario(self):
		return self.idUsuario
	def setIdUsuario(self,idUsuario):
		self.idUsuario = idUsuario



	#Getters y Setters de idDiasReserva

	def getIdDiasReserva(self):
		return self.idDiasReserva
	def setIdDiasReserva(self,idDiasReserva):
		self.idDiasReserva = idDiasReserva



	#Getters y Setters de fechaInicio

	def getFechaInicio(self):
		return self.fechaInicio
	def setFechaInicio(self,fechaInicio):
		self.fechaInicio = fechaInicio



	#Getters y Setters de fechaFin

	def getFechaFin(self):
		return self.fechaFin
	def setFechaFin(self,fechaFin):
		self.fechaFin = fechaFin



	#Getters y Setters de horaInicio

	def getHoraInicio(self):
		return self.horaInicio
	def setHoraInicio(self,horaInicio):
		self.horaInicio = horaInicio



	#Getters y Setters de horaFin

	def getHoraFin(self):
		return self.horaFin
	def setHoraFin(self,horaFin):
		self.horaFin = horaFin



	#Getters y Setters de fechaReserva

	def getFechaReserva(self):
		return self.fechaReserva
	def setFechaReserva(self,fechaReserva):
		self.fechaReserva = fechaReserva




#Autogenerado: 05/09/17 23:48:59