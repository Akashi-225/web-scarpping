from bs4 import *
import requests
import os


def folder_create(images,url):#fonction de creation d'un dossier qui contien des images telecharger
	try: #essaie de creer le dossier
		#folder_name = input("Entrer le nom du dossier:- ")#entrer le nom du dossier a creer
		folder_name = 	url[8:-4]	#"https://www.exemple.com/index.html"=>"www.exemple.com/index".
   # folder creation
		os.makedirs(folder_name) #creation sur le bureau

	except:#gerer l'execption dans le cas ou le dossier existe deja
		print("un dossier existe déja avec ce nom")
		folder_create()#creer un autre  dossier 

	
	download_images(images, folder_name)#telecharger les images dans le dossier



def download_images(images, folder_name):#fonctions de telechargement

	
	count = 0 #compteur a 0


	print(f"Nombre d'images trouvé est {len(images)} ")

	
	if len(images) != 0:#si nombre d'images different de 0
		for i, image in enumerate(images): #pour toute images 
			

			try:
				
				image_link = image["data-srcset"]
				
			
			except:
				try:
					
					image_link = image["data-src"]
				except:
					try:
						
						image_link = image["data-fallback-src"]
					except:
						try:
							
							image_link = image["src"]

						
						except:
							pass

			
			try:
				r = requests.get(image_link).content
				try:

					
					r = str(r, 'utf-8')

				except  UnicodeDecodeError:

					
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					
					count += 1
			except:
				pass

		
		if count == len(images):
			print("Toutes les images ont été telechargé!")
			
		
		else:
			print(f"nombre Total {count} Image superieur a  {len(images)}")


def main(url):

	
	r = requests.get(url)#recuperer l'url

	
	soup = BeautifulSoup(r.content, 'html.parser')#scrapping du lien 

	
	images = soup.findAll('img')

	
	folder_create(images,url)



url = input("Entrer l' URL:- ")


main(url)
#example : https://www.example.com/telephone-tablette/