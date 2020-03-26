# 1. Intro

- historique
  - 1922,  Otto Stern et Walther Gerlach
  - Expérience originale :  faisceau d'atomes d'argent dans leur état fondamental (moment cinétique $l = 0$ et moment magnétique $m = 0$) envoyés dans un champ magnétique non-uniforme, résultat : dévié en deux faisceaux.
  - Classiquement: le faisceau n'est pas dévié, profil d'intensité mesuré gaussien, maximum d'intensité à la même position que la fente du four. 
    - Force subie par les atomes est $\vec{F} = \vec{M}\cdot\vec{\nabla} \vec{B}$ avec $\vec{M} = g\frac{\mu_b}{\hbar}\vec{L}$ $\rightarrow$ donc force nulle car état fondamental
  - Quantiquement: prise en compte du moment magnétique de spin donc le moment magnétique total devient : $\vec{M_{tot}} = g\frac{\mu_b}{\hbar}(\vec{L} + \vec{S})$ donc force non-nulle même à l'état fondamental car présence du spin. Donc séparation du faisceau en deux et observation de deux pics d'intensité de part et d'autre du centre.
- Objectifs du laboratoire
  - Déterminer les conditions expérimentales de production et de détection d’un jet atomique
    de potassium. (présentation du montage)
  - Vérifier la loi de LANGMUIR (Expérience 1)
  - Mesurer la distribution spatiale du jet atomique non-défléchi (Expérience 2)
    - Déterminer les conditions optimales d’observation du phénomène de quantification
      spatiale
  - Mesurer la distribution spatiale du jet atomique défléchi. (Expérience 3)
    - Mettre en évidence le phénomène de déflexion magnétique d’un jet atomique dans un
      champ magnétique non uniforme
    - Évaluer l’ordre de grandeur du gradient moyen du champ magnétique non uniforme
      responsable de la déflexion magnétique du jet de potassium

# 2. Présentation montage

- Appareils utilisés : 

  - Four (chauffer potassium sous vide pour vaporiser et créer faisceau de particules)
  - Pompe à vide (pour éviter les collisions avec d'autres atomes)
  - Electro-aimant (appliquer un champ magnétique non-uniforme)
  - Détecteur (filament de tungstène chauffé, pour qu'au contact du filament les atomes de potassium s'ionisent, et entouré d'une cage de Faraday pour attirer les atomes ionisés)
  - Moteur + capteurs (permet de déplacer le détecteur et toujours parcourir la même distance depuis la même psosition)
  - Sources de courant : $I_{\text{détecteur}}$ et $I_{\text{électro-aimant}}$ 
  - Source de tension : $V_{\text{cage de Faraday}}$
  - Réglage de la température du four
  - Pico-ampèremètre (mesurer l'intensité du courant d'ions produit par le filament)
  - Oscilloscope & Picolog (visualisation des données)

- Résumé bref de la mesure du parcours et de la mesure du faisceau

  

# 3. Vérification de la loi de Langmuir

- Théorie
  - On chauffe du potassium dans le four (sous vide) pour le vaporiser. Avec la fente étroite du four, seuls les atomes avec une direction perpendiculaire à la surface du four pourront passer.
  - La pression de vapeur des atomes de potassium est supposée suivre la loi de Langmuir (pression de vapeur d'une substance en équilibre thermodynamique dans un four maintenu à une température T) : $\ln(p) = A - \frac{\Lambda}{T} = A - \frac{\Phi}{k_BT}$ donc $p = Ce^{-\frac{\Lambda}{T}} = Ce^{-\frac{\Phi}{k_BT}}$ 
  - On sait également que l'intensité du jet atomique issu de l'ouverture du four à température T est: $I_{jet} = 1.11\times 10^{22}\frac{ap\cos(\theta)}{r^2\sqrt{M_{ato}T}}$ $\text{molécules}.cm^{-2}.s^{-1}$. Après la conversion en ampère et en prenant compte l'efficacité du détecteur (combien d'atomes de potassium sont ionisés par rapport au total d'atomes de potassium), l'intensité mesurée $I_{mes}$par le pico-ampèremètre est proportionnelle à l'intensité du jet atomique $I_{jet}$ : $I_{mes} = \frac{C'}{\sqrt{T}}e^{-\frac{\Lambda}{T}} = \frac{C'}{\sqrt{T}}e^{-\frac{\Phi}{k_BT}}$. 
    $\rightarrow$ On peut tracer la courbe $I_{mes}\times\sqrt{T} = C'\times e^{-\frac{\Lambda}{T}}$ (*) et faire un fit exponentiel pour trouver les paramètres $\Lambda$ et $\Phi$.
- Matériel et Méthodes
  - Le détecteur est préalablement placé à l'endroit où l'intensité est maximale.
  - Le courant du filament est amené à 3.0A, puis on attend 5min pour que sa température se stabilise.
  - La cage de faraday est amenée à 5.0V
  - Le pico-ampèremètre est utilisée à la position '+' pour capter les ions, et l'échelle utilisée est de 0.1nA. 
  - On prend les mesures de température à chaque fois que l'aiguille passe 0. 01nA (avantage d'être plus précis que si on prenait le courant pour chaque augmentation d'un degré car aiguille peut se trouver entre 2 graduations). Arrivé à la saturation de l'échelle, on passera à l'échelle de 0.3nA (se verra sur l'incertitude des points de la courbe) jusqu'à s'arrêter à une intensité de 0.15nA.
- Résultats et analyse
  - On peut alors tracer la courbe (*) et faire le fit exponentiel (voir graphe).
  - La courbe à bien une décroissance exponentielle, ce qui vérifie le comportement prédit par la loi de Langmuir. Avec le fit, on peut déduire la valeur approximative des paramètres $\Lambda$ et $\Phi$ (voir valeurs). On remarque un certain écart entre les valeurs théoriques et expérimentales, notamment car le courant de bruit de fond constant n'a pas été soustrait aux données. Mais on obtient au moins l'ordre de grandeur des valeurs de $\Lambda$ et $\Phi$. Le but ici était de valider expérimentalement la loi de Langmuir.



# 4. Distribution spatiale du jet non-défléchi

- Théorie
  - But : Déterminer les conditions optimales d’observation du phénomène de quantification spatiale
  - Comme attendu classiquement, sans champ magnétique non-uniforme appliqué, le faisceau ne doit pas être dévié. Distribution gaussienne avec comme maximum la position en face de la fente du four.
  - Détermination du rapport $\text{Signal}/\text{Bruit}$ : $(V_{pic} - V_{fond}) / V_{fond}$. 
- Matériel et Méthodes
  - On amène le courant du filament à 2.8A (toujours attendre la stabilisation), et la tension de la cage de Faraday à 5.0V
  - On positionne le détecteur à une des extrémités.
  - On start l'oscilloscope, puis on sélectionne la position '+' et on démarre le moteur en même temps. On a alors un repère pour le moment où le détecteur à commencer à mesurer. On refait la même chose à la fin (à l'envers bien sûr) et on a un repère pour la fin de la mesure. 
  - On peut alors calculer le temps passé pour effectuer la mesure (entre les deux repères), et sachant la distance parcourue en regardant la position de la vis micrométrique à chaque extrémité, on a une conversion $sec \rightarrow mm$. 
  - On réitère l'opération pour des valeurs différentes de $I_{détecteur}$ (avec valeurs fixes de $V_{cage}$), et on évalue le rapport $\text{Signal}/\text{Bruit}$ pour chaque prise de mesures, pour ensuite continuer avec la valeur de $I_{détecteur}$ qui donne un rapport $\text{Signal}/\text{Bruit}$ le plus élevé en faisant varier cette fois-ci $V_{cage}$. 
- Résultats et Analyse
  - (voir tableaux)
  - On a un meilleur rapport $\text{Signal}/\text{Bruit}$ pour un $I_{détecteur} = 2.9A$ et $V_{cage} = 5.0V$. 
  - On remarque également (voir sur graphe oscillo) que le pic est asymétrique. Plusieurs hypothèses sont émises : 
    - Au fur et a mesure que le détecteur se déplace, un dépôt de potassium se forme sur ce dernier, ce qui a pour effet d'ioniser des atomes qui ne sont pas forcément envoyés par le faisceau mais qui sont ionisés directement depuis le dépôt.
    - Le détecteur se rapproche du maximum d'intensité du faisceau au début et s'en éloigne à la fin. 
    - L'intensité du faisceau augmente peut-être avec le temps. 