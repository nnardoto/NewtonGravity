import numpy as np
import tkinter


class CorpoCeleste:
	'''
	Define as propriedades básicas de cada corpo celeste individualmente
	'''
	Nome  = 'Nome'
	Raio  = 0.0
	Massa = 0.0
	R     = np.array([0.0, 0.0])
	dR    = np.array([0.0, 0.0])

	def __init__(self, Nome, Color, Raio, Massa, R, dR):
		self.Nome  = Nome
		self.Raio  = Raio
		self.Color = Color
		self.Massa = Massa
		self.R     = np.array(R)
		self.dR    = np.array(dR)

class Universo(tkinter.Tk):
	'''
	Gerencia as propriedades gerais do universo, bem como as interações entre os corpos celestes inseridos nele
	'''
	Lista_Corpos = []


	G_SI        = 6.6743E-11
	Massa_Terra = 5.9742E+24
	Raio_Terra  = 6.371E+3
	Terra_Sol   = 1.496E11
	G_BARRA     = G_SI*Massa_Terra**2/(Terra_Sol**2) 



	def __init__(self, G = G_BARRA):
		'''
		Inicializador da classe Universo, Define o Background,  
		'''
		tkinter.Tk.__init__(self)
		self.wm_title("Meu Universo")
		self.Background = tkinter.Canvas(self, bg = 'black', height = 1200, width = 1200)

		self.Background.pack()


	def Start(self):
		'''
		Função para inicializar o universo
		'''
		self.TicTac()
		self.mainloop()	



	def Add_Corpos(self, Lista_Corpos):
		'''
		Função para adicionar corpos no universo
		'''
		for i in Lista_Corpos:
			self.Lista_Corpos.append(i)

	def Draw(self):
		'''
		Função para defiir regras de desenho no universo
		'''
		self.Background.delete('all')
		
		for i in self.Lista_Corpos:
			self.S = 10
			xscale = 200
			xmm    = i.R[0]*xscale-self.S*i.Raio + 600
			xMM    = i.R[0]*xscale+self.S*i.Raio + 600

			ymm    = i.R[1]*xscale-self.S*i.Raio + 500
			yMM    = i.R[1]*xscale+self.S*i.Raio + 500



			self.Background.create_oval(xmm, ymm, xMM, yMM, fill = i.Color)


	def EvoluirNoTempo(self, dt):
		'''
		Função para realizar integração simples (Euler) para evoluir o sistema no tempo
		'''
		
		N = len(self.Lista_Corpos)
		xForce = np.zeros((N, N))
		yForce = np.zeros((N, N))


		# Calcula as Forças Abaixo da Diagonal
		for i in range(N):
			for j in range(i):
				G           = self.G_BARRA 
				m1			= self.Lista_Corpos[i].Massa
				m2			= self.Lista_Corpos[j].Massa
				D       	= np.linalg.norm(self.Lista_Corpos[i].R - self.Lista_Corpos[j].R)
				vD          = (self.Lista_Corpos[i].R - self.Lista_Corpos[j].R) / D
				
				# Módulo da Força
				xForce[i, j] = G*m1*m2/D**2 * vD[0]
				yForce[i, j] = G*m1*m2/D**2 * vD[1]

	    # Completa a Matriz
		for i in range(N):
			for j in range(i):
				xForce[j, i] = -xForce[i, j]
				yForce[j, i] = -yForce[i, j]


		for i in range(N):
			xSumF = np.sum(xForce[:, i])
			ySumF = np.sum(yForce[:, i])

			m			= self.Lista_Corpos[i].Massa * 5.9742E+24

			self.Lista_Corpos[i].dR = self.Lista_Corpos[i].dR + (xSumF/m)*dt * np.array([1, 0]) + (ySumF/m)*dt * np.array([0, 1])
			self.Lista_Corpos[i].R  = self.Lista_Corpos[i].R + self.Lista_Corpos[i].dR*dt




	def TicTac(self):
		'''
		TicTac Função que Controla os Steps
		'''
		self.Draw()
		self.EvoluirNoTempo(1E-2)
		self.Background.after(10, self.TicTac)

	def Listar_Universo(self):
		'''
		Função de Debug, Lista corpos no universo
		'''
		for corpo in self.Lista_Corpos:
			print(corpo.Nome)
