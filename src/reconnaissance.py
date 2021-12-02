from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im_bin = image.binarisation(S)
    im_loc = im_bin.localisation()
    sim = 0
    sim_indice = 0
    for i in (liste_modeles) :
        im_res = im_loc.resize(i.H,i.W)
        if sim < im_res.similitude(i) :
            sim = im_res.similitude(i)
            sim_indice = i
    
    return sim_indice

