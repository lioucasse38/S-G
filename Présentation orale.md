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
  - Moteur + capteurs (permet de déplacer le détecteur et toujours parcourir la même distance depuis la même position)
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
  - > Le pico-ampèremètre est utilisée à la position '+' pour capter les ions, et l'échelle utilisée est de 0.1nA. 
  - > On prend les mesures de température à chaque fois que l'aiguille passe 0. 01nA (avantage d'être plus précis que si on prenait le courant pour chaque augmentation d'un degré car aiguille peut se trouver entre 2 graduations). Arrivé à la saturation de l'échelle, on passera à l'échelle de 0.3nA (se verra sur l'incertitude des points de la courbe) jusqu'à s'arrêter à une intensité de 0.15nA.
- Résultats et analyse
  - On peut alors tracer la courbe (*) et faire le fit exponentiel (voir graphe).
  - La courbe à bien une décroissance exponentielle, ce qui vérifie le comportement prédit par la loi de Langmuir. Avec le fit, on peut déduire la valeur approximative des paramètres $\Lambda$ et $\Phi$ (voir valeurs). On remarque un certain écart entre les valeurs théoriques et expérimentales, notamment car le courant de bruit de fond constant n'a pas été soustrait aux données. Mais on obtient au moins l'ordre de grandeur des valeurs de $\Lambda$ et $\Phi$. Le but ici était de valider expérimentalement la loi de Langmuir.



# 4. Distribution spatiale du jet non-défléchi

- Théorie
  - But : Déterminer les conditions optimales d’observation du phénomène de quantification spatiale
  - Comme attendu classiquement, sans champ magnétique non-uniforme appliqué, le faisceau ne doit pas être dévié. Distribution gaussienne avec comme maximum la position alignée avec la fente du four.
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
  
  # 5. Distribution spatiale du jet défléchi
  
- Théorie

  - Comme vu dans l'introduction, les atomes subissent une force à cause du champ magnétique non-uniforme et de leur moment magnétique de spin. On est alors censé observer une déflexion du faisceau en deux si les atomes se trouvent dans leur état fondamental. Avec une analyse statistique du gaz de potassium et du faisceau qui en résulte et une étude des forces appliquées aux atomes de potassium, on peut déterminer la déflexion des atomes avec la vitesse la plus probable (qui se trouve être $v_m = \sqrt{\frac{3k_BT}{m_{potass}}}$ après l'analyse de la distribution des vitesses et du flux de particules généré à la sortie du four).
  -  On se retrouve alors avec la déflexion en fonction du gradient du champ magnétique appliqué : $s_m = \pm \frac{d}{3T}(D + d/2)\frac{\mu_B}{k_B}\frac{\partial B}{\partial z}$. Où D est la distance entre la fin de l'électro-aimant et la position du "mur" où les atomes sont observés, et d la longueur que les atomes parcourent dans l'électro-aimant.
  - Il est également possible d'obtenir la valeur du champ magnétique moyen de l'électro-aimant : $B_{moyen} \approx a\times \frac{\partial B}{\partial z}$ où $a$ est un paramètre de notre électro-aimant valant $5.5mm$, si le champ magnétique était produit par deux fils parallèles de longueur infinie, $a$ serait la moitié de la distance les séparant.

- Matériel et méthode

  - Même technique pour que pour le jet non-défléchi pour avoir un repère lors de l'acquisition des données. On utilise les paramètres optimaux trouvés précédemment pour le courant de détecteur et la tension de la cage de Faraday. On mesure le profil du jet défléchi pour des valeurs de courant de bobine fixes.
  - On fait varier le courant appliqué dans la bobine de l'électro-aimant pour faire varier le gradient du champ magnétique et prendre d'autres mesures du profil. 
  - On mesure la position des pics $s_+$ et $s_-$ par rapport au creux, avec la conversion $sec \rightarrow mm$, on peut trouver la déflexion en $mm$.
  - Avec un $D = 49.1cm$ et $d = 9.5cm$, on peut calculer la valeur du gradient du champ en fonction de $s$ et de $T$  d'après la formule vue précédemment: $\frac{\partial B}{\partial z} (T.cm^{-1})= 8,01\times 10^{-4}\times s(mm) \times T(K)$ .
  - On peut ainsi en déduire le champ magnétique moyen.

- Résultats et analyse

  - On obtient un profil comme attendu, le faisceau est séparé en deux, de part et d'autre du centre.
  - On peut d'abord tracer les écarts $s_+$ et $s_-$ obtenus en fonction du courant appliqué à la bobine. (voir graphe), ce qui nous permet de faire un fit linéaire pour ensuite avoir la valeur du gradient du champ magnétique pour différents courants (à l'aide de la formule précédente), et ainsi en déduire la valeur du champ magnétique moyen pour différents courants. (voir graphe)
  - On remarque donc que la déflexion augmente avec le courant, ce qui était prévisible car le champ magnétique créé par l'électro-aimant augmente linéairement avec le courant.
  - Après avoir trouvé les valeurs de champ magnétique moyen en fonction du courant, on remarque que l'ordre de grandeur du champ magnétique est  environ $0.4 \space T$, ce qui est raisonnable est cohérent selon notre configuration (les valeurs typiques de champ magnétique pour ce type).
  - Quoi dire d'autre ??

> # 6. Evaluation du nombre d'atomes dans le jet non-défléchi
>
> - Théorie
>   - On a mesuré des profils d'intensité pour le jet non-défléchi, en connaissant l'aire sous la courbe grâce à la formule suivante : $\text{Aire} [nA.s]= 1.065(I_{pic} - I_{fond})\times\text{FWHM}$, on peut déduire directement le nombre d'atomes captés si on considère l'efficacité du détecteur de 100%.
>   - On a la charge d'un ion qui est égale à $1.6\times10^{-19} \space C$. Comme le coulomb est également des $A.s$, on peut obtenir le nombre d'atomes par : $\#\text{atomes} = \frac{\text{Aire}}{1.6\times10^{-19}C}$. 
> - Matériel et méthode
>   - On prend comme exemple le profil obtenu pour les paramètres optimaux.
> - Résultats
>   - En utilisant la formule, on trouve que $5.14\times10^{9}$ atomes ont été perçus par le détecteur, avec l'efficacité d'ionisation supposée de 100%, il y a le même nombre d'atomes de potassium qui ont été envoyés par le jet non-défléchi.

# Conclusion

Les objectifs du laboratoire étant de vérifier le comportement de la loi de Langmuir et de mesurer la distribution spatiale des jets défléchi et non-défléchi, on a démontré que le gaz de potassium se comportait bien selon cette loi, le bruit de fond aurait pu être soustrait pour pouvoir mesurer précisément les paramètres $\Lambda$ et $\Phi$. Quant aux mesures liées aux jets, on obtient bien des mesures selon les prédictions les plus récentes (on a connaissance du spin maintenant lol) et on a vérifié la loi de la déflexion magnétique en calculant les écarts  $s_+$ et $s_-$ en faisant varier le gradient du champ.  



Ce qui met fin à notre présentation, merci de nous avoir écouté.