from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        #creation d'une image vide
        im_bin = Image()
        # affectation à l'image d'un tableau de pixelsde même taille
        # que self dont les intensités, de type uint8 (8bits non signés),
        # sont mises à 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        #TODO:boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        for i in range (self.H) :
            for j in range (self.W) :
                if self.pixels[i,j] >= S :
                    im_bin.pixels[i][j] = 255
                else :
                    im_bin.pixels[i][j] = 0
        return im_bin
        
    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        imagecentre = Image()
        
        lmax = 0
        lmin = self.H
        cmax = 0
        cmin = self.W
        for i in range(self.H) :
            for j in range(self.W) :
                if self.pixels[i][j] == 0 :
                    if i < lmin :
                        lmin = i
                    if i > lmax :
                        lmax = i
                    if j < cmin :
                        cmin = j
                    if j > cmax :
                        cmax = j
                
        imagecentre.set_pixels(self.pixels[lmin:lmax ,cmin:cmax])
        return imagecentre
    
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_res = Image()
        a = resize(self.pixels, (new_H,new_W), 0) 
        im_res.set_pixels(np.uint8(a*255))
        return im_res

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        if self.H == im.H and self.W == im.W :
            p_commun = 0
            for i in range(self.H) :
                for j in range (self.W) :
                    if self.pixels[i][j] == im.pixels[i][j] :
                        p_commun += 1
        
        return (p_commun/(self.W * self.H))

